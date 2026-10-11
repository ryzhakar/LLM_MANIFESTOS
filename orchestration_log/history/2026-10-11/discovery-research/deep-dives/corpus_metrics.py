#!/usr/bin/env python3
"""Corpus metrics for /home/user/LLM_MANIFESTOS/manifestos/*.md.

Run:  python3 -I corpus_metrics.py            (markdown tables: metrics + hand-check)
      python3 -I corpus_metrics.py --json     (all per-file values as JSON)
      python3 -I corpus_metrics.py --sample   (list the hand-check sample, no labels needed)
      python3 -I corpus_metrics.py --firstwords   (first-word frequency of non-imperative sentences)

Standard library only. Deterministic: the hand-check sample is seeded.
"""
import glob
import json
import os
import random
import re
import statistics
import sys

MANIFESTO_DIR = "/home/user/LLM_MANIFESTOS/manifestos"
SEED = "manifesto-craft-tier0-corpus-audit"
LONG_SENTENCE = 20      # "over 20 words"
LONG_SECTION = 150      # "over 150 words"
FRAGMENT_MAX = 4        # "4 words or fewer"
SAMPLE_PER_FILE = 10
SAMPLE_PER_STRATUM = 5

# ---------------------------------------------------------------- text parsing

def split_frontmatter(text):
    """Return (body_lines, first_body_line_number). Frontmatter = leading ---/--- block."""
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return lines[i + 1:], i + 2
    return lines, 1


def classify(body_lines):
    """Tag every body line: fence, code, blank, table, heading, hr, text."""
    out = []
    in_code = False
    for ln in body_lines:
        s = ln.strip()
        if s.startswith("```"):
            out.append(("fence", ln))
            in_code = not in_code
            continue
        if in_code:
            out.append(("code", ln))
            continue
        if not s:
            kind = "blank"
        elif s.startswith("|"):
            kind = "table"
        elif re.match(r"#{1,6}\s", s):
            kind = "heading"
        elif re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", s):
            kind = "hr"
        else:
            kind = "text"
        out.append((kind, ln))
    return out


TOKEN_SPLIT = re.compile(r"[\s—–]+")


def words_of(text):
    """A word = whitespace/dash-delimited token holding at least one letter or digit."""
    return [t for t in TOKEN_SPLIT.split(text.replace("|", " ")) if re.search(r"[A-Za-z0-9]", t)]


LIST_MARK = re.compile(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|>\s*)")
EDGE_UNDERSCORE = re.compile(r"(?<![A-Za-z0-9])_|_(?![A-Za-z0-9])")
SENT = re.compile(r"\S.*?(?:[.!?]+[\"'”’)\]]*(?=\s|$)|$)")
ABBREV_END = re.compile(r"(?:\b(?:Mr|Mrs|Ms|Dr|vs)|\be\.g|\bi\.e)\.$|\b[A-Z][A-Za-z]+ [A-Z]\.$")
TERMINATED = re.compile(r"[.!?]+[\"'”’)\]]*$")


MASK = {".": "\ue000", "!": "\ue001", "?": "\ue002"}
UNMASK = {v: k for k, v in MASK.items()}


def mask_inline_code(s):
    """Sentence terminators inside an inline-code span do not end a sentence."""
    def repl(m):
        return "".join(MASK.get(c, c) for c in m.group(0))
    return re.sub(r"`[^`]*`", repl, s)


def clean_unit(line):
    s = line.strip()
    s = LIST_MARK.sub("", s)
    s = mask_inline_code(s)
    s = s.replace("**", "").replace("*", "").replace("`", "")
    s = EDGE_UNDERSCORE.sub("", s)
    return s.strip()


def split_sentences(unit):
    pieces = SENT.findall(unit)
    merged = []
    i = 0
    while i < len(pieces):
        p = pieces[i]
        while ABBREV_END.search(p) and i + 1 < len(pieces):
            i += 1
            p = p + " " + pieces[i]
        merged.append(p.strip())
        i += 1
    restore = str.maketrans(UNMASK)
    return [p.translate(restore) for p in merged if words_of(p)]


# ---------------------------------------------------------------- imperative heuristic

LEAD_SKIP = {"always", "then", "now", "first", "next", "also", "just", "please", "instead",
             "finally", "actually", "simply", "only", "still", "but", "or", "and", "so"}

BASE_VERBS = set("""
abstract accept accumulate act add admit adopt aim allow amend answer apply arrange ask assert assume
attack avoid balance batch be begin believe bind blame borrow break bring build bury buy calculate capture
carry cast challenge check choose clone collapse commit communicate compare complete confirm connect
continue convert copy count cover crank create crush cut decide declare decompose decomplect decouple deconstruct define delete
demand deny deploy derive describe design determine develop diagnose dig disable discard discover document
do doubt draw drop dump duplicate eat embrace enable encode enforce ensure enter escape evaluate evolve examine expect
explain explore express extend extract feed fetch fight fill filter find finish fix flatten flip follow
force forget gather generate get give go grab grant grow guess handle hate help hide hit hold hunt identify
ignore imagine implement import improve include increase inherit inject inline inspect install introduce
invest isolate iterate jump justify keep kill know launch lay lead learn leave let lift listen load lock
look maintain make manage map measure memorize merge minimize mirror mix model monitor move name note notice
obey observe offer omit open optimize override participate pass pay perform persist pick place pour practice predict
prefer prepare press pretend prevent prioritize produce promise propose protect prove provide publish pull
push put question quote raise rank reach read realize recognize reconstruct reduce refactor refer refuse
reject release remember remove rename repair repeat replace report represent require reserve resist resolve
respect respond restore retire return reuse reveal review revoke rewrite rip roll run save say scan scrap
search see seek select send separate serve set shape share shift ship show shrink shut sit size skip solve
sort speak specify spend split spread stand start state stay step stick store strengthen strip strive study
substitute summarize supply surrender swap switch take talk teach tell test think throw tighten tolerate
track train transform treat trust try tune turn unbraid understand undo unify untangle update use utilize validate
verify wait walk warn watch weigh wonder worry wrap write
""".split())


def is_imperative(sentence):
    t = sentence.replace("’", "'").lstrip(" \"'“”‘([{-—_*`")
    low = t.lower()
    m = re.match(r"([a-z]+(?:'[a-z]+)?)", low)
    if not m:
        return False
    w = m.group(1)
    if w in LEAD_SKIP:
        low = low[m.end():].lstrip(" ,")
        m = re.match(r"([a-z]+(?:'[a-z]+)?)", low)
        if not m:
            return False
        w = m.group(1)
    if w in ("never", "stop", "don't") or re.match(r"do\s+not\b", low):
        return True
    if w == "do" and re.match(r"do\s+(you|we|they|i|he|she|it)\b", low):
        return False
    return w in BASE_VERBS


# ---------------------------------------------------------------- per-file measurement

HEDGE_RE = re.compile(
    r"(?<![a-z'])(i think|perhaps|maybe|it seems|sort of|kind of|might|could|should consider|somewhat|quite)(?![a-z'])")
CAPS_RE = re.compile(r"(?<![A-Za-z])[A-Z]{3,}(?![A-Za-z])")
QUOTE_SPAN = re.compile(r"[\"“][^\"“”]*[\"”]")
TICK_SPAN = re.compile(r"`[^`]*`")
SECOND_CORE = {"you", "your", "you're", "yourself"}
SECOND_EXT_EXTRA = {"you've", "you'll", "you'd", "yours", "yourselves"}


def in_spans(pos, spans):
    return any(a <= pos < b for a, b in spans)


def per1k(n, base):
    return 1000.0 * n / base if base else 0.0


def measure(path):
    name = os.path.basename(path)
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    body_lines, first_line_no = split_frontmatter(text)
    tagged = classify(body_lines)

    words = 0
    code_words = 0
    sentences = []            # cleaned sentence strings, in order
    sent_words = []
    unterminated_units = 0
    wrap_candidates = 0
    tables = 0
    code_blocks = 0
    prev_kind = None
    prev_unit_terminated = True
    prev_unit_adjacent = False
    sections = []             # word counts per ## section
    preamble_words = 0
    cur_section = None
    h2_titles = []

    hedge_counts = {}
    hedge_total = 0
    hedge_quoted = 0
    caps_total = 0
    caps_in_headings = 0
    caps_in_ticks = 0
    excl = 0
    second_core = 0
    second_ext = 0
    articles = 0
    in_fence = False

    for kind, ln in tagged:
        if kind == "fence":
            if not in_fence:
                code_blocks += 1
            in_fence = not in_fence
            prev_kind = kind
            continue
        if kind == "code":
            code_words += len(words_of(ln))
            prev_kind = kind
            continue
        # ---- non-code line
        w = len(words_of(ln))
        words += w
        s = ln.strip()
        is_h2 = kind == "heading" and re.match(r"##(?!#)\s", s) is not None
        if is_h2:
            if cur_section is not None:
                sections.append(cur_section)
            cur_section = 0
            h2_titles.append(re.sub(r"^##\s*", "", s))
        else:
            if cur_section is None:
                preamble_words += w
            else:
                cur_section += w
        if kind == "table" and prev_kind != "table":
            tables += 1

        # ---- character-level rates (headings and tables included, code excluded)
        norm = ln.replace("’", "'")
        low = norm.lower()
        qspans = [m.span() for m in QUOTE_SPAN.finditer(low)]
        for m in HEDGE_RE.finditer(low):
            hedge_total += 1
            hedge_counts[m.group(1)] = hedge_counts.get(m.group(1), 0) + 1
            if in_spans(m.start(), qspans):
                hedge_quoted += 1
        tspans = [m.span() for m in TICK_SPAN.finditer(norm)]
        for m in CAPS_RE.finditer(norm):
            caps_total += 1
            if kind == "heading":
                caps_in_headings += 1
            elif in_spans(m.start(), tspans):
                caps_in_ticks += 1
        excl += TICK_SPAN.sub("", norm).count("!")
        for tok in re.findall(r"[a-z]+(?:'[a-z]+)*", low):
            if tok in SECOND_CORE:
                second_core += 1
                second_ext += 1
            elif tok in SECOND_EXT_EXTRA:
                second_ext += 1
            if tok in ("a", "an", "the"):
                articles += 1

        # ---- sentence units
        if kind == "text":
            unit = clean_unit(ln)
            pieces = split_sentences(unit)
            if pieces:
                if not TERMINATED.search(pieces[-1]):
                    unterminated_units += 1
                for p in pieces:
                    sentences.append(p)
                    sent_words.append(len(words_of(p)))
                # candidate mid-sentence wrap: previous adjacent unit unterminated and this one starts lowercase
                if prev_kind == "text" and not prev_unit_terminated and unit[:1].islower():
                    wrap_candidates += 1
                prev_unit_terminated = bool(TERMINATED.search(pieces[-1]))
        prev_kind = kind
    if cur_section is not None:
        sections.append(cur_section)

    imp_flags = [is_imperative(s) for s in sentences]
    n_sent = len(sentences)
    rate_base = words
    res = {
        "file": name,
        "words": words,
        "code_words": code_words,
        "lines": len(body_lines),
        "sentences": n_sent,
        "mean_sentence_words": statistics.mean(sent_words) if sent_words else 0.0,
        "max_sentence_words": max(sent_words) if sent_words else 0,
        "pct_sentences_over20": 100.0 * sum(1 for x in sent_words if x > LONG_SENTENCE) / n_sent if n_sent else 0.0,
        "h2_sections": len(sections),
        "h2_titles": h2_titles,
        "max_section_words": max(sections) if sections else None,
        "pct_sections_over150": (100.0 * sum(1 for x in sections if x > LONG_SECTION) / len(sections)) if sections else None,
        "sections_detail": [{"title": t, "words": w} for t, w in zip(h2_titles, sections)],
        "sections_under20_words": sum(1 for x in sections if x < 20),
        "sentences_over15": sum(1 for x in sent_words if x > 15),
        "articles_count": articles,
        "preamble_words": preamble_words,
        "tables": tables,
        "code_blocks": code_blocks,
        "second_person_per1k": per1k(second_core, rate_base),
        "second_person_count": second_core,
        "second_person_ext_count": second_ext,
        "hedge_per1k": per1k(hedge_total, rate_base),
        "hedge_count": hedge_total,
        "hedge_in_quotes": hedge_quoted,
        "hedge_terms": hedge_counts,
        "caps_per1k": per1k(caps_total, rate_base),
        "caps_count": caps_total,
        "caps_in_headings": caps_in_headings,
        "caps_in_backticks": caps_in_ticks,
        "caps_other": caps_total - caps_in_headings - caps_in_ticks,
        "excl_per1k": per1k(excl, rate_base),
        "excl_count": excl,
        "fragments_per1k": per1k(sum(1 for x in sent_words if x <= FRAGMENT_MAX), rate_base),
        "fragments_count": sum(1 for x in sent_words if x <= FRAGMENT_MAX),
        "imperative_count": sum(imp_flags),
        "imperative_pct": 100.0 * sum(imp_flags) / n_sent if n_sent else 0.0,
        "unterminated_units": unterminated_units,
        "wrap_candidates": wrap_candidates,
        "first_body_line": first_line_no,
    }
    return res, sentences, imp_flags


# ---------------------------------------------------------------- hand-check sample

def build_sample(name, imp_flags):
    rng = random.Random(f"{SEED}:{name}")
    pos = [i for i, f in enumerate(imp_flags) if f]
    neg = [i for i, f in enumerate(imp_flags) if not f]
    take_pos = min(SAMPLE_PER_STRATUM, len(pos))
    take_neg = min(SAMPLE_PER_STRATUM, len(neg))
    # fill to SAMPLE_PER_FILE from the larger stratum when the other is short
    short = SAMPLE_PER_FILE - take_pos - take_neg
    if short > 0:
        extra_pos = min(short, len(pos) - take_pos)
        take_pos += extra_pos
        short -= extra_pos
        take_neg += min(short, len(neg) - take_neg)
    chosen = rng.sample(pos, take_pos) + rng.sample(neg, take_neg)
    return sorted(chosen)


# Hand labels: for each file, {sentence index: (truth, first 40 characters of the sentence)}.
# truth = True when the sentence is grammatically an imperative clause (command form;
# quoted commands count by form), else False. Assigned by reading the --sample listing.
HAND_LABELS = {
    'cargo-cult-science.md': {
        17: (False, 'Then I became overwhelmed.'),
        21: (False, 'She says OK, so she gets up on a table a'),
        37: (False, '(And I thought then about the witch doct'),
        39: (False, 'There are big schools of reading methods'),
        55: (False, 'I will have to limit myself to just a fe'),
        106: (False, 'And so they eliminated the numbers that '),
        120: (False, 'He does work on cosmology and astronomy,'),
        123: (False, 'I think that’s kind of dishonest.'),
        149: (False, 'Nowadays there’s a certain danger of the'),
        163: (False, 'Obviously there was something about the '),
    },
    'correct-by-construction.md': {
        5: (True, 'Move fast and break things.'),
        12: (False, 'Neither am I.'),
        36: (False, 'Cannot.'),
        73: (True, 'Write the function signature.'),
        82: (True, 'Add tests for logic.'),
        101: (False, 'Type mismatches become compiler errors.'),
        105: (True, 'Pay at compile time or pay forever in pr'),
        119: (False, 'You can write code where the compiler do'),
        132: (True, 'Pay upfront.'),
        142: (False, 'Done is the engine of more.'),
    },
    'dry.md': {
        14: (True, 'Push them back, they never disappear.'),
        34: (False, 'They will diverge.'),
        43: (True, 'Fix it.'),
        63: (False, 'Quality risk escalates'),
        66: (False, 'Another described "elegant code" rotting'),
        105: (False, "You'll build the wrong abstraction."),
        154: (True, 'Write them when they feel right.'),
        166: (True, 'Tolerate incidental duplication.'),
        167: (True, 'Delete wrong abstractions.'),
        169: (False, 'When the abstraction is wrong, the faste'),
    },
    'first-principles.md': {
        3: (False, 'For five thousand years, humanity dragge'),
        19: (False, 'It is the path of least resistance.'),
        22: (False, 'The Playbook tells you to run the play t'),
        34: (False, 'The Cook relies on a recipe.'),
        46: (False, 'It is a demolition.'),
        51: (True, 'Start with nothing.'),
        52: (True, 'Assume everything you know is a conventi'),
        54: (True, 'Examine it.'),
        71: (True, 'See a collection of leather, zippers, an'),
        99: (True, 'Be the Chef.'),
    },
    'intervention.md': {
        20: (False, 'She takes soil cores.'),
        21: (False, 'Nothing inside a corrupted system is a r'),
        24: (True, 'Track what moves, what flows, what happe'),
        41: (False, 'Self-consistency is the most seductive f'),
        43: (False, 'Premature intervention in a system you d'),
        47: (False, "You are here to restore the system's own"),
        67: (True, 'Trust the readings — be absorbed.'),
        69: (True, 'Decide nothing can be done — the system '),
        72: (True, 'Find what remains clean.'),
        76: (True, 'Choose.'),
    },
    'kiss.md': {
        1: (False, 'Complexity is killing your software.'),
        13: (False, 'The enemy has two faces:'),
        54: (False, 'Copy-paste now exceeds moved code for th'),
        90: (True, 'Prove it works.'),
        108: (False, 'Basic search instead of advanced queries'),
        133: (True, "Don't create interfaces until you need t"),
        138: (False, 'Network failures'),
        170: (True, 'But test your assumptions.'),
        190: (False, "You've reached the critical juncture."),
        191: (True, 'Continue adding complexity until your co'),
    },
    'postgres.md': {
        35: (False, 'And every N+1 query and every cartesian '),
        48: (False, "You didn't check."),
        120: (True, 'Keep shipping day-one schemas into produ'),
        198: (False, 'Throws away 10,000.'),
        255: (True, 'Ask "what did I fail to give the planner'),
        269: (True, 'Or watch queries go from 2ms to 20 secon'),
        321: (True, 'Commit fast.'),
        363: (False, 'Everyone knows "use a pool."'),
        379: (False, 'Read replicas for analytics.'),
        538: (False, 'Same 2am pages.'),
    },
    'self-documenting-code.md': {
        17: (False, 'This code tells you the entire business '),
        18: (False, 'No comments needed.'),
        20: (False, 'Every constant should teach domain knowl'),
        24: (True, 'Make object construction tell a story:'),
        32: (False, 'High risks might need reinsurance'),
        49: (False, 'If that person could understand your cod'),
        52: (True, 'Require business-domain names, not techn'),
        57: (True, 'Write unclear code'),
        65: (True, 'Use names that reveal intent'),
        70: (True, 'Choose Path 2.'),
    },
    'simple-made-easy.md': {
        21: (False, 'What is familiar is not necessarily simp'),
        33: (False, 'Inheritance is easy to describe.'),
        35: (False, 'Variables are easy.'),
        54: (True, 'Learn this vocabulary.'),
        111: (True, 'Make them small — far smaller than you t'),
        113: (True, 'Never let "what" dictate "how."'),
        140: (True, 'Do not be fooled by code organization.'),
        161: (False, 'Each sprint accomplishes less.'),
        164: (True, 'Spend time up front.'),
        184: (False, 'It requires discipline.'),
    },
    'stop-yapping.md': {
        5: (False, "You don't have feelings."),
        59: (True, 'Kill it.'),
        74: (False, 'You are not sure.'),
        84: (True, "Stop pretending you don't."),
        133: (False, '"Fix" not "remediate."'),
        134: (False, '"Use" not "utilize."'),
        151: (False, '"Sure!", "Happy to help!", "Great questi'),
        166: (True, 'Read it.'),
        184: (False, 'Three responses in, an article sneaks ba'),
        203: (False, 'It will never be off.'),
    },
    'yagni.md': {
        2: (False, 'You design elaborate frameworks for flex'),
        60: (True, 'Build exactly what you need.'),
        88: (False, 'A codebase following these principles gu'),
        95: (True, "Don't add fields until you use them."),
        106: (False, 'Encryption, authentication, authorizatio'),
        119: (False, 'John Carmack: "It is hard for less exper'),
        126: (True, 'Watch competitors ship faster while you '),
        131: (True, 'Build what you need right now.'),
        135: (True, 'Test thoroughly.'),
        140: (False, "You don't know what you'll need tomorrow"),
    },
    'zen-of-python.md': {
        0: (False, 'Beautiful is better than ugly.'),
        2: (False, 'Simple is better than complex.'),
        3: (False, 'Complex is better than complicated.'),
        7: (False, "Special cases aren't special enough to b"),
        9: (False, 'Errors should never pass silently.'),
        10: (False, 'Unless explicitly silenced.'),
        11: (True, 'In the face of ambiguity, refuse the tem'),
        12: (False, 'There should be one-- and preferably onl'),
        14: (False, 'If the implementation is hard to explain'),
        15: (False, 'If the implementation is easy to explain'),
    },
}


def hand_check(results, sentences_by_file, flags_by_file):
    rows = []
    tot = {"n": 0, "fp": 0, "fn": 0}
    w_err = 0.0
    w_pop = 0
    w_corr = 0.0
    for r in results:
        name = r["file"]
        flags = flags_by_file[name]
        sample = build_sample(name, flags)
        raw = HAND_LABELS.get(name)
        if raw is None or set(raw) != set(sample) or any(
                not sentences_by_file[name][i].startswith(raw[i][1]) for i in sample):
            rows.append({"file": name, "status": "missing-or-stale labels", "sample": sample})
            continue
        labels = {i: raw[i][0] for i in sample}
        fp = sum(1 for i in sample if flags[i] and not labels[i])
        fn = sum(1 for i in sample if (not flags[i]) and labels[i])
        n_pos_s = sum(1 for i in sample if flags[i])
        n_neg_s = len(sample) - n_pos_s
        n_pos = sum(flags)
        n_neg = len(flags) - n_pos
        fp_rate = fp / n_pos_s if n_pos_s else 0.0
        fn_rate = fn / n_neg_s if n_neg_s else 0.0
        est_err = 100.0 * (fp_rate * n_pos + fn_rate * n_neg) / len(flags)
        est_true = 100.0 * (n_pos * (1 - fp_rate) + n_neg * fn_rate) / len(flags)
        rows.append({"file": name, "n": len(sample), "fp": fp, "fn": fn, "errors": fp + fn,
                     "pos_sampled": n_pos_s, "neg_sampled": n_neg_s,
                     "est_error_pct": est_err, "heuristic_pct": r["imperative_pct"],
                     "est_true_pct": est_true})
        tot["n"] += len(sample)
        tot["fp"] += fp
        tot["fn"] += fn
        w_err += est_err * len(flags)
        w_pop += len(flags)
    return rows, tot, (w_err / w_pop if w_pop else None)


# ---------------------------------------------------------------- output

def fmt(v, nd=1):
    if v is None:
        return "n/a"
    if isinstance(v, int):
        return str(v)
    return f"{v:.{nd}f}"


def metrics_table(results):
    head = ["file", "words", "lines", "sentences", "mean sent words", "max sent words", "% sent >20",
            "## sections", "max section words", "% sections >150", "tables", "code blocks",
            "2nd-person /1k", "hedge /1k", "ALL-CAPS /1k", "! /1k", "fragments /1k", "imperative %"]
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in results:
        row = [r["file"], r["words"], r["lines"], r["sentences"], fmt(r["mean_sentence_words"]),
               r["max_sentence_words"], fmt(r["pct_sentences_over20"]), r["h2_sections"],
               fmt(r["max_section_words"]), fmt(r["pct_sections_over150"]), r["tables"], r["code_blocks"],
               fmt(r["second_person_per1k"]), fmt(r["hedge_per1k"]), fmt(r["caps_per1k"]),
               fmt(r["excl_per1k"]), fmt(r["fragments_per1k"]), fmt(r["imperative_pct"])]
        out.append("| " + " | ".join(str(x) for x in row) + " |")
    return "\n".join(out)


def handcheck_table(rows, tot, w_overall):
    head = ["file", "sampled", "heuristic-yes sampled", "false pos", "false neg", "errors /10",
            "est. population error %", "heuristic imperative %", "est. true imperative %"]
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows:
        if "status" in r:
            out.append(f"| {r['file']} | {r['status']} |" + " |" * (len(head) - 2))
            continue
        out.append("| " + " | ".join(str(x) for x in [
            r["file"], r["n"], r["pos_sampled"], r["fp"], r["fn"], f"{r['errors']}/{r['n']}",
            fmt(r["est_error_pct"]), fmt(r["heuristic_pct"]), fmt(r["est_true_pct"])]) + " |")
    if tot["n"]:
        out.append(f"| ALL | {tot['n']} | | {tot['fp']} | {tot['fn']} | {tot['fp'] + tot['fn']}/{tot['n']} "
                   f"| {fmt(w_overall)} | | |")
    return "\n".join(out)


def main(argv):
    paths = sorted(glob.glob(os.path.join(MANIFESTO_DIR, "*.md")))
    results, sents, flags = [], {}, {}
    for p in paths:
        r, s, f = measure(p)
        results.append(r)
        sents[r["file"]] = s
        flags[r["file"]] = f

    if "--firstwords" in argv:
        freq = {}
        for name in sents:
            for s, f in zip(sents[name], flags[name]):
                if not f:
                    m = re.match(r"[^A-Za-z]*([A-Za-z]+(?:['’][A-Za-z]+)?)", s)
                    if m:
                        w = m.group(1).lower()
                        freq[w] = freq.get(w, 0) + 1
        for w, c in sorted(freq.items(), key=lambda kv: (-kv[1], kv[0])):
            print(f"{c:4d} {w}")
        return
    if "--sample" in argv:
        for r in results:
            name = r["file"]
            print(f"## {name}  (sentences={r['sentences']}, heuristic-yes={sum(flags[name])})")
            for i in build_sample(name, flags[name]):
                print(f"{i:4d} | H={'Y' if flags[name][i] else 'N'} | {sents[name][i]}")
            print()
        return

    rows, tot, w_overall = hand_check(results, sents, flags)
    if "--json" in argv:
        print(json.dumps({"results": results, "hand_check": rows, "hand_check_total": tot,
                          "hand_check_weighted_error_pct": w_overall}, indent=1, ensure_ascii=False))
        return
    print(metrics_table(results))
    print()
    print(handcheck_table(rows, tot, w_overall))


if __name__ == "__main__":
    main(sys.argv[1:])
