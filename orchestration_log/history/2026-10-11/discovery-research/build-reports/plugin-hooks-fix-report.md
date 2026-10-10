Elements loaded (full read from source): First Principles (/home/user/LLM_MANIFESTOS/manifestos/first-principles.md, 5,061 bytes); Strunk SPR v3 (/home/user/LLM_MANIFESTOS/instructions/strunk_spr_v3_complete.xml, 123,636 bytes, 2,923 lines, read through the Read tool in one pass); Binding protocol (/home/user/claude-skills/manifesto/skills/manifesto-oath/SKILL.md, 7,290 bytes); TDD (/home/user/claude-skills/dev-discipline/skills/tdd/SKILL.md, 7,575 bytes); Ethos (/home/user/claude-skills/ETHOS.md, 4,064 bytes). Evidence read whole before work: resolutions/runtime-defects-verification.md (27,832 bytes) and deep-dives/runtime-audit.md (36,351 bytes). No element referenced a loadable file outside this list (Strunk's book citations excepted).
Interplay: First Principles and Strunk converge on function over form, stated concretely and briefly; TDD and Ethos converge on checkable boundaries (a failing test, a line ceiling, a character cap). Four tensions, each resolved by rule. (1) Ethos "inline all essential content" against the owner decision "hooks never inline the oath skill": the owner decision governs hooks; the five steps stay inline in at most 25 lines; the skill text loads by command, with a Read fallback path when the Skill tool is absent. (2) TDD "never write a comment" against comment-bearing shell scripts: new code carries no comment; comments that turned false were deleted; true comments stayed. (3) Ethos "policy without rationale" against the preamble's rationale sentences: new text carries none; untouched preamble sentences stay, listed under Open. (4) TDD "one test, then code" against the task's single test script: one script, written and run red before any code change.
Commitments: I must derive each fix from the verified defects (10,000-character cap, 22-variant schema, matcher source), and I will assert each through the test before and after the change; I must not inline skill text or leave a PostCompact path, and I will not; I must state facts in active, positive, concrete sentences, and I will cut every word that does not tell; I must keep scope to hooks, templates, SCHEMA.md, README, and plugin.json, and I will leave skills, the agent, CLAUDE.md, and ETHOS.md unedited.

# Plugin Hooks Fix

Branch `manifesto-binding-channel` (from `main`), HEAD `a0fe378`, pushed on the first attempt.

## Red — the failing test output before changes

Command: `TMPDIR=<scratchpad> bash manifesto/hooks/test_hooks.sh` against the unchanged scripts, with the live `.manifestos.yaml` copied into a temp project dir plus `manifesto_dir: /home/user/LLM_MANIFESTOS`, a stub `git` first on PATH (no pull, no clone), and stdin JSON per event. Exit 1; 43 of 76 checks passed, 33 failed. All 33 failures follow (PASS lines omitted):

```
FAIL  hooks.json: SessionStart matcher is startup|resume|compact
        matcher startup|resume, expected startup|resume|compact
FAIL  hooks.json: no PostCompact event
        hooks.json registers PostCompact
FAIL  post-compact.sh deleted
        present: /home/user/claude-skills/manifesto/hooks/post-compact.sh
FAIL  preamble-compact.txt deleted
        present: /home/user/claude-skills/manifesto/hooks/templates/parts/preamble-compact.txt
FAIL  SessionStart startup: stdout parses as JSON
        not JSON: Expecting value: line 1 column 1 (char 0)
FAIL  SessionStart startup: hookEventName is SessionStart and host-accepted
        no hookSpecificOutput.hookEventName
FAIL  SessionStart startup: stdout under 8000 characters
        10759 characters, limit 8000
FAIL  SessionStart startup: additionalContext under 8000 characters
        10759 characters, limit 8000
FAIL  SessionStart startup: carries the load command
        missing: Invoke the Skill tool with skill manifesto:manifesto-oath
FAIL  SessionStart startup: carries no oath skill body
        present: You are a knight receiving an oath
FAIL  SessionStart startup: says which source fired
        missing: Session source: startup.
FAIL  SessionStart resume: stdout parses as JSON
        not JSON: Expecting value: line 1 column 1 (char 0)
FAIL  SessionStart resume: hookEventName is SessionStart and host-accepted
        no hookSpecificOutput.hookEventName
FAIL  SessionStart resume: stdout under 8000 characters
        10759 characters, limit 8000
FAIL  SessionStart resume: additionalContext under 8000 characters
        10759 characters, limit 8000
FAIL  SessionStart resume: carries the load command
        missing: Invoke the Skill tool with skill manifesto:manifesto-oath
FAIL  SessionStart resume: carries no oath skill body
        present: You are a knight receiving an oath
FAIL  SessionStart resume: says which source fired
        missing: Session source: resume.
FAIL  SessionStart compact: stdout parses as JSON
        not JSON: Expecting value: line 1 column 1 (char 0)
FAIL  SessionStart compact: hookEventName is SessionStart and host-accepted
        no hookSpecificOutput.hookEventName
FAIL  SessionStart compact: stdout under 8000 characters
        10759 characters, limit 8000
FAIL  SessionStart compact: additionalContext under 8000 characters
        10759 characters, limit 8000
FAIL  SessionStart compact: carries the load command
        missing: Invoke the Skill tool with skill manifesto:manifesto-oath
FAIL  SessionStart compact: carries no oath skill body
        present: You are a knight receiving an oath
FAIL  SessionStart compact: says which source fired
        missing: Session source: compact.
FAIL  SubagentStart instruction-writer: stdout under 8000 characters
        9193 characters, limit 8000
FAIL  SubagentStart instruction-writer: additionalContext under 8000 characters
        8779 characters, limit 8000
FAIL  SubagentStart instruction-writer: carries the load command
        missing: Invoke the Skill tool with skill manifesto:manifesto-oath
FAIL  SubagentStart instruction-writer: carries no oath skill body
        present: You are a knight receiving an oath
FAIL  SubagentStart manifesto:maximalist-reviewer: stdout under 8000 characters
        8826 characters, limit 8000
FAIL  SubagentStart manifesto:maximalist-reviewer: additionalContext under 8000 characters
        8433 characters, limit 8000
FAIL  SubagentStart manifesto:maximalist-reviewer: carries the load command
        missing: Invoke the Skill tool with skill manifesto:manifesto-oath
FAIL  SubagentStart manifesto:maximalist-reviewer: carries no oath skill body
        present: You are a knight receiving an oath

43/76 checks passed
```

Length failures: SessionStart 10,759 characters (all three sources); SubagentStart 8,779 (matched) and 8,433 (fallback). Inline-text failures: the sentence `You are a knight receiving an oath` is present in all five binding outputs, and the load command is absent from all five. Structure failures: matcher `startup|resume`, PostCompact registered, `post-compact.sh` and `preamble-compact.txt` present, SessionStart plain text instead of JSON, no source line.

## Green — the passing output after, with character counts per hook

Exit 0; 76 of 76 checks passed, run again on the clean committed tree (HEAD `a0fe378`):

```
PASS  hooks.json: SessionStart matcher is startup|resume|compact
PASS  hooks.json: no PostCompact event
PASS  hooks.json: every command script exists
PASS  post-compact.sh deleted
PASS  preamble-compact.txt deleted
PASS  SessionStart startup: exit status 0
PASS  SessionStart startup: stderr empty
PASS  SessionStart startup: stdout parses as JSON
PASS  SessionStart startup: hookEventName is SessionStart and host-accepted
PASS  SessionStart startup: stdout under 8000 characters
PASS  SessionStart startup: additionalContext under 8000 characters
PASS  SessionStart startup: carries the load command
PASS  SessionStart startup: carries no oath skill body
PASS  SessionStart startup: names the manifesto dir
PASS  SessionStart startup: names the plugin cache path
PASS  SessionStart startup: binding section within 25 lines
PASS  SessionStart startup: names every you: element and purpose
PASS  SessionStart startup: says which source fired
PASS  SessionStart startup: keeps the subagent reinforcement footer
PASS  SessionStart resume: exit status 0
PASS  SessionStart resume: stderr empty
PASS  SessionStart resume: stdout parses as JSON
PASS  SessionStart resume: hookEventName is SessionStart and host-accepted
PASS  SessionStart resume: stdout under 8000 characters
PASS  SessionStart resume: additionalContext under 8000 characters
PASS  SessionStart resume: carries the load command
PASS  SessionStart resume: carries no oath skill body
PASS  SessionStart resume: names the manifesto dir
PASS  SessionStart resume: names the plugin cache path
PASS  SessionStart resume: binding section within 25 lines
PASS  SessionStart resume: names every you: element and purpose
PASS  SessionStart resume: says which source fired
PASS  SessionStart resume: keeps the subagent reinforcement footer
PASS  SessionStart compact: exit status 0
PASS  SessionStart compact: stderr empty
PASS  SessionStart compact: stdout parses as JSON
PASS  SessionStart compact: hookEventName is SessionStart and host-accepted
PASS  SessionStart compact: stdout under 8000 characters
PASS  SessionStart compact: additionalContext under 8000 characters
PASS  SessionStart compact: carries the load command
PASS  SessionStart compact: carries no oath skill body
PASS  SessionStart compact: names the manifesto dir
PASS  SessionStart compact: names the plugin cache path
PASS  SessionStart compact: binding section within 25 lines
PASS  SessionStart compact: names every you: element and purpose
PASS  SessionStart compact: says which source fired
PASS  SessionStart compact: keeps the subagent reinforcement footer
PASS  SubagentStart instruction-writer: exit status 0
PASS  SubagentStart instruction-writer: stderr empty
PASS  SubagentStart instruction-writer: stdout parses as JSON
PASS  SubagentStart instruction-writer: hookEventName is SubagentStart and host-accepted
PASS  SubagentStart instruction-writer: stdout under 8000 characters
PASS  SubagentStart instruction-writer: additionalContext under 8000 characters
PASS  SubagentStart instruction-writer: carries the load command
PASS  SubagentStart instruction-writer: carries no oath skill body
PASS  SubagentStart instruction-writer: names the manifesto dir
PASS  SubagentStart instruction-writer: names the plugin cache path
PASS  SubagentStart instruction-writer: binding section within 25 lines
PASS  SubagentStart instruction-writer: names every element and purpose
PASS  SubagentStart manifesto:maximalist-reviewer: exit status 0
PASS  SubagentStart manifesto:maximalist-reviewer: stderr empty
PASS  SubagentStart manifesto:maximalist-reviewer: stdout parses as JSON
PASS  SubagentStart manifesto:maximalist-reviewer: hookEventName is SubagentStart and host-accepted
PASS  SubagentStart manifesto:maximalist-reviewer: stdout under 8000 characters
PASS  SubagentStart manifesto:maximalist-reviewer: additionalContext under 8000 characters
PASS  SubagentStart manifesto:maximalist-reviewer: carries the load command
PASS  SubagentStart manifesto:maximalist-reviewer: carries no oath skill body
PASS  SubagentStart manifesto:maximalist-reviewer: names the manifesto dir
PASS  SubagentStart manifesto:maximalist-reviewer: names the plugin cache path
PASS  SubagentStart manifesto:maximalist-reviewer: binding section within 25 lines
PASS  SubagentStart manifesto:maximalist-reviewer: states no element matched
PASS  UserPromptSubmit: exit status 0
PASS  UserPromptSubmit: stderr empty
PASS  UserPromptSubmit: stdout under 8000 characters
PASS  UserPromptSubmit: names every you: element
PASS  UserPromptSubmit: carries no oath skill body

76/76 checks passed
```

Character counts, measured on the same config and environment as the test (stdout = bytes the host receives; context = `additionalContext`):

| Hook | Before: stdout / context | After: stdout / context | Binding section |
|---|---|---|---|
| SessionStart `startup` | 10,759 plain text / 10,759 | 4,440 JSON / 4,232 | 12 lines |
| SessionStart `resume` | 10,759 / 10,759 | 4,439 / 4,231 | 12 lines |
| SessionStart `compact` | none (matcher omitted `compact`) | 4,440 / 4,232 | 12 lines |
| SubagentStart `instruction-writer` (matched, 3 elements) | 9,193 / 8,779 | 2,416 / 2,265 | 12 lines |
| SubagentStart `manifesto:maximalist-reviewer` (fallback) | 8,826 / 8,433 | 2,049 / 1,919 | 12 lines |
| UserPromptSubmit `drift-reminder.sh` (unchanged) | 114 plain text | 114 plain text | n/a |
| PostCompact `post-compact.sh` | 9,995 / 9,567, rejected by the host schema | deleted | n/a |

Ceiling: 8,000 characters for stdout and for context; the largest output is 4,440. The load command reads `Invoke the Skill tool with skill manifesto:manifesto-oath before any other work.` and the Binding Required section runs 12 lines against a 25-line ceiling. The SUBAGENT BINDING REINFORCEMENT footer stays in all three SessionStart outputs. Added tests beyond the task list: exit status 0 and empty stderr per hook; the manifesto dir line; the plugin cache line; `Session source: <source>.` per source; matcher equals `startup|resume|compact`; hooks.json holds no PostCompact event; every hooks.json command script exists; `post-compact.sh` and `preamble-compact.txt` are absent.

## Harness run — command, result, whether the text arrived whole

Command (wrapper script in the scratchpad; cwd a scratch project holding the live config copy plus `manifesto_dir: /home/user/LLM_MANIFESTOS`; stub `git` first on PATH; stdin `/dev/null`; permission mode default, no bypassPermissions):

```
claude -p --plugin-dir /home/user/claude-skills/manifesto --output-format json --debug-file <scratchpad>/hf-out/debug.log 'reply with the single word ok'
```

Result: exit 0; `subtype` `success`, `is_error` false, `result` `"ok"`, `num_turns` 1, `permission_denials` `[]`; 5 s wall time; stderr empty.

Whether the text arrived whole: yes.
- Debug log: `Hook SessionStart (Binding constitution...) provided additionalContext (4232 chars)`. The words `persisted-output` and `Persisted tool result` occur 0 times in the log.
- Transcript (`/root/.claude/projects/-tmp-claude-0--home-user-ce8858a2-4629-5988-bee7-daa6cda6115e-scratchpad-hf-proj/ce8858a2-4629-5988-bee7-daa6cda6115e.jsonl`, line 4): attachment `hook_additional_context`, content 4,232 characters. The model-facing `rendered` block is a 4,307-character `<system-reminder>` beginning `SessionStart hook additional context: MANDATORY CONSTITUTION INITIALIZATION` and ending `You provide the authority.`. It contains `Session source: startup.`, the load command, `Silent binding is worthless`, and the Subagent Binding Reinforcement section; it contains no `<persisted-output>` wrapper and no oath body.
- The UserPromptSubmit hook arrived as `UserPromptSubmit hook success: Active bindings: ...` (transcript line 12), unchanged.
- Before the fix (verification file): the model received a 1,944-character persisted-output wrapper with a 2KB preview cut at the heading `# Manifesto Oath Protocol`.

Observation, not a defect claim: the model answered `ok` in one turn and did not invoke the skill for this prompt. The run shows delivery, not obedience.

## Commits

| Hash | Message | Files |
|---|---|---|
| a390757 | fix(manifesto): bind via skill load command, emit SessionStart JSON, drop PostCompact | manifesto/hooks/hooks.json; session-start.sh; subagent-start.sh; post-compact.sh (deleted) |
| 1065099 | fix(manifesto): replace inlined oath with load command in binding templates | manifesto/hooks/templates/parts/binding-core.txt; preamble-session.txt; preamble-compact.txt (deleted) |
| 0432260 | test(manifesto): hook output contract | manifesto/hooks/test_hooks.sh |
| 43ffb02 | doc(manifesto): SessionStart sources, no PostCompact, skill load command | manifesto/SCHEMA.md |
| de30f04 | chore(manifesto): bump to 3.3.0 | manifesto/.claude-plugin/plugin.json |
| a0fe378 | doc(readme): regenerate for manifesto 3.3.0 | README.md; .claude-plugin/marketplace.json |

Push: `git push -u origin manifesto-binding-channel` succeeded on attempt 1 of 5 (no retry needed). No attribution lines in any commit message.

Code changes in brief: `session-start.sh` reads `source` from stdin, emits `hookSpecificOutput` JSON with `hookEventName` `SessionStart`, drops the inlined skill, and sets `SKILL_PATH`; `subagent-start.sh` drops the inlined skill and `REBIND_NOTE`; `binding-core.txt` carries the load command, a Read fallback by absolute path, the five steps, the element sentences, the manifesto dir, and the plugin cache path; `preamble-session.txt` swaps "This hook fires once at session start." for `Session source: ${SOURCE}.`; `hooks.json` matcher is `startup|resume|compact` and holds no PostCompact entry; the `SOURCE` value is accepted only when it matches `[a-z]+`, else `unknown`.

## Open

- Commit split: the owner order gave four commits; the repo's artifact classes add two. `test_hooks.sh` is its own commit (tests are a separate class) and lands third, where the suite first passes. The regenerated root `README.md` and `.claude-plugin/marketplace.json` (version fields derived from `plugin.json`) form a sixth commit, matching the repo's earlier `doc(readme): regenerate` and `chore(manifesto): bump to` commits. Commits 1 and 2 are individually inconsistent (scripts without templates, then templates without tests); the tree is green from commit 2 and tested from commit 3.
- README: `manifesto/README.md` carries no hook text, and `generate.py` scans only `hooks/*.md`, so the generator produced no change to it. SCHEMA.md holds the only hook-behavior text change.
- `drift-reminder.sh` stays unchanged and emits plain text, so the task's JSON assertion cannot apply to it; the test asserts exit 0, empty stderr, under 8,000 characters, every `you:` element name, and no oath body.
- Not exercised under the real host: the `resume` and `compact` sources, and a real `/compact`. The test covers both at script level; the matcher change rests on hooks.json plus the verification file's finding that the host runs SessionStart with source `compact` after compaction.
- The maximalist-reviewer agent lacks the Skill tool in its frontmatter; the hook text carries `Read <absolute SKILL.md path>` as the fallback. The agent stays untouched per scope.
- Defects from the audit left in place as outside the request: the hook text caps read depth at three while the skill body reads until no reference remains; the skill names `.claude/manifesto-repo/LLM_MANIFESTOS/manifestos/` while the hook line names `manifesto_dir`; SCHEMA.md omits the suffix step of the SubagentStart match cascade; the live config has no `subagents.other` key; the preamble sentences "Shortcuts here propagate as binding gaps throughout the session." and "Each skipped step produces a gap that cannot be recovered without re-binding." remain; the SubagentStart comment "Plain text stdout is silently discarded" is unverified; ETHOS.md line 37 still lists PostCompact.
- Scratchpad: the shared scratchpad held `proj` and `stubbin` directories from an earlier verification run; this run deleted and recreated them (for `count-hooks.sh`) before switching to `hf-proj` and `hf-stubbin`. After the harness run, `find -newer` listed only `.git` under /home/user/claude-skills; under /home/user/LLM_MANIFESTOS it listed `.git` (index refresh from my `git status`) and two reports that other sessions wrote. The repository tree is clean at HEAD.

Summary: The tests failed 33 of 76 checks on the old code and pass 76 of 76 now. SessionStart now emits 4,232 characters of additionalContext (4,440 characters of stdout), down from 10,759, and the real host delivered it whole with no persisted-output wrapper. The branch manifesto-binding-channel pushed to origin on the first attempt with six commits and plugin.json at 3.3.0.

## Follow-up

Same branch, pushed on attempt 1 of 5 (`a0fe378..b4e4bde`). The three commits below supersede the Open bullets on the depth conflict, the SCHEMA suffix omission, and the preamble rationale sentences.

| Hash | Message | Files |
|---|---|---|
| 59ed694 | refactor(manifesto): templates state commands only | manifesto/hooks/templates/parts/binding-core.txt; preamble-session.txt; preamble-subagent.txt |
| 02d8b8b | test(manifesto): hooks omit rationale and depth cap | manifesto/hooks/test_hooks.sh |
| b4e4bde | doc(manifesto): schema names suffix match and depth | manifesto/SCHEMA.md |

The test commit is a third commit beyond the two the coordinator named; tests are their own artifact class.

Red (new assertions against the unchanged templates): 76 of 91 checks passed, 15 failed: per binding output, `states the oath skill's closure rule` (missing `until no unresolved references remain`), `sets no depth cap` (present `maximum depth of three levels`), and, for the three SessionStart and the two SubagentStart outputs, `omits rationale sentences` (present: "Shortcuts here propagate as binding gaps", "Each skipped step produces a gap", "Silent binding is worthless", plus "Shallow reading produces incomplete binding" and "The binding determines whether your work survives review" in SubagentStart). Green: 91 of 91.

Removed from templates: "Shortcuts here propagate as binding gaps throughout the session."; "Each skipped step produces a gap that cannot be recovered without re-binding."; "Shallow reading produces incomplete binding and the orchestrator will reject your output."; "The binding determines whether your work survives review."; "Silent binding is worthless." Kept: every command, the `This is not optional.` marker, the source line, and the element, repo, and cache facts.

Depth: the oath skill states no number; it says to repeat "until no unresolved references remain". The template had capped depth at three levels. Step two of `binding-core.txt` now reads "Follow every referenced file, skill, URL, or document until no unresolved references remain." SCHEMA.md states: transitive depth unbounded, the hooks set no depth cap.

SCHEMA.md: the SubagentStart cascade now lists five steps (exact, prefix-strip, suffix, `other:`, static fallback) and notes that an absent `agent_type` skips to `other:`. Checked by running the hook: `my-instruction-writer` and `some-plugin:instruction-writer` match `instruction-writer`; `{}` takes the fallback.

Character counts after the follow-up (same config and environment as the Green table; stdout / context):

| Hook | Before follow-up | After follow-up |
|---|---|---|
| SessionStart `startup` | 4,440 / 4,232 | 4,272 / 4,066 |
| SessionStart `resume` | 4,439 / 4,231 | 4,271 / 4,065 |
| SessionStart `compact` | 4,440 / 4,232 | 4,272 / 4,066 |
| SubagentStart `instruction-writer` | 2,416 / 2,265 | 2,243 / 2,094 |
| SubagentStart `manifesto:maximalist-reviewer` | 2,049 / 1,919 | 1,876 / 1,748 |
| UserPromptSubmit `drift-reminder.sh` | 114 | 114 |

### Open (follow-up)

- Two manifesto-dir paths remain, untouched by order: the oath skill names `.claude/manifesto-repo/LLM_MANIFESTOS/manifestos/` (project-relative) while the hook text names `manifesto_dir` on its `Manifesto repo:` line.
- ETHOS.md line 37 still lists PostCompact, untouched by order.
- The inline footers in `session-start.sh` and `subagent-start.sh` are not templates and keep their rationale sentences (for example "System context has lower compliance authority than user messages." and "This dual injection ... is the binding's enforcement mechanism."); the order covered templates only.
- Still not run under the real host: the `resume` and `compact` sources and a real `/compact`; the harness run predates the follow-up, and the follow-up changes were tested at script level only.

Summary: test_hooks.sh now passes 91 of 91 checks (15 of the new assertions failed first). SessionStart now emits 4,066 characters of additionalContext (4,272 of stdout), down from 4,232 after the first fix. The follow-up pushed to origin on the first attempt as 59ed694, 02d8b8b, and b4e4bde.

## Follow-up 2

Same branch, pushed on attempt 1 of 5 (`c84a59b..9ff0b6a`). Closes OQ-004 and OQ-005.

| Hash | Message | Files |
|---|---|---|
| abd7459 | doc(ethos): one-time hooks list without PostCompact | ETHOS.md (line 37 only: `(SessionStart, SubagentStart)`) |
| 9d4ef86 | fix(manifesto-oath): manifesto dir comes from the hook injection | manifesto/skills/manifesto-oath/SKILL.md (Tier 1 line only) |
| 9ff0b6a | test(manifesto): oath skill Tier 1 defers to the hook injection | manifesto/hooks/test_hooks.sh |

The test commit is a third commit beyond the two the coordinator named; tests are their own artifact class.

Tier 1 line now reads: "**Tier 1: Manifesto repo (PRIMARY).** The manifesto repo is the directory the hook injection names on its `Manifesto repo:` line; the default is `.claude/manifesto-repo/LLM_MANIFESTOS` under the project. Search its `manifestos/` folder — file names, headings, content. Purpose-built manifesto documents live here." The skill holds no absolute path; every other line of the skill is byte-identical (the diff is one line). The skill's Example block still shows the relative default path, untouched by order.

Red: the new assertion `oath skill Tier 1 takes the manifesto dir from the hook injection` failed against the old line (`Tier 1 does not name the Manifesto repo: line`); 91 of 92 passed. Green: 92 of 92, re-run on the committed tree.

README: the generator reads skill frontmatter only, the skill description is unchanged, and `generate.py` produced no diff.

Branch note: another session merged the manifesto-writing standard into the branch (`c84a59b`, with commits e7ace90, 879bc24, 1f314d1) between the previous push and this work. This follow-up sits on top of it; the suite passes on the merged tree and the generator produced no diff.

Open: none from the coordinator's list remain. Still not run under the real host: the `resume` and `compact` sources and a real `/compact`. The rationale sentences in the script-inlined footers remain (not templates; not covered by an order).

Summary: ETHOS.md line 37 now lists only SessionStart and SubagentStart, and the oath skill's Tier 1 line takes the manifesto dir from the hook injection's `Manifesto repo:` line with no absolute path. test_hooks.sh passes 92 of 92 checks (one new assertion failed first), and the generator produced no README change. The three commits abd7459, 9d4ef86, and 9ff0b6a pushed to origin on the first attempt.
