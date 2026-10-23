#!/usr/bin/env python3
"""Sweep one Claude Code version for env names and settings keys.

    python3 -I .claude/skills/sweep-switches/sweep.py <X.Y.Z> [--tarball PATH] [--docs DIR] [--previous PATH]

Writes .claude/switch-sweeps/<version>.json and prints a markdown report.
Never edits the switch registry. Stdlib only, Python 3.11 or newer.
"""

import argparse
import json
import platform
import re
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
SWEEPS = REPO / ".claude" / "switch-sweeps"
REGISTRY = REPO / "plugin" / "unharness" / "src" / "unharness" / "switches.json"
PACKAGE = "@anthropic-ai/claude-code"
DOC_PAGES = {
    "env-vars.md": "https://code.claude.com/docs/en/env-vars.md",
    "settings-reference.md": "https://code.claude.com/docs/en/settings-reference.md",
}
BIG_FILE = 1_000_000

ENV_READ = re.compile(rb"""process\.env(?:\.([A-Za-z_][A-Za-z0-9_]*)|\[["']([A-Za-z_][A-Za-z0-9_]*)["']\])""")
ENV_LITERAL = re.compile(rb"\bCLAUDE_CODE_[A-Z0-9_]+\b")
SETTINGS_KEY = re.compile(
    rb"[{,]([a-z][A-Za-z0-9]+):[\w$]{1,3}\."
    rb"(?:boolean|string|number|enum|array|object|record|union|literal)\("
)
# Claude Code 2.1.309 builds its settings schema lazily: key:()=>O().optional().describe("...").
SETTINGS_LAZY = re.compile(
    rb"[{,]([a-z][A-Za-z0-9]+):\(\)=>[\w$]{1,6}\(\)(?:\.[a-z]+\([^()]{0,60}\)){0,3}?\.describe\("
)
BACKTICK = re.compile(r"`([^`\n]+)`")
LEADING_NAME = re.compile(r"[\"']?([A-Za-z_][A-Za-z0-9_]*)")
VERSION = re.compile(r"\d+\.\d+\.\d+")


class SweepError(Exception):
    pass


def version_key(text):
    return tuple(int(part) for part in text.split("."))


def obtain_tarball(package, version, folder):
    try:
        run = subprocess.run(
            ["npm", "pack", f"{package}@{version}", "--pack-destination", str(folder)],
            capture_output=True, text=True, timeout=300,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise SweepError(f"npm pack failed to run: {error}; pass --tarball PATH") from error
    if run.returncode != 0:
        raise SweepError(f"npm pack {package}@{version} failed: {run.stderr.strip()}")
    packed = sorted(folder.glob("*.tgz"))
    if not packed:
        raise SweepError(f"npm pack wrote no tarball into {folder}")
    return packed[0]


def platform_package():
    """The per-platform package that holds the native binary on this host."""
    system = {"darwin": "darwin", "linux": "linux", "win32": "win32"}.get(sys.platform)
    machine = {"arm64": "arm64", "aarch64": "arm64", "x86_64": "x64", "amd64": "x64"}.get(platform.machine().lower())
    if system is None or machine is None:
        raise SweepError(f"no platform package for {sys.platform}/{platform.machine()}; pass --tarball PATH")
    musl = "-musl" if system == "linux" and any(Path("/lib").glob("ld-musl*")) else ""
    return f"{PACKAGE}-{system}-{machine}{musl}"


def read_source(tarball, folder):
    """Return (source name, bytes) from package/cli.js, else from the files over 1 MB; None when neither exists."""
    with tarfile.open(tarball) as archive:
        archive.extractall(folder, filter="data")
    cli = folder / "package" / "cli.js"
    if cli.is_file():
        return "cli.js", cli.read_bytes()
    big = [p for p in sorted((folder / "package").rglob("*")) if p.is_file() and p.stat().st_size > BIG_FILE]
    if not big:
        return None
    return "bytes:" + ",".join(p.name for p in big), b"\n".join(p.read_bytes() for p in big)


def extract(text):
    def names(found):
        return sorted({n.decode("ascii") for n in found})

    reads = names(a or b for a, b in ENV_READ.findall(text))
    return reads, names(ENV_LITERAL.findall(text)), names(SETTINGS_KEY.findall(text) + SETTINGS_LAZY.findall(text))


def read_docs(docs_dir):
    pages = {}
    for name, url in DOC_PAGES.items():
        if docs_dir is not None:
            path = Path(docs_dir) / name
            if not path.is_file():
                raise SweepError(f"{path} is missing; --docs DIR needs {', '.join(DOC_PAGES)}")
            pages[name] = path.read_text(encoding="utf-8")
            continue
        try:
            request = urllib.request.Request(url, headers={"User-Agent": "sweep-switches"})
            with urllib.request.urlopen(request, timeout=60) as response:
                pages[name] = response.read().decode("utf-8")
        except OSError as error:
            raise SweepError(f"cannot fetch {url}: {error}; pass --docs DIR holding {', '.join(DOC_PAGES)}") from error
    return pages


def backticked_names(markdown):
    """Leading identifier of every inline code span: `NAME=1` gives NAME, `attribution.pr` gives attribution."""
    names = set()
    for span in BACKTICK.findall(markdown):
        found = LEADING_NAME.match(span.strip())
        if found:
            names.add(found.group(1))
    return names


def documented(pages):
    env_page = backticked_names(pages["env-vars.md"])
    settings_page = backticked_names(pages["settings-reference.md"])
    env = sorted(n for n in env_page if re.fullmatch(r"[A-Z][A-Z0-9_]+", n))
    settings = sorted(n for n in settings_page if re.fullmatch(r"[a-z][A-Za-z0-9]+", n))
    return env, settings


def find_previous(version, explicit):
    if explicit is not None:
        path = Path(explicit)
        if not path.is_file():
            raise SweepError(f"--previous {path} is not a file")
        return path
    others = [p for p in SWEEPS.glob("*.json") if VERSION.fullmatch(p.stem) and p.stem != version]
    return max(others, key=lambda p: version_key(p.stem), default=None)


def names_of(record):
    return set(record["env"]) | set(record["literals"]) | set(record["settings_candidates"])


def registry_absent(record, text):
    """Registry switches this version's names do not hold."""
    if not REGISTRY.is_file():
        return None
    absent = []
    for entry in json.loads(REGISTRY.read_text(encoding="utf-8")):
        name, kind = entry["name"], entry["kind"]
        if kind == "env":
            held = name in record["env"] or name in record["literals"]
        elif kind == "settings":
            held = name in record["settings_candidates"] or name.encode() + b":" in text or b'"' + name.encode() + b'"' in text
        else:
            held = name.encode() in text
        if not held:
            absent.append(f"{name} ({kind})")
    return absent


def section(title, items):
    body = "\n".join(f"- `{i}`" for i in items) if items else "none"
    return f"## {title}\n\n{body}\n"


def report(record, source, previous, previous_name, absent):
    docs_env = set(record["documented_env"])
    docs_settings = set(record["documented_settings"])
    env_names = set(record["env"]) | set(record["literals"])
    lines = [f"# Switch sweep of {record['version']}\n", f"Source: {source}\n"]
    lines.append(section("Undocumented env names", sorted(env_names - docs_env)))
    lines.append(section("Undocumented settings candidates", sorted(set(record["settings_candidates"]) - docs_settings)))
    if previous is None:
        lines.append("## New and gone since the previous sweep\n\nno previous sweep\n")
    else:
        now, before = names_of(record), names_of(previous)
        lines.append(section(f"New since {previous_name}", sorted(now - before)))
        lines.append(section(f"Gone since {previous_name}", sorted(before - now)))
    if absent is None:
        lines.append("## Registry switches absent from this version\n\nregistry not found\n")
    else:
        lines.append(section("Registry switches absent from this version", absent))
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("version")
    parser.add_argument("--tarball")
    parser.add_argument("--docs")
    parser.add_argument("--previous")
    args = parser.parse_args(argv)
    try:
        if not VERSION.fullmatch(args.version):
            raise SweepError(f"{args.version!r} is not X.Y.Z")
        with tempfile.TemporaryDirectory() as temp:
            work = Path(temp)
            extracted = work / "extracted"
            extracted.mkdir()
            if args.tarball:
                tarball = Path(args.tarball)
                if not tarball.is_file():
                    raise SweepError(f"--tarball {tarball} is not a file")
                found = read_source(tarball, extracted)
            else:
                found = read_source(obtain_tarball(PACKAGE, args.version, work), extracted)
                if found is None:
                    native = work / "native"
                    native.mkdir()
                    found = read_source(obtain_tarball(platform_package(), args.version, native), native / "extracted")
            if found is None:
                raise SweepError("the tarball holds no package/cli.js and no file over 1 MB")
            source, text = found
        reads, literals, candidates = extract(text)
        doc_env, doc_settings = documented(read_docs(args.docs))
        record = {
            "version": args.version,
            "env": reads,
            "literals": literals,
            "settings_candidates": candidates,
            "documented_env": doc_env,
            "documented_settings": doc_settings,
        }
        previous_path = find_previous(args.version, args.previous)
        previous = json.loads(previous_path.read_text(encoding="utf-8")) if previous_path else None
        output = report(record, source, previous, previous_path.stem if previous_path else None,
                        registry_absent(record, text))
        SWEEPS.mkdir(parents=True, exist_ok=True)
        (SWEEPS / f"{args.version}.json").write_text(json.dumps(record, indent=1) + "\n", encoding="utf-8")
    except SweepError as error:
        print(f"sweep: {error}", file=sys.stderr)
        return 1
    print(output)
    return 0


if __name__ == "__main__":
    sys.exit(main())
