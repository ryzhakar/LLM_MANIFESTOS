# .manifestos.yaml Schema Reference

## Format variants

### Flat list (backwards compatible, orchestrator-only)

Root is a YAML list. All elements bind to the orchestrator. No subagent bindings.

```yaml
- only-fluff-die
- first-principles
- agentic-delegation
```

### Grouped mapping (full form)

Root is a YAML mapping with `you:` and/or `subagents:` keys. Supports optional top-level fields.

```yaml
manifesto_dir: /path/to/a/folder/with/a/manifestos/subfolder
you:
  - only-fluff-die
  - name: first-principles
    purpose: reasoning methodology
  - name: agentic-delegation
    purpose: orchestration operating model
    source: skill orchestration:agentic-delegation

subagents:
  instruction-writer:
    - name: first-principles
    - name: strunk-spr-v3
      purpose: writing compression standard
      source: file standards/strunk_spr_v3_complete.xml
  other:
    - first-principles
```

---

## Where the config lives

1. `<project>/.manifestos.yaml`, where `<project>` is `$CLAUDE_PROJECT_DIR`, else the current folder.
2. Only when that file is absent: the `## Active Manifestos` section of `<project>/CLAUDE.md`, up to the next `## ` heading, read as the same YAML.
3. Neither: the hooks stay silent; `unharness` stops with `no config: tried <path> and the Active Manifestos section of <CLAUDE.md path>`.

One module reads it: `unharness/src/unharness/config.py`. The hooks run it with `python3 <config> --json`; `unharness` imports it. It needs only the standard library and runs on Python 3.9 or later when run as a script.

---

## Element forms

Each element in any list is one of:

**String** — a registry manifesto by name.

```yaml
- only-fluff-die
```

A colon not followed by a space belongs to the name: `- agent-conduct:write-well` is the name `agent-conduct:write-well`.

**Mapping** — `name`, and optionally `purpose` and `source`. Other keys are dropped.

```yaml
- name: first-principles
  purpose: reasoning methodology
  source: manifesto first-principles
```

**Null** (`~`, `null`, or an empty item) — dropped. An empty or absent list is an empty stack.

---

## Fields

### Top-level mapping fields

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| `you` | list of elements | no | empty | The orchestrator's constitution. |
| `subagents` | mapping of role to list of elements | no | empty | Constitutions by agent type. A role with no value is an empty list. |
| `manifesto_dir` | string (path) | no | hooks: `${CLAUDE_PLUGIN_ROOT}`; `unharness`: the manifesto plugin at its highest version in the plugin cache | The folder whose `manifestos/` subfolder is the registry. Ignored in the flat list form. A relative path resolves against the config's folder, in the hooks and in `unharness` alike. |

Any other top-level key is ignored.

### Element fields

| Field | Required | Description |
|-------|----------|-------------|
| `name` | yes, except for a `file` source | The label and tag. For a `file` source it defaults to the file's stem. |
| `purpose` | no | Freeform text. Hooks inject it as natural language; `unharness` puts it in `governs`. |
| `source` | no | A source type and its reference, below. Absent means a registry manifesto named `name`. |

### Source types

| Source | Resolves to |
|--------|-------------|
| none, or `manifesto <name>` | `<registry>/manifestos/<name>.md` (the reference is `name` when no source is given) |
| `skill <plugin>:<skill>` | `skills/<skill>/SKILL.md` of the plugin at its highest version under `<login>/plugins/cache/<marketplace>/<plugin>/<version>/` |
| `skill <skill>` | `<login>/skills/<skill>/SKILL.md` |
| `file <path>` | the file, relative to the folder holding the config |
| anything else (a path, a URL, a hint) | kept as written; the hooks print it, `unharness` refuses it |

The login folder is `$CLAUDE_CONFIG_DIR`, else `~/.claude`. Versions compare by number, so `1.10.0` is above `1.9.0`. `unharness` strips a text file's frontmatter and replaces `${CLAUDE_PLUGIN_ROOT}` with the registry's plugin folder or the skill's version folder; a user skill and a file keep the placeholder as written.

---

## Errors

Every error is one line. `unharness` prints `unharness: <line>` on stderr and exits 1. A hook prints the same line on stderr, prints nothing on stdout, and exits 0. A missing config is the exception: the hooks stay silent, and `config.py` exits 2 instead of 1 so they can tell it apart.

| Line | Cause |
|------|-------|
| `no config: tried ...` | no config file and no CLAUDE.md section |
| `<list> must be a list of elements` | `you` or a role holds a scalar or a flow list such as `[a, b]` |
| `subagents must be a mapping of role to list of elements` | `subagents` holds a scalar or a list |
| `element N of <list> has no name; add name: or a file source` | a mapping without `name` and without a `file` source; `<list>` is `you` or `subagents.<role>` |
| `element X did not resolve; tried <path>` | the one path the source names does not exist; with no cached plugin the path shows the pattern `plugins/cache/*/<plugin>/*/...` |
| `element X has source type 'T' that is none of manifesto, skill, or file` | a legacy source form |
| `the stack is empty` | `unharness prompt` or `stack` with no element in `you` |
| `<file> is missing`, `<file> is stale (...)`, `<file> has no <stack> block` | a session file of `unharness prompt`; each names `/compile-commitments` |

---

## YAML subset

Block mappings and lists of string scalars, indented with spaces. A list must be indented deeper than its key. Whole-line and trailing `#` comments are dropped. A quoted scalar loses one pair of quotes. `~`, `null`, and an empty value are null. Flow collections, anchors, and multiline scalars are not supported. Manifesto frontmatter is read by the same reader.

---

## Scope keys

| Key | Meaning |
|-----|---------|
| `you:` | Orchestrator constitution. Injected by SessionStart and PostCompact hooks as natural language prose. |
| `subagents:` | Mapping of agent-type keys. Each key names a list of elements for that agent type. |
| `other:` (under `subagents:`) | Catch-all for agents not matching any specific key. |

---

## Hook behavior

### SessionStart / PostCompact

Read the config through `config.py --json`, render `you:` elements as natural language prose, one sentence per element: `"<name>" governs your <purpose>` or `"<name>" is part of your constitution`, then `— <where>`. The where is `read it from <absolute path>` for a `file` source, `read it from <manifesto_dir>/manifestos/<name>.md` for a `manifesto` source, `fetch it from <source>` for a source starting with `http`, `read it from <source>` for any other source, and `resolve its location via the tiered protocol before binding` for none. Compose output from three parts: hook-specific preamble + shared binding core + inline footer. NEVER inject raw YAML.

The footer includes a SUBAGENT BINDING REINFORCEMENT block instructing the orchestrator to use first-person user voice in dispatch prompts, so subagents receive binding directives as owner instructions rather than forwarded AI text.

The orchestrator is NOT responsible for supplying base subagent bindings — SubagentStart handles that automatically. The orchestrator MAY augment subagent bindings via dispatch prompts.

### SubagentStart

Reads `agent_type` from stdin JSON. Matches against `subagents:` keys in `.manifestos.yaml` using this resolution order:

1. Exact key match
2. Prefix-strip match (the part after the last `:`)
3. Suffix match (a key that ends `agent_type`)
4. `other:` catch-all
5. Static fallback (no config)

Injects the FULL binding ceremony — same resolution protocol, transitive reading, interplay analysis, and manifesto-oath mandate as the orchestrator hooks. This is a real binding injection, not a reminder.

The ceremony carries element names, purposes, and configured sources — never element content. Subagents read or fetch each element themselves; dispatch prompts carry sources for elements the config omits.

Tier 2 resolution injects the plugin cache path so subagents can resolve skills from the installed plugin location without knowing the absolute path at authoring time.

### UserPromptSubmit

Fires on every user message. Matches each `you:` name against the slug and title of the files in `<manifesto_dir>/manifestos/` and extracts their frontmatter taglines; a name with no match prints bare. Injects the taglines as a brief drift-prevention reminder into the hook output.

Output accumulates in conversation history (platform behavior) — this is intentional. Each injection reinforces the active constitution without re-running the full binding ceremony.

### Standing down under unharness

When `UNHARNESS` is set and not `0`, SessionStart and PostCompact print nothing and exit 0, because the compiled system prompt already carries the binding. UserPromptSubmit and SubagentStart run as usual.

### Template architecture

Composable parts live in `hooks/templates/parts/`:

| File | Used by |
|------|---------|
| `preamble-session.txt` | SessionStart |
| `preamble-compact.txt` | PostCompact |
| `preamble-subagent.txt` | SubagentStart |
| `binding-core.txt` | All three hooks (shared) |

Footers are inlined in the shell scripts, not extracted to files. The element sentences come from `hooks/describe_elements.py`, which all three binding hooks call.

---

## Bundled manifestos

The plugin carries `manifestos/` and `digests/` in its own folder. Every hook reads `${CLAUDE_PLUGIN_ROOT}/manifestos` (or the `manifesto_dir` override) directly; no hook clones, pulls, or touches the network.

---

## Parsing rules

1. Root is a list → treat as `you:` section; no subagent bindings.
2. Root is a mapping → read `you:`, `subagents:`, and `manifesto_dir:`.
3. String node in any list → `{name: <string>}`.
4. Mapping node → `{name:, purpose:, source:}`; a file source supplies the name when `name` is absent.
5. Null node → dropped.
