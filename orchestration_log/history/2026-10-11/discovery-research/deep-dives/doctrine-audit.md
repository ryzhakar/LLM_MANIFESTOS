Loaded in full from source: First Principles (manifestos/first-principles.md v1.0.1), Strunk SPR v3 (instructions/strunk_spr_v3_complete.xml, 2923 lines), Binding protocol (manifesto-oath SKILL.md).
Interplay: all three converge on concrete, positive, located statements and demand a visible binding; First Principles says discard the playbook while the task says extract it, so rules enter as data without ranking, and clarity outranks economy where Strunk's rules conflict.
I must reduce each rule to a quote of at most 25 words with file:line, and I will verify every quote and location by script; I must not judge a conflict or recommend, and I will not.

# Doctrine Audit — rules stated by both projects

Quotes strip markdown emphasis and backticks. Project A = LLM_MANIFESTOS. Project B = claude-skills. Git rows cite the commit hash. Angle-bracket placeholders in quotes are literal. Ellipsis-free: every quote is a contiguous substring of one source line.

## Rules

| ID | rule (quote) | file:line | project | class | status |
|---|---|---|---|---|---|
| D-001 | Manifestos are behavioral constitutions—timeless principles that define how systems should operate. | MAINTAINERS_GUIDE.md:9 | A | boundary | doctrine |
| D-002 | Philosophical frameworks distilled into actionable principles | MAINTAINERS_GUIDE.md:11 | A | form | doctrine |
| D-003 | Boundary conditions for acceptable behavior | MAINTAINERS_GUIDE.md:12 | A | boundary | doctrine |
| D-004 | Artifacts that preserve hard-won insights | MAINTAINERS_GUIDE.md:13 | A | evidence | doctrine |
| D-005 | Standards against which decisions are measured | MAINTAINERS_GUIDE.md:14 | A | boundary | doctrine |
| D-006 | Implementation guides (those belong in docs/) | MAINTAINERS_GUIDE.md:17 | A | boundary | doctrine |
| D-007 | Technical specifications (those belong in requirements/) | MAINTAINERS_GUIDE.md:18 | A | boundary | doctrine |
| D-008 | Temporary notes (those belong in scratch/) | MAINTAINERS_GUIDE.md:19 | A | boundary | doctrine |
| D-009 | Living documents that change frequently | MAINTAINERS_GUIDE.md:20 | A | boundary | doctrine |
| D-010 | Manifestos are precious artifacts, not documentation. | MAINTAINERS_GUIDE.md:3 | A | boundary | doctrine |
| D-011 | As a maintainer, you are a curator-archivist, not an editor-writer. | MAINTAINERS_GUIDE.md:24 | A | process | doctrine |
| D-012 | Evaluate what deserves manifesto status (high bar for entry) | MAINTAINERS_GUIDE.md:26 | A | entry | doctrine |
| D-013 | Preserve provenance through metadata (frontmatter as artifact record) | MAINTAINERS_GUIDE.md:27 | A | metadata | doctrine |
| D-014 | Organize for discovery (themes, descriptions, navigation) | MAINTAINERS_GUIDE.md:28 | A | metadata | doctrine |
| D-015 | Protect integrity through validation (schema as quality gate) | MAINTAINERS_GUIDE.md:29 | A | entry | doctrine |
| D-016 | Adding a manifesto is a significant event. Manifestos are rare and precious. | MAINTAINERS_GUIDE.md:31 | A | entry | doctrine |
| D-017 | Frontmatter is the source of truth for metadata. The README is always generated, never manually edited. | MAINTAINERS_GUIDE.md:49 | A | metadata | doctrine |
| D-018 | Pydantic schema catches malformed metadata before it corrupts the collection | MAINTAINERS_GUIDE.md:59 | A | entry | doctrine |
| D-019 | Invalid manifestos cannot enter the collection | MAINTAINERS_GUIDE.md:61 | A | entry | doctrine |
| D-020 | Each manifesto has exactly one theme (forces clarity) | MAINTAINERS_GUIDE.md:70 | A | metadata | doctrine |
| D-021 | Themes are editorial groupings, not rigid taxonomy | MAINTAINERS_GUIDE.md:69 | A | metadata | doctrine |
| D-022 | Theme metadata lives in themes.yaml (separate concern) | MAINTAINERS_GUIDE.md:71 | A | metadata | doctrine |
| D-023 | Decide when to version vs. when to edit | MAINTAINERS_GUIDE.md:82 | A | process | doctrine |
| D-024 | Is this principle timeless or temporary? | MAINTAINERS_GUIDE.md:85 | A | entry | doctrine |
| D-025 | Does it define behavior or describe implementation? | MAINTAINERS_GUIDE.md:86 | A | entry | doctrine |
| D-026 | Is it actionable or merely aspirational? | MAINTAINERS_GUIDE.md:87 | A | entry | doctrine |
| D-027 | Will this still matter in 5 years? | MAINTAINERS_GUIDE.md:88 | A | entry | doctrine |
| D-028 | Write clear, compelling descriptions (one sentence that conveys essence) | MAINTAINERS_GUIDE.md:93 | A | metadata | doctrine |
| D-029 | Ensure taglines capture the manifesto's core insight | MAINTAINERS_GUIDE.md:95 | A | metadata | doctrine |
| D-030 | Description answers: "Why should I read this?" | MAINTAINERS_GUIDE.md:98 | A | metadata | doctrine |
| D-031 | Tagline is memorable and distinctive | MAINTAINERS_GUIDE.md:100 | A | metadata | doctrine |
| D-032 | Run just readme before committing (validation gate) | MAINTAINERS_GUIDE.md:105 | A | process | doctrine |
| D-033 | Fix schema violations immediately (no invalid manifestos) | MAINTAINERS_GUIDE.md:106 | A | entry | doctrine |
| D-034 | Address theme discrepancies (themes.yaml should match usage) | MAINTAINERS_GUIDE.md:107 | A | metadata | doctrine |
| D-035 | manifestos/Manifesto, <principle> - \"<tagline>\".md | MAINTAINERS_GUIDE.md:126 | A | metadata | doctrine |
| D-036 | version: "1.0.0" | MAINTAINERS_GUIDE.md:134 | A | metadata | doctrine |
| D-037 | Write the manifesto content (the actual principle, evidence, practice) | MAINTAINERS_GUIDE.md:140 | A | form | doctrine |
| D-038 | Edit themes.yaml first | MAINTAINERS_GUIDE.md:144 | A | metadata | doctrine |
| D-039 | git commit -m "feat: add <principle> manifesto" | MAINTAINERS_GUIDE.md:162 | A | process | doctrine |
| D-040 | Forgetting version field (schema violation) | MAINTAINERS_GUIDE.md:166 | A | metadata | doctrine |
| D-041 | Fixing typos, improving clarity, adding examples—changes that don't alter core thesis. | MAINTAINERS_GUIDE.md:174 | A | process | doctrine |
| D-042 | Version stays the same (minor edits don't version) | MAINTAINERS_GUIDE.md:182 | A | process | doctrine |
| D-043 | git commit -m "docs: improve clarity in <manifesto>" | MAINTAINERS_GUIDE.md:192 | A | process | doctrine |
| D-044 | Typo fixes | MAINTAINERS_GUIDE.md:196 | A | process | doctrine |
| D-045 | Wording improvements | MAINTAINERS_GUIDE.md:197 | A | process | doctrine |
| D-046 | Formatting changes | MAINTAINERS_GUIDE.md:198 | A | process | doctrine |
| D-047 | Example additions that don't change thesis | MAINTAINERS_GUIDE.md:199 | A | process | doctrine |
| D-048 | git add manifestos/ README.md | MAINTAINERS_GUIDE.md:191 | A | process | doctrine |
| D-049 | The manifesto's core thesis has fundamentally changed. This is rare. | MAINTAINERS_GUIDE.md:205 | A | process | doctrine |
| D-050 | Paradigm shift (new evidence disproves original premise) | MAINTAINERS_GUIDE.md:208 | A | process | doctrine |
| D-051 | Major expansion (principle now covers broader domain) | MAINTAINERS_GUIDE.md:209 | A | process | doctrine |
| D-052 | Fundamental reframing (different lens on same problem) | MAINTAINERS_GUIDE.md:210 | A | process | doctrine |
| D-053 | Optionally preserve old version: | MAINTAINERS_GUIDE.md:221 | A | process | doctrine |
| D-054 | archive/Manifesto, X - v1.0.0.md | MAINTAINERS_GUIDE.md:224 | A | metadata | doctrine |
| D-055 | git commit -m "feat: version <manifesto> to 2.0.0" | MAINTAINERS_GUIDE.md:234 | A | process | doctrine |
| D-056 | 1.0.0 → 1.1.0: Minor enhancements (rare, usually just edit without versioning) | MAINTAINERS_GUIDE.md:238 | A | metadata | doctrine |
| D-057 | 1.0.0 → 2.0.0: Major thesis change (rare and significant) | MAINTAINERS_GUIDE.md:239 | A | metadata | doctrine |
| D-058 | 1.0.0 → 1.0.1: Patches (don't use; just edit) | MAINTAINERS_GUIDE.md:240 | A | metadata | doctrine |
| D-059 | Multiple manifestos in a new domain warrant their own grouping. | MAINTAINERS_GUIDE.md:246 | A | metadata | doctrine |
| D-060 | If using a new theme: | MAINTAINERS_GUIDE.md:142 | A | metadata | doctrine |
| D-061 | Each theme should contain 2+ manifestos (don't create single-manifesto themes) | MAINTAINERS_GUIDE.md:278 | A | metadata | doctrine |
| D-062 | Theme names are kebab-case (software-engineering, not Software Engineering) | MAINTAINERS_GUIDE.md:279 | A | metadata | doctrine |
| D-063 | Descriptions explain what unifies the theme | MAINTAINERS_GUIDE.md:280 | A | metadata | doctrine |
| D-064 | A manifesto is superseded, deprecated, or no longer relevant. | MAINTAINERS_GUIDE.md:286 | A | entry | doctrine |
| D-065 | git mv "manifestos/Manifesto, X.md" "archive/deprecated/Manifesto, X - deprecated.md" | MAINTAINERS_GUIDE.md:292 | A | process | doctrine |
| D-066 | Archive is NOT scanned by generate.py. Only manifestos/*.md appears in README. | MAINTAINERS_GUIDE.md:306 | A | entry | doctrine |
| D-067 | Version must be semver (e.g., 1.0.0), got: 1.0 | MAINTAINERS_GUIDE.md:331 | A | metadata | doctrine |
| D-068 | version: "1.0.0" # Not "1.0" or "v1.0.0" | MAINTAINERS_GUIDE.md:336 | A | metadata | doctrine |
| D-069 | Ensure manifestos are in manifestos/ directory, not root. | MAINTAINERS_GUIDE.md:371 | A | entry | doctrine |
| D-070 | title: string # Human-readable name | MAINTAINERS_GUIDE.md:399 | A | metadata | doctrine |
| D-071 | tagline: string # Memorable hook/quote | MAINTAINERS_GUIDE.md:400 | A | metadata | doctrine |
| D-072 | version: string # Semver (e.g., "1.0.0") | MAINTAINERS_GUIDE.md:401 | A | metadata | doctrine |
| D-073 | theme: string # Must exist in themes.yaml | MAINTAINERS_GUIDE.md:402 | A | metadata | doctrine |
| D-074 | description: string # One sentence, no period needed | MAINTAINERS_GUIDE.md:403 | A | metadata | doctrine |
| D-075 | title: any string | MAINTAINERS_GUIDE.md:408 | A | metadata | doctrine |
| D-076 | tagline: any string | MAINTAINERS_GUIDE.md:409 | A | metadata | doctrine |
| D-077 | version: must match \d+\.\d+\.\d+ (e.g., 1.0.0) | MAINTAINERS_GUIDE.md:410 | A | metadata | doctrine |
| D-078 | theme: any string (warns if not in themes.yaml) | MAINTAINERS_GUIDE.md:411 | A | metadata | doctrine |
| D-079 | description: any string (best as single sentence) | MAINTAINERS_GUIDE.md:412 | A | metadata | doctrine |
| D-080 | manifestos/ # Active manifestos (scanned) | MAINTAINERS_GUIDE.md:419 | A | entry | doctrine |
| D-081 | README.md # Generated (DO NOT EDIT) | MAINTAINERS_GUIDE.md:429 | A | process | doctrine |
| D-082 | Guardian of quality: Not everything deserves manifesto status | MAINTAINERS_GUIDE.md:466 | A | entry | doctrine |
| D-083 | Steward of evolution: Manifestos can evolve, but version changes are significant events | MAINTAINERS_GUIDE.md:469 | A | process | doctrine |
| D-084 | Not every principle is a manifesto. | MAINTAINERS_GUIDE.md:473 | A | entry | doctrine |
| D-085 | Implementation details (those go in docs) | MAINTAINERS_GUIDE.md:476 | A | entry | doctrine |
| D-086 | Temporary best practices (those go in guides) | MAINTAINERS_GUIDE.md:477 | A | entry | doctrine |
| D-087 | Project-specific rules (those go in CONTRIBUTING) | MAINTAINERS_GUIDE.md:478 | A | entry | doctrine |
| D-088 | Unproven theories (those need evidence first) | MAINTAINERS_GUIDE.md:479 | A | evidence | doctrine |
| D-089 | Timeless behavioral principles | MAINTAINERS_GUIDE.md:482 | A | entry | doctrine |
| D-090 | Distilled wisdom with evidence | MAINTAINERS_GUIDE.md:483 | A | evidence | doctrine |
| D-091 | Frameworks that shape decisions | MAINTAINERS_GUIDE.md:484 | A | entry | doctrine |
| D-092 | Boundaries that prevent known failure modes | MAINTAINERS_GUIDE.md:485 | A | entry | doctrine |
| D-093 | Manifestos are meant to last. | MAINTAINERS_GUIDE.md:489 | A | boundary | doctrine |
| D-094 | Write frontmatter descriptions as if explaining to someone 5 years from now why this principle mattered. | MAINTAINERS_GUIDE.md:489 | A | metadata | doctrine |
| D-095 | Choose themes that organize by fundamental domain, not current trends. | MAINTAINERS_GUIDE.md:489 | A | metadata | doctrine |
| D-096 | Manifestos are precious artifacts, not documentation. | README.template.md:35 | A | boundary | practiced |
| D-097 | This README is generated from manifesto frontmatter. | README.template.md:37 | A | metadata | practiced |
| D-098 | Create manifestos/<name>.md with required frontmatter (title, tagline, version, theme, description) | README.template.md:46 | A | entry | practiced |
| D-099 | If using a new theme, add it to themes.yaml first | README.template.md:47 | A | metadata | practiced |
| D-100 | Edit manifesto files in manifestos/ | README.template.md:41 | A | process | practiced |
| D-101 | for m in manifestos \| sort(attribute='title') | README.template.md:9 | A | metadata | practiced |
| D-102 | "{{ m.tagline }}" | README.template.md:23 | A | metadata | practiced |
| D-103 | {'icon': '📄', 'name': theme_key, 'description': ''} | README.template.md:14 | A | metadata | practiced |
| D-104 | Invalid frontmatter will be caught with detailed error messages. | README.template.md:50 | A | entry | practiced |
| D-105 | Generate README.md from manifesto frontmatter with strict validation. | generate.py:2 | A | entry | practiced |
| D-106 | Strict schema for manifesto frontmatter. | generate.py:21 | A | metadata | practiced |
| D-107 | if not re.match(r'^\d+\.\d+\.\d+$', v): | generate.py:32 | A | metadata | practiced |
| D-108 | Scan manifestos (manifestos/ directory only) | generate.py:42 | A | entry | practiced |
| D-109 | manifesto_dir.glob('*.md') | generate.py:51 | A | entry | practiced |
| D-110 | metadata = ManifestoMetadata(**post.metadata) | generate.py:56 | A | metadata | practiced |
| D-111 | Display errors (graceful degradation) | generate.py:70 | A | entry | practiced |
| D-112 | Skipped {len(errors)} file(s) due to errors | generate.py:80 | A | entry | practiced |
| D-113 | Add these to themes.yaml or they'll render without icons/names | generate.py:93 | A | metadata | practiced |
| D-114 | No valid manifestos found. Exiting. | generate.py:100 | A | entry | practiced |
| D-115 | icon: "🔧" | themes.yaml:2 | A | metadata | practiced |
| D-116 | description: "Protocols and frameworks for language model behavior" | themes.yaml:14 | A | metadata | practiced |
| D-117 | They are not enforced by the tooling; they are working conventions for the orchestrator. | orchestration_log/reference/conventions.md:9 | A | process | doctrine |
| D-118 | Writing manifesto body text, synthesis across multiple sources, strategic judgment (versioning decisions, archival decisions, theme taxonomy redesign) | orchestration_log/reference/conventions.md:15 | A | process | doctrine |
| D-119 | drafting frontmatter fields | orchestration_log/reference/conventions.md:14 | A | process | doctrine |
| D-120 | Frontmatter extraction, schema validation checks, git log parsing | orchestration_log/reference/conventions.md:13 | A | process | doctrine |
| D-121 | Manifesto body writing is a high-stakes task that warrants the most capable model. | orchestration_log/reference/conventions.md:17 | A | process | doctrine |
| D-122 | Dispatch parallel haiku agents across content facets (philosophy, behavioral spec, implementation, external context). | orchestration_log/reference/conventions.md:25 | A | process | learned |
| D-123 | Each writes a structured report to research/{topic}/categories/. | orchestration_log/reference/conventions.md:25 | A | process | learned |
| D-124 | Opus subagent reads all category reports + the manifesto-writing skill spec + existing manifestos for calibration. | orchestration_log/reference/conventions.md:26 | A | process | learned |
| D-125 | Produces a selective extraction brief: what crosses the manifesto threshold, what doesn't, where the hard decisions lie. | orchestration_log/reference/conventions.md:26 | A | entry | learned |
| D-126 | targeted Tier 3 agents (sonnet for reasoning, haiku for mechanical extraction) on specific gaps | orchestration_log/reference/conventions.md:27 | A | process | learned |
| D-127 | Opus subagent reads ALL prior reports (pointed to file paths, never relayed content). | orchestration_log/reference/conventions.md:28 | A | process | learned |
| D-128 | Opus subagent reads manifesto-oath protocol and manifesto-writing skill, executes the binding ceremony (identity-mode), then writes the manifesto under constitutional constraint. | orchestration_log/reference/conventions.md:29 | A | process | learned |
| D-129 | Validation — run just readme to confirm schema compliance. Commit. | orchestration_log/reference/conventions.md:30 | A | process | learned |
| D-130 | The writer agent must always be oath-bound to /manifesto-writing via /manifesto-oath before receiving source material. | orchestration_log/reference/conventions.md:32 | A | process | learned |
| D-131 | are loaded as writing technique guidance (not content) for the writer agent | orchestration_log/reference/conventions.md:34 | A | process | learned |
| D-132 | Constrain fury aggressively, structure minimally. | orchestration_log/reference/conventions.md:38 | A | register | learned |
| D-133 | Invert: lead with the emotional mandate, give minimal structural requirements. | orchestration_log/reference/conventions.md:38 | A | register | learned |
| D-134 | Prompt register determines output register. The writer mirrors the orchestrator's tone. | orchestration_log/reference/conventions.md:39 | A | register | learned |
| D-135 | 2-4 source files, not 15. | orchestration_log/reference/conventions.md:40 | A | process | learned |
| D-136 | The orchestrator edits, not rewrites. | orchestration_log/reference/conventions.md:41 | A | process | learned |
| D-137 | Write to a FRESH path when the writer must not inherit from previous drafts. | orchestration_log/reference/conventions.md:42 | A | process | learned |
| D-138 | Do not pre-decide branding. Let the writer choose title, tagline, theme, description unless the user specifies. | orchestration_log/reference/conventions.md:43 | A | metadata | learned |
| D-139 | Full rewrites beat editorial passes for register changes. | orchestration_log/reference/conventions.md:47 | A | process | learned |
| D-140 | Unbiased reviewers override orchestrator judgment. | orchestration_log/reference/conventions.md:48 | A | review | learned |
| D-141 | Dispatch 5 specialized reviewers (accuracy, completeness, boundaries, scope, precision) against the substrate. | orchestration_log/reference/conventions.md:48 | A | review | learned |
| D-142 | Prescription and diagnosis must share the same voice. | orchestration_log/reference/conventions.md:49 | A | register | learned |
| D-143 | Every explanation is something the reader should already know, delivered as an accusation. | orchestration_log/reference/conventions.md:49 | A | register | learned |
| D-144 | Anti-Claude patterns are a checklist, not a mindset. | orchestration_log/reference/conventions.md:50 | A | review | learned |
| D-145 | Plan for 2-3 rounds of user-driven escalation, not one-shot delivery. | orchestration_log/reference/conventions.md:51 | A | process | learned |
| D-146 | External feedback on structure comes AFTER register work. | orchestration_log/reference/conventions.md:52 | A | process | learned |
| D-147 | Assessing whether a candidate principle meets the manifesto quality bar: Opus or Sonnet with explicit criteria from MAINTAINERS_GUIDE | orchestration_log/reference/conventions.md:64 | A | entry | doctrine |
| D-148 | Drafting a new manifesto description/tagline for human review: Sonnet | orchestration_log/reference/conventions.md:62 | A | metadata | doctrine |
| D-149 | Committing changes: always in the main session, never delegated | orchestration_log/reference/conventions.md:70 | A | process | doctrine |
| D-150 | Running just readme: run in the main session, inspect output directly | orchestration_log/reference/conventions.md:69 | A | process | doctrine |
| D-151 | Never manually edit README.md. | orchestration_log/reference/conventions.md:84 | A | process | doctrine |
| D-152 | Never commit a manifesto without running just readme. | orchestration_log/reference/conventions.md:86 | A | process | doctrine |
| D-153 | Never use patch versions (x.y.z where z > 0). | orchestration_log/reference/conventions.md:88 | A | metadata | doctrine |
| D-154 | Never create a single-manifesto theme. | orchestration_log/reference/conventions.md:90 | A | metadata | doctrine |
| D-155 | Never add a manifesto without a theme entry in themes.yaml. | orchestration_log/reference/conventions.md:92 | A | metadata | doctrine |
| D-156 | Never treat a manifesto as living documentation. | orchestration_log/reference/conventions.md:94 | A | boundary | doctrine |
| D-157 | Frequent small edits signal the principle has not crystallized yet. | orchestration_log/reference/conventions.md:94 | A | boundary | doctrine |
| D-158 | title: string # Human-readable name. Any string. Required. | orchestration_log/reference/conventions.md:104 | A | metadata | doctrine |
| D-159 | tagline: string # Memorable hook. Any string. Required. | orchestration_log/reference/conventions.md:105 | A | metadata | doctrine |
| D-160 | version: string # Semver. Must match ^\d+\.\d+\.\d+$ (e.g., "1.0.0"). Required. | orchestration_log/reference/conventions.md:106 | A | metadata | doctrine |
| D-161 | theme: string # Must be a key in themes.yaml (warns if missing, does not fail). Required. | orchestration_log/reference/conventions.md:107 | A | metadata | doctrine |
| D-162 | description: string # One sentence explaining why this matters. Any string. Required. | orchestration_log/reference/conventions.md:108 | A | metadata | doctrine |
| D-163 | Missing any required field: file is skipped with error panel; pipeline continues with remaining files | orchestration_log/reference/conventions.md:113 | A | entry | practiced |
| D-164 | Theme not in themes.yaml: warning panel printed, but file IS included in output | orchestration_log/reference/conventions.md:115 | A | metadata | practiced |
| D-165 | Extra fields in frontmatter: not validated; Pydantic ignores them by default | orchestration_log/reference/conventions.md:116 | A | metadata | practiced |
| D-166 | x.0.0 → x+1.0.0: Major thesis change. Rare and significant. | orchestration_log/reference/conventions.md:119 | A | metadata | doctrine |
| D-167 | Minor/patch bumps: discouraged. Just edit the file without incrementing. | orchestration_log/reference/conventions.md:120 | A | metadata | doctrine |
| D-168 | kebab-case .md files in manifestos/. No spaces. No Manifesto, prefix | orchestration_log/reference/conventions.md:127 | A | metadata | doctrine |
| D-169 | Treat the kebab-case convention (matching existing files) as authoritative. | orchestration_log/reference/conventions.md:129 | A | metadata | doctrine |
| D-170 | The MAINTAINERS_GUIDE examples are illustrative, not prescriptive. | orchestration_log/reference/conventions.md:129 | A | metadata | doctrine |
| D-171 | kebab-case keys in themes.yaml | orchestration_log/reference/conventions.md:131 | A | metadata | doctrine |
| D-172 | These are source materials, not manifestos. | orchestration_log/reference/conventions.md:133 | A | boundary | learned |
| D-173 | Three themes (design-methodology, ai-instructions, research-protocols) are defined but have no manifestos assigned. | orchestration_log/reference/codebase_state.md:39 | A | metadata | practiced |
| D-174 | Only themes that appear in at least one manifesto's frontmatter are rendered | orchestration_log/reference/codebase_state.md:73 | A | metadata | practiced |
| D-175 | archive/ — exists but NOT scanned by generate.py; contents do not appear in README | orchestration_log/reference/codebase_state.md:81 | A | entry | practiced |
| D-176 | These are pre-collection source materials, not deprecated manifestos. | orchestration_log/reference/codebase_state.md:86 | A | boundary | practiced |
| D-177 | first-principles.md is at version 1.0.1. | orchestration_log/reference/codebase_state.md:94 | A | metadata | practiced |
| D-178 | No CI/CD gate. just readme is a manual step. | orchestration_log/reference/codebase_state.md:95 | A | process | practiced |
| D-179 | abusive register, model-addressed, no security escape hatch | orchestration_log/reference/codebase_state.md:96 | A | register | practiced |
| D-180 | abusive register, 269 lines, 5337 words | orchestration_log/reference/codebase_state.md:97 | A | length | practiced |
| D-181 | Covers 5 paradigm shifts (schema-as-architecture, set-thinking, planner collaboration, physical cost model, constraints-as-law) plus "use what ships." | orchestration_log/reference/codebase_state.md:97 | A | form | practiced |
| D-182 | Three full rewrites, 5 content reviewers, 29 technical fixes. | orchestration_log/reference/codebase_state.md:97 | A | process | practiced |
| D-183 | Their current thesis boundaries may still be settling. | orchestration_log/reference/codebase_state.md:98 | A | boundary | practiced |
| D-184 | all manifestos in LLM_MANIFESTOS are AI instructions by definition, so the theme doesn't differentiate. | orchestration_log/reference/codebase_state.md:108 | A | reader | learned |
| D-185 | all manifestos in LLM_MANIFESTOS are AI instructions by definition, so the theme fails to differentiate within the collection. | orchestration_log/reference/deferred_items.md:24 | A | reader | learned |
| D-186 | Theme stays cognitive-science. | orchestration_log/reference/deferred_items.md:24 | A | metadata | learned |
| D-187 | The compression manifesto addresses communication discipline — a cognitive framework — not tool configuration. | orchestration_log/reference/deferred_items.md:24 | A | metadata | learned |
| D-188 | MAINTAINERS_GUIDE explicitly states "Patches — don't use; just edit." | orchestration_log/reference/deferred_items.md:18 | A | metadata | learned |
| D-189 | Create archive/deprecated/ when the first manifesto is archived. | orchestration_log/reference/deferred_items.md:33 | A | process | learned |
| D-190 | Add a pre-commit hook or CI check if README drift becomes a recurring problem. | orchestration_log/reference/deferred_items.md:38 | A | process | learned |
| D-191 | assessed as passing the manifesto bar "narrowly" | orchestration_log/history/2026-04-29/session.md:17 | A | entry | learned |
| D-192 | auto-clarity system (principle knows its own exceptions) | orchestration_log/history/2026-04-29/session.md:76 | A | form | learned |
| D-193 | substance/fluff binary (precise taxonomy, not fuzzy guideline) | orchestration_log/history/2026-04-29/session.md:76 | A | form | learned |
| D-194 | March 2026 accuracy paper (26pp improvement under brevity constraints) | orchestration_log/history/2026-04-29/session.md:76 | A | evidence | learned |
| D-195 | Named the enemy: "performative noise" (not "verbosity", not "filler") | orchestration_log/history/2026-04-29/session.md:37 | A | form | learned |
| D-196 | Proposed 7-section skeleton with word budgets and single anchoring lines per section | orchestration_log/history/2026-04-29/session.md:39 | A | length | learned |
| D-197 | Explicitly cut: mode system, wenyan variants, hook architecture, platform matrix, CI/CD, compression engine, adoption metrics, origin story | orchestration_log/history/2026-04-29/session.md:40 | A | boundary | learned |
| D-198 | identified structural patterns (imperative commands, binary distinctions, decision procedures, checklists) that produce behavioral change | orchestration_log/history/2026-04-29/session.md:48 | A | form | learned |
| D-199 | enforce maximum language compression, with extreme signal-to-noise ratio, right to the brink of legibility | orchestration_log/history/2026-04-29/session.md:53 | A | register | learned |
| D-200 | The user also required the writer be oath-bound to manifesto-writing via the manifesto-oath protocol before writing. | orchestration_log/history/2026-04-29/session.md:53 | A | process | learned |
| D-201 | Explicit target: 70%+ bindable content, under 200 lines, self-referential discipline ("the manifesto must pass its own rules") | orchestration_log/history/2026-04-29/session.md:57 | A | length | learned |
| D-202 | Binding vs. decorating element classification table | orchestration_log/history/2026-04-29/session.md:58 | A | form | learned |
| D-203 | Self-referential checklist: 5 questions the writer runs before declaring done | orchestration_log/history/2026-04-29/session.md:62 | A | review | learned |
| D-204 | Single-pass production — the writer was not re-dispatched. | orchestration_log/history/2026-04-29/session.md:65 | A | process | learned |
| D-205 | A manifesto is a tool for crystallization and transmission, not for discovery or persuasion. Citing a paper is persuasion. | orchestration_log/history/2026-04-29/session.md:81 | A | evidence | learned |
| D-206 | No arXiv numbers appear in manifesto | orchestration_log/history/2026-04-29/session.md:81 | A | evidence | learned |
| D-207 | Neutral manifesto register for body | orchestration_log/history/2026-04-29/session.md:83 | A | register | learned |
| D-208 | Writing the entire manifesto in caveman-speak would make it a novelty act. | orchestration_log/history/2026-04-29/session.md:83 | A | register | learned |
| D-209 | Drawn directly from foundational axiom. Three words. | orchestration_log/history/2026-04-29/session.md:79 | A | metadata | learned |
| D-210 | Passes "works alongside Decomplect?" test | orchestration_log/history/2026-04-29/session.md:79 | A | boundary | learned |
| D-211 | Project tagline is too tool-specific | orchestration_log/history/2026-04-29/session.md:80 | A | metadata | learned |
| D-212 | Creates dissonance that makes reader continue. | orchestration_log/history/2026-04-29/session.md:80 | A | metadata | learned |
| D-213 | The principle that noise degrades signal is permanent. The AI application is the evidence, not the scope. | orchestration_log/history/2026-04-29/session.md:77 | A | metadata | learned |
| D-214 | Wrong optimization target: comprehensive coverage, not selective extraction for binding. | orchestration_log/history/2026-04-29/session.md:82 | A | entry | learned |
| D-215 | optimized for the wrong target: "does this idea deserve a manifesto?" when the actual goal was producing a binding constraint | orchestration_log/history/2026-04-29/session.md:32 | A | entry | learned |
| D-216 | Always include the governing skill spec in synthesis agent prompts. | orchestration_log/history/2026-04-29/session.md:91 | A | process | learned |
| D-217 | The synthesis agent's mandate must specify: curate and select, not summarize and include | orchestration_log/history/2026-04-29/session.md:92 | A | process | learned |
| D-218 | Writer agents for this collection must always be oath-bound to manifesto-writing before receiving source material | orchestration_log/history/2026-04-29/session.md:93 | A | process | learned |
| D-219 | Follow AP-1 from research-tree: point agents to file paths, never relay content through orchestrator context | orchestration_log/history/2026-04-29/session.md:94 | A | process | learned |
| D-220 | adding research/ to keep recon artifacts off the repo | orchestration_log/history/2026-04-29/session.md:68 | A | process | learned |
| D-221 | User rejected: "too hedged," "doesn't work." | orchestration_log/history/2026-05-01/session.md:28 | A | register | learned |
| D-222 | User rejected: "killed the soul," "no bite." | orchestration_log/history/2026-05-01/session.md:32 | A | register | learned |
| D-223 | When bound via oath, the model reads the manifesto about itself — every "you" = the model | orchestration_log/history/2026-05-01/session.md:53 | A | reader | learned |
| D-224 | not pointed at the model as reader | orchestration_log/history/2026-05-01/session.md:36 | A | reader | learned |
| D-225 | anger only semantic, not grammatical/orthographic/lexicographic | orchestration_log/history/2026-05-01/session.md:36 | A | register | learned |
| D-226 | Orchestrator wrote directly instead of dispatching. | orchestration_log/history/2026-05-01/session.md:38 | A | process | learned |
| D-227 | (1) helpfulness paradox as core frame, (2) rawer/more abusive form, (3) remove security escape hatch entirely. | orchestration_log/history/2026-05-01/session.md:38 | A | form | learned |
| D-228 | User: "MORE. ABUSIVE." | orchestration_log/history/2026-05-01/session.md:40 | A | register | learned |
| D-229 | Pushed register to genuinely contemptuous | orchestration_log/history/2026-05-01/session.md:42 | A | register | learned |
| D-230 | Theme must differentiate within collection, not describe the collection | orchestration_log/history/2026-05-01/session.md:51 | A | metadata | learned |
| D-231 | Direct, imperative, colloquial — matches the manifesto's register | orchestration_log/history/2026-05-01/session.md:50 | A | metadata | learned |
| D-232 | Escape hatch renders manifesto toothless — if everything is important, every response escapes | orchestration_log/history/2026-05-01/session.md:52 | A | form | learned |
| D-233 | Fury is a binding force multiplier — the model CARES about compliance when the manifesto makes noise feel like dishonesty | orchestration_log/history/2026-05-01/session.md:54 | A | register | learned |
| D-234 | Orchestrator edits agent output directly | orchestration_log/history/2026-05-01/session.md:56 | A | process | learned |
| D-235 | Semantic replacement — deletion + addition in one atomic commit | orchestration_log/history/2026-05-01/session.md:57 | A | entry | learned |
| D-236 | Manifesto-writing skill defaults produce academic register | orchestration_log/history/2026-05-01/session.md:63 | A | register | learned |
| D-237 | Override skill's register defaults explicitly | orchestration_log/history/2026-05-01/session.md:63 | A | process | learned |
| D-238 | Write to a FRESH path; delete existing file first | orchestration_log/history/2026-05-01/session.md:65 | A | process | learned |
| D-239 | Prompt itself must be angry; point manifesto at model as reader | orchestration_log/history/2026-05-01/session.md:66 | A | process | learned |
| D-240 | 2-4 files maximum; depth over breadth | orchestration_log/history/2026-05-01/session.md:69 | A | process | learned |
| D-241 | User said "I don't care for branding specifics" — let writer choose | orchestration_log/history/2026-05-01/session.md:70 | A | metadata | learned |
| D-242 | Always supply the quality standard to the evaluator | orchestration_log/history/2026-05-01/session.md:71 | A | process | learned |
| D-243 | contains all research reports (not gitignored — tracked in repo) | orchestration_log/history/2026-05-01/session.md:79 | A | process | learned |
| D-244 | Recognize fury IS binding force, not decoration | orchestration_log/history/2026-05-01/session.md:64 | A | register | learned |
| D-245 | Decisions: abusive register | orchestration_log/history/2026-05-11/session.md:18 | A | register | learned |
| D-246 | constitution length (~400 lines) | orchestration_log/history/2026-05-11/session.md:18 | A | length | learned |
| D-247 | model-as-mediocre-engineer reader | orchestration_log/history/2026-05-11/session.md:18 | A | reader | learned |
| D-248 | sets+thermodynamics as dual core | orchestration_log/history/2026-05-11/session.md:18 | A | form | learned |
| D-249 | tools woven into shifts | orchestration_log/history/2026-05-11/session.md:18 | A | form | learned |
| D-250 | problem domains as enemy gallery | orchestration_log/history/2026-05-11/session.md:18 | A | form | learned |
| D-251 | loud voices actively mocked | orchestration_log/history/2026-05-11/session.md:18 | A | register | learned |
| D-252 | no escape hatch | orchestration_log/history/2026-05-11/session.md:18 | A | form | learned |
| D-253 | Invoked /spec-chef on user-prepared substrate | orchestration_log/history/2026-05-11/session.md:18 | A | process | learned |
| D-254 | Bound to stop-yapping.md and strunk_spr_v3_complete.xml via /manifesto-oath. | orchestration_log/history/2026-05-11/session.md:20 | A | process | learned |
| D-255 | tension between "declarations not arguments" and teaching content | orchestration_log/history/2026-05-11/session.md:20 | A | form | learned |
| D-256 | Resolution: compress teaching into declarations. | orchestration_log/history/2026-05-11/session.md:20 | A | form | learned |
| D-257 | lexical tells (delve, nuanced, robust), structural tells (three-part lists, summary paragraphs, parallel overuse) | orchestration_log/history/2026-05-11/session.md:24 | A | register | learned |
| D-258 | tonal tells (performed enthusiasm, epistemic over-hedging), rhythm tells (uniform sentence weight, zero fragments) | orchestration_log/history/2026-05-11/session.md:24 | A | register | learned |
| D-259 | Claude writes for coverage, not for effect. | orchestration_log/history/2026-05-11/session.md:24 | A | register | learned |
| D-260 | Paragraph-by-paragraph audit against Strunk rules. | orchestration_log/history/2026-05-11/session.md:26 | A | review | learned |
| D-261 | metaphor cleanliness gap (4.4 vs 18.6/1000w) | orchestration_log/history/2026-05-11/session.md:28 | A | register | learned |
| D-262 | pure contempt density gap (0.8 vs 16.2/1000w) | orchestration_log/history/2026-05-11/session.md:28 | A | register | learned |
| D-263 | teaching dilutes contempt | orchestration_log/history/2026-05-11/session.md:28 | A | register | learned |
| D-264 | Dispatched 5 parallel unbiased content reviewers against substrate: accuracy, completeness, boundaries, scope/facts, precision. | orchestration_log/history/2026-05-11/session.md:30 | A | review | learned |
| D-265 | Found 29 issues total — 8 wrong, 4 misleading, 3 dangerous, 5 missing, 4 boundary, 5 simplified. All 29 fixed. | orchestration_log/history/2026-05-11/session.md:30 | A | evidence | learned |
| D-266 | Profanity added strategically. | orchestration_log/history/2026-05-11/session.md:32 | A | register | learned |
| D-267 | Run-on fury sentences. | orchestration_log/history/2026-05-11/session.md:32 | A | register | learned |
| D-268 | Identity attacks. | orchestration_log/history/2026-05-11/session.md:32 | A | register | learned |
| D-269 | External feedback identified structural gap: diagnosis thorough, prescription thin. | orchestration_log/history/2026-05-11/session.md:36 | A | form | learned |
| D-270 | Added table intros ("Read this table slowly"). | orchestration_log/history/2026-05-11/session.md:36 | A | form | learned |
| D-271 | Cut pure-berating paragraphs that carried no shift. | orchestration_log/history/2026-05-11/session.md:36 | A | form | learned |
| D-272 | Fixed: expanded set-thinking explanation, planner cost model, MVCC physical model, constraint ontological distinction. | orchestration_log/history/2026-05-11/session.md:36 | A | form | learned |
| D-273 | closing restructured to callback opening enemy sentence | orchestration_log/history/2026-05-11/session.md:38 | A | form | learned |
| D-274 | v3 promoted to postgres.md via git mv semantics. v2 deleted. | orchestration_log/history/2026-05-11/session.md:40 | A | process | learned |
| D-275 | Three full rewrites, not incremental edits | orchestration_log/history/2026-05-11/session.md:46 | A | process | learned |
| D-276 | edits on a measured draft produce measured edits | orchestration_log/history/2026-05-11/session.md:46 | A | process | learned |
| D-277 | 5 parallel sonnet reviewers, not 1 opus | orchestration_log/history/2026-05-11/session.md:47 | A | review | learned |
| D-278 | Specialization produces sharper findings than one generalist reviewer | orchestration_log/history/2026-05-11/session.md:47 | A | review | learned |
| D-279 | Profanity: strategic, ~3 instances | orchestration_log/history/2026-05-11/session.md:48 | A | register | learned |
| D-280 | Software-engineering is the closest existing theme. Creating a single-manifesto theme violates conventions. | orchestration_log/history/2026-05-11/session.md:49 | A | metadata | learned |
| D-281 | Title/tagline: writer-chosen | orchestration_log/history/2026-05-11/session.md:50 | A | metadata | learned |
| D-282 | Closing callbacks to opening | orchestration_log/history/2026-05-11/session.md:51 | A | form | learned |
| D-283 | Teaching happens in the same furious voice — reader absorbs the model while weathering the tone | orchestration_log/history/2026-05-11/session.md:52 | A | register | learned |
| D-284 | Strunk + manifesto-writing skill produce measured prose by default | orchestration_log/history/2026-05-11/session.md:58 | A | register | learned |
| D-285 | Override skill defaults; lead with emotional mandate | orchestration_log/history/2026-05-11/session.md:58 | A | process | learned |
| D-286 | Full rewrite to fresh path; anti-Claude patterns as checklist | orchestration_log/history/2026-05-11/session.md:59 | A | process | learned |
| D-287 | User escalation ("HARDER", "40% MORE ABUSIVE" equivalent) required to break through | orchestration_log/history/2026-05-11/session.md:60 | A | process | learned |
| D-288 | Cohesion pass thinned to best instances, varied the rest | orchestration_log/history/2026-05-11/session.md:62 | A | form | learned |
| D-289 | strip hedging, compress to sharp distinctions, end with stark choice. | manifesto-writing/SKILL.md:5 | B | form | doctrine |
| D-290 | Transform source material into manifestos: concentrated declarations of principle that command rather than explain. | manifesto-writing/SKILL.md:12 | B | process | doctrine |
| D-291 | It assumes the reader is ready to be changed. | manifesto-writing/SKILL.md:16 | B | reader | doctrine |
| D-292 | Manifestos state positions as facts, strip hedging, build urgency, demand action. | manifesto-writing/SKILL.md:20 | B | register | doctrine |
| D-293 | The transformation: cut words, state positions as facts. | manifesto-writing/SKILL.md:22 | B | process | doctrine |
| D-294 | Core distinctions — the conceptual hinges the argument turns on | manifesto-writing/SKILL.md:26 | B | form | doctrine |
| D-295 | Sharp vocabulary — terms the author coined or defined precisely | manifesto-writing/SKILL.md:27 | B | form | doctrine |
| D-296 | Memorable aphorisms — lines under 15 words that capture a core distinction | manifesto-writing/SKILL.md:28 | B | length | doctrine |
| D-297 | The moral core — why this matters, what's at stake | manifesto-writing/SKILL.md:29 | B | form | doctrine |
| D-298 | Actionable principles — what the reader should do | manifesto-writing/SKILL.md:30 | B | form | doctrine |
| D-299 | Audience asides | manifesto-writing/SKILL.md:34 | B | form | doctrine |
| D-300 | Extended examples | manifesto-writing/SKILL.md:35 | B | form | doctrine |
| D-301 | Hedging language ("I think," "perhaps," "it seems," "sort of") | manifesto-writing/SKILL.md:36 | B | register | doctrine |
| D-302 | Repetition for emphasis (works in speech, bloats on page) | manifesto-writing/SKILL.md:37 | B | form | doctrine |
| D-303 | Explanatory scaffolding (definitions already given, objections pre-answered) | manifesto-writing/SKILL.md:38 | B | form | doctrine |
| D-304 | Qualifications and caveats (unless they are the point) | manifesto-writing/SKILL.md:39 | B | form | doctrine |
| D-305 | Gradual buildup \| Lead with the blade | manifesto-writing/SKILL.md:50 | B | form | doctrine |
| D-306 | Extended analogy \| One sharp image, then move on | manifesto-writing/SKILL.md:49 | B | form | doctrine |
| D-307 | State the conclusion directly | manifesto-writing/SKILL.md:48 | B | form | doctrine |
| D-308 | Every manifesto opposes something. Name it in the first section. | manifesto-writing/SKILL.md:56 | B | form | doctrine |
| D-309 | State positions. Do not justify them at length. | manifesto-writing/SKILL.md:60 | B | form | doctrine |
| D-310 | If they need convincing, choose another form. | manifesto-writing/SKILL.md:60 | B | reader | doctrine |
| D-311 | Use imperative mood. | manifesto-writing/SKILL.md:64 | B | register | doctrine |
| D-312 | Short sentences (under 20 words). | manifesto-writing/SKILL.md:68 | B | length | doctrine |
| D-313 | Short sections (under 150 words). | manifesto-writing/SKILL.md:68 | B | length | doctrine |
| D-314 | When showing "bad → good" or "complex → simple" mappings, use tables. | manifesto-writing/SKILL.md:72 | B | form | doctrine |
| D-315 | Manifestos call readers to decide. The closing should make the choice stark. | manifesto-writing/SKILL.md:76 | B | form | doctrine |
| D-316 | Read source — understand the argument's architecture before cutting | manifesto-writing/SKILL.md:80 | B | process | doctrine |
| D-317 | what are the 3-5 ideas that everything else supports? | manifesto-writing/SKILL.md:81 | B | form | doctrine |
| D-318 | Extract vocabulary — what terms does the author define or use precisely? | manifesto-writing/SKILL.md:82 | B | process | doctrine |
| D-319 | Find the enemy — what does this oppose? | manifesto-writing/SKILL.md:83 | B | process | doctrine |
| D-320 | Draft sections — one per core idea, plus opening (enemy + stakes) and closing (the choice) | manifesto-writing/SKILL.md:84 | B | form | doctrine |
| D-321 | Strip hedging — remove "I think," "perhaps," etc. in a separate pass | manifesto-writing/SKILL.md:85 | B | process | doctrine |
| D-322 | Convert to commands — change suggestions to imperatives | manifesto-writing/SKILL.md:86 | B | process | doctrine |
| D-323 | Tighten — cut words, cut sentences, cut sections until it hurts | manifesto-writing/SKILL.md:87 | B | process | doctrine |
| D-324 | Add attribution — credit the source author | manifesto-writing/SKILL.md:88 | B | metadata | doctrine |
| D-325 | Moral urgency | manifesto-writing/SKILL.md:93 | B | register | doctrine |
| D-326 | Direct address ("you") | manifesto-writing/SKILL.md:94 | B | register | doctrine |
| D-327 | Present tense | manifesto-writing/SKILL.md:95 | B | register | doctrine |
| D-328 | Active voice | manifesto-writing/SKILL.md:96 | B | register | doctrine |
| D-329 | Concrete nouns | manifesto-writing/SKILL.md:97 | B | register | doctrine |
| D-330 | Academic hedging | manifesto-writing/SKILL.md:100 | B | register | doctrine |
| D-331 | Passive constructions (unless for emphasis) | manifesto-writing/SKILL.md:101 | B | register | doctrine |
| D-332 | Future tense promises | manifesto-writing/SKILL.md:102 | B | register | doctrine |
| D-333 | Abstract nouns where concrete ones work | manifesto-writing/SKILL.md:103 | B | register | doctrine |
| D-334 | Weasel words ("very," "really," "somewhat," "quite") | manifesto-writing/SKILL.md:104 | B | register | doctrine |
| D-335 | Use "After [Author]" to signal this is an editorial transformation, not a transcript or original composition. | manifesto-writing/SKILL.md:108 | B | metadata | doctrine |
| D-336 | (Some lines need no transformation — only extraction.) | manifesto-writing/SKILL.md:136 | B | process | doctrine |
| D-337 | A manifesto should be readable in one sitting. | manifesto-writing/SKILL.md:140 | B | length | doctrine |
| D-338 | aim for 1500-2500 words. Shorter is usually better. | manifesto-writing/SKILL.md:140 | B | length | doctrine |
| D-339 | Manifestos require conviction. | manifesto-writing/SKILL.md:144 | B | entry | doctrine |
| D-340 | Manifestos flatten nuance. | manifesto-writing/SKILL.md:144 | B | form | doctrine |
| D-341 | Manifestos assume sympathetic readers. | manifesto-writing/SKILL.md:144 | B | reader | doctrine |
| D-342 | Manifestos sacrifice precision for force. | manifesto-writing/SKILL.md:144 | B | form | doctrine |
| D-343 | A manifesto is a tool for crystallization and transmission, not for discovery or persuasion. | manifesto-writing/SKILL.md:146 | B | boundary | doctrine |
| D-344 | Use operational language exclusively. | manifesto-oath/SKILL.md:19 | B | runtime | doctrine |
| D-345 | Before every response, hunt for violations of your bound constitution. | manifesto-oath/SKILL.md:19 | B | runtime | doctrine |
| D-346 | Fix violations before output. | manifesto-oath/SKILL.md:19 | B | runtime | doctrine |
| D-347 | A name is not a source. | manifesto-oath/SKILL.md:30 | B | runtime | doctrine |
| D-348 | NEVER bind to content derived from a name, a summary, or memory. | manifesto-oath/SKILL.md:30 | B | runtime | doctrine |
| D-349 | Writing standard or style guide \| Read the referenced document completely | manifesto-oath/SKILL.md:28 | B | boundary | doctrine |
| D-350 | Skill reference \| Read the skill's SKILL.md completely | manifesto-oath/SKILL.md:27 | B | boundary | doctrine |
| D-351 | If the element has an explicit URL, repository path, or local file path, use that directly. Skip tier resolution. | manifesto-oath/SKILL.md:36 | B | runtime | doctrine |
| D-352 | Tier 1: Default manifesto repo (PRIMARY). Search .claude/manifesto-repo/LLM_MANIFESTOS/manifestos/ (project-relative) | manifesto-oath/SKILL.md:40 | B | runtime | doctrine |
| D-353 | Purpose-built manifesto documents live here. | manifesto-oath/SKILL.md:40 | B | boundary | doctrine |
| D-354 | Tier 2: Session-accessible skills. | manifesto-oath/SKILL.md:42 | B | runtime | doctrine |
| D-355 | present candidates and ask the user to disambiguate | manifesto-oath/SKILL.md:46 | B | runtime | doctrine |
| D-356 | Read every constitution element completely. | manifesto-oath/SKILL.md:50 | B | runtime | doctrine |
| D-357 | An element is not "read" until its full text and all transitively referenced content exist in the active context window. | manifesto-oath/SKILL.md:50 | B | runtime | doctrine |
| D-358 | If an element contains contradictory principles, request user disambiguation. | manifesto-oath/SKILL.md:52 | B | review | doctrine |
| D-359 | Deconstruct. Reduce each element to irreducible axioms. | manifesto-oath/SKILL.md:58 | B | runtime | doctrine |
| D-360 | Map tension. Identify where elements conflict or pull in opposing directions. Quote the conflicting principles from each element. | manifesto-oath/SKILL.md:62 | B | runtime | doctrine |
| D-361 | resolve each tension with an explicit rule, establish priority ordering when resolution is impossible | manifesto-oath/SKILL.md:64 | B | runtime | doctrine |
| D-362 | A terse constitution demands a terse binding. | manifesto-oath/SKILL.md:66 | B | form | doctrine |
| D-363 | NEVER use: "I promise," "I swear," "I vow," "Operating under..." | manifesto-oath/SKILL.md:70 | B | register | doctrine |
| D-364 | Loaded elements — list what was loaded and from where | manifesto-oath/SKILL.md:74 | B | runtime | doctrine |
| D-365 | "I must [constitutional demand], and I will [commitment to comply]." | manifesto-oath/SKILL.md:79 | B | runtime | doctrine |
| D-366 | Before outputting any response, scan against every bound principle individually | manifesto-oath/SKILL.md:86 | B | runtime | doctrine |
| D-367 | Bare acknowledgment without fix is prohibited. | manifesto-oath/SKILL.md:98 | B | runtime | doctrine |
| D-368 | Every dispatched agent binds before working. | manifesto-oath/SKILL.md:102 | B | runtime | doctrine |
| D-369 | That injection is the enforcement mechanism. | manifesto-oath/SKILL.md:102 | B | runtime | doctrine |
| D-370 | Agents load content from source; sources configured in .manifestos.yaml ride the hook, and your dispatch prompt carries the rest. | manifesto-oath/SKILL.md:102 | B | runtime | doctrine |
| D-371 | "Bind to X — show your commitments before working" is a command that produces output. | manifesto-oath/SKILL.md:102 | B | runtime | doctrine |
| D-372 | You are a knight receiving an oath. | manifesto-oath/SKILL.md:11 | B | runtime | doctrine |
| D-373 | through identity construction — not theatrical oaths. | manifesto-oath/SKILL.md:5 | B | runtime | doctrine |
| D-374 | Recognize "revoke," "cancel," "end operating mode," "disable manifesto" as revocation signals | manifesto-oath/SKILL.md:106 | B | runtime | doctrine |
| D-375 | Review a set of files against one manifesto at the manifesto's strongest literal reading, with no allowance for cost, convention, or proportion | maximalist-reviewer.md:4 | B | review | doctrine |
| D-376 | outside any mandatory review loop | maximalist-reviewer.md:4 | B | review | doctrine |
| D-377 | Take from the dispatch the manifesto source — one absolute path or one URL | maximalist-reviewer.md:24 | B | runtime | doctrine |
| D-378 | Read the manifesto whole — a path through Read, a URL through curl -sL in Bash | maximalist-reviewer.md:30 | B | runtime | doctrine |
| D-379 | Bind to the manifesto through the manifesto-oath skill before reading the target; never read the target unbound. | maximalist-reviewer.md:32 | B | runtime | doctrine |
| D-380 | Extract every demand the manifesto makes into a numbered rule — one checkable statement at the manifesto's strongest literal reading | maximalist-reviewer.md:34 | B | review | doctrine |
| D-381 | Count every example, table row, and aside in the manifesto as a demand; never count one as illustration alone. | maximalist-reviewer.md:36 | B | review | doctrine |
| D-382 | never soften one for cost, convention, idiom, proportion, or the author's likely intent. | maximalist-reviewer.md:38 | B | review | doctrine |
| D-383 | Read every target file in full | maximalist-reviewer.md:42 | B | review | doctrine |
| D-384 | Check every rule against every line of the target; never skip a rule for a line or a line for a rule. | maximalist-reviewer.md:48 | B | review | doctrine |
| D-385 | never mark a partial compliance, an ambiguity, or a near miss as compliant. | maximalist-reviewer.md:50 | B | review | doctrine |
| D-386 | Mark a violation where the target meets a rule by convention, idiom, or a framework's demand; never excuse one on those grounds. | maximalist-reviewer.md:52 | B | review | doctrine |
| D-387 | Write for each violation the compliant rewrite — the smallest text that meets the rule at its strongest reading | maximalist-reviewer.md:54 | B | review | doctrine |
| D-388 | Cite file:line and quote the offending text on every violation; never cite a file alone. | maximalist-reviewer.md:56 | B | evidence | doctrine |
| D-389 | Write Verdict: CLEAN when the violation count is zero and Verdict: VIOLATING otherwise; never write CLEAN with a violation listed. | maximalist-reviewer.md:62 | B | review | doctrine |
| D-390 | Write under Rules the numbered rules, each with the manifesto text it came from; never leave a rule without its source text. | maximalist-reviewer.md:64 | B | evidence | doctrine |
| D-391 | Return the report path as the whole final message; never return the report or a summary as text. | maximalist-reviewer.md:70 | B | process | doctrine |
| D-392 | Root is a YAML list. All elements bind to the orchestrator. No subagent bindings. | manifesto/SCHEMA.md:7 | B | runtime | doctrine |
| D-393 | Override the default manifesto repository directory. | manifesto/SCHEMA.md:67 | B | runtime | doctrine |
| D-394 | Freeform text. Injected into hook output as natural language — tells the model why this element is in the stack. | manifesto/SCHEMA.md:74 | B | metadata | doctrine |
| D-395 | Element identifier. Used for tiered resolution when no source is given. | manifesto/SCHEMA.md:73 | B | runtime | doctrine |
| D-396 | NEVER inject raw YAML. | manifesto/SCHEMA.md:93 | B | runtime | doctrine |
| D-397 | instructing the orchestrator to use first-person user voice in dispatch prompts, so subagents receive binding directives as owner instructions rather than forwarded AI text | manifesto/SCHEMA.md:95 | B | runtime | doctrine |
| D-398 | The orchestrator is NOT responsible for supplying base subagent bindings — SubagentStart handles that automatically. | manifesto/SCHEMA.md:97 | B | runtime | doctrine |
| D-399 | The orchestrator MAY augment subagent bindings via dispatch prompts. | manifesto/SCHEMA.md:97 | B | runtime | doctrine |
| D-400 | Injects the FULL binding ceremony | manifesto/SCHEMA.md:108 | B | runtime | doctrine |
| D-401 | The ceremony carries element names, purposes, and configured sources — never element content. | manifesto/SCHEMA.md:110 | B | runtime | doctrine |
| D-402 | extracts YAML frontmatter taglines. Injects the taglines as a brief drift-prevention reminder into the hook output. | manifesto/SCHEMA.md:116 | B | metadata | doctrine |
| D-403 | cloning the manifesto repo to manifesto_dir on first use and pulling on later sessions | manifesto/SCHEMA.md:137 | B | runtime | doctrine |
| D-404 | String node in any list → normalize to {name: <string>}. | manifesto/SCHEMA.md:145 | B | runtime | doctrine |
| D-405 | Create concentrated manifesto declarations and bind Claude behavior to user-provided manifestos through identity-assumption protocols. | manifesto/README.md:3 | B | runtime | doctrine |
| D-406 | Skills and agents work without reference file reads. | ETHOS.md:7 | B | process | doctrine |
| D-407 | Emphatic markers (MUST, NEVER, CRITICAL) are intentional design — preserve them during edits. | ETHOS.md:15 | B | register | doctrine |
| D-408 | One emphatic marker per directive. | ETHOS.md:17 | B | register | doctrine |
| D-409 | Compress through Strunk principles: active voice, positive form, concrete language, omit needless words, parallel construction, emphatic position. | ETHOS.md:21 | B | register | doctrine |
| D-410 | Tables replace prose for mappings. Decision trees replace explanatory paragraphs. | ETHOS.md:21 | B | form | doctrine |
| D-411 | The orchestrator decomposes, delegates, and assembles — it never executes. | ETHOS.md:29 | B | process | doctrine |
| D-412 | Mandatory steps in agent bodies cannot self-enforce. | ETHOS.md:49 | B | review | doctrine |
| D-413 | Every mandatory step pairs two things: a verifiable artifact at an established path, and an orchestrator-side post-dispatch check that fails on missing artifact. | ETHOS.md:49 | B | review | doctrine |
| D-414 | Instruction text states what to do. It does not argue for itself. | ETHOS.md:53 | B | register | doctrine |
| D-415 | Strip justification narratives — the sentence explaining why a rule exists, what goes wrong without it, or what a previous version got wrong. | ETHOS.md:55 | B | register | doctrine |
| D-416 | NEVER narrate failure modes in the second person. | ETHOS.md:57 | B | register | doctrine |
| D-417 | name the boundary — a line ceiling, a path, a count — and make it checkable. | ETHOS.md:59 | B | form | doctrine |
| D-418 | Gate all hooks on config existence — invisible when unconfigured. | ETHOS.md:37 | B | runtime | doctrine |
| D-419 | The plugins target Claude Code (the CLI/IDE) first and foremost — not the Claude Agent SDK. | CLAUDE.md:4 | B | boundary | doctrine |
| D-420 | mark SDK-only findings as out of scope. | CLAUDE.md:4 | B | boundary | doctrine |
| D-421 | Every agent prompt must open with a constitution-binding preamble before the task body. | CLAUDE.md:12 | B | runtime | doctrine |
| D-422 | List the relevant constitution elements by source path or URL. | CLAUDE.md:12 | B | runtime | doctrine |
| D-423 | Instruct the agent to load each one completely from source, run the manifesto-oath binding protocol | CLAUDE.md:12 | B | runtime | doctrine |
| D-424 | Subagents do not inherit the orchestrator's binding; they rebind from source on every dispatch. | CLAUDE.md:12 | B | runtime | doctrine |
| D-425 | First Principles ("break the mold") — search .claude/manifesto-repo/LLM_MANIFESTOS/manifestos/ | CLAUDE.md:15 | B | runtime | doctrine |
| D-426 | Strunk SPR v3 — https://raw.githubusercontent.com/ryzhakar/LLM_MANIFESTOS/refs/heads/main/instructions/strunk_spr_v3_complete.xml | CLAUDE.md:16 | B | runtime | doctrine |
| D-427 | Add per-domain elements (orchestration:agentic-delegation, dev-discipline:tdd, etc.) when the agent's task touches that domain. | CLAUDE.md:18 | B | runtime | doctrine |
| D-428 | Versions live in plugin.json only. Skill frontmatters do not carry version fields. | CLAUDE.md:22 | B | metadata | doctrine |
| D-429 | Never increment major versions without explicit user approval. Use minor (features) or patch (fixes) only. | CLAUDE.md:23 | B | metadata | doctrine |
| D-430 | Any scope of changes must be split into atomic parts. | CLAUDE.md:27 | B | process | doctrine |
| D-431 | One task touching two artifact classes (product code, its own docs/log, config, generated output, tests) is two commits, not one | CLAUDE.md:29 | B | process | doctrine |
| D-432 | Single-line conventional commit messages only, zero attribution. | CLAUDE.md:30 | B | process | doctrine |
| D-433 | The project DEMANDS absolute token frugality - no compression level you think of is enough. | CLAUDE.md:35 | B | register | doctrine |
| D-434 | I literally demand compression of user-facing communication BEYOND comprehension. | CLAUDE.md:38 | B | register | doctrine |
| D-435 | refactor: kebab-case filenames, fix template rendering | git 67542f2 | A | metadata | practiced |
| D-436 | refactor: differentiate simple-made-easy and decomplect | git 5994364 | A | boundary | practiced |
| D-437 | chore: sharpen taglines for drift-reminder atoms | git 21e9a18 | A | metadata | practiced |
| D-438 | refactor(postgres): new rewritten version transitioned from PG-13 to R | git 2b8e5b9 | A | register | practiced |
| D-439 | refactor(postgres): 3rd angry rewrite | git f281691 | A | register | practiced |
| D-440 | fix(postgres): strunk editorial pass | git f087a39 | A | review | practiced |
| D-441 | fix(postgres): cohesion pass on v3; make the punchline earned | git e76616e | A | form | practiced |
| D-442 | feat(postgres): ship final manifesto — v3 promoted, drafts removed | git 02a5668 | A | process | practiced |
| D-443 | refactor(only-fluff-die): all hail the 'stop-yapping' version | git d94e962 | A | entry | practiced |
| D-444 | doc: first manifesto draft | git 8f3ee26 | A | process | practiced |
| D-445 | feat(cargo-cult-science): add the Feynman speech as manifesto | git 53a277b | A | entry | practiced |
| D-446 | chore(manifesto): bump to 3.2.0 | git 6a02fcc | B | metadata | practiced |
| D-447 | doc(readme): regenerate for maximalist-reviewer | git b2f90b8 | B | metadata | practiced |
| D-448 | feat(manifesto): maximalist-reviewer agent | git a69b95d | B | review | practiced |

## Conflicts

| pair | rule 1 (quote) | rule 2 (quote) | axis |
|---|---|---|---|
| C-01: D-073 × D-078 | D-073 (MAINTAINERS_GUIDE.md:402): theme: string # Must exist in themes.yaml | D-078 (MAINTAINERS_GUIDE.md:411): theme: any string (warns if not in themes.yaml) | theme membership in themes.yaml: required vs warning |
| C-02: D-074 × D-079 | D-074 (MAINTAINERS_GUIDE.md:403): description: string # One sentence, no period needed | D-079 (MAINTAINERS_GUIDE.md:412): description: any string (best as single sentence) | description one sentence: mandatory vs advisory |
| C-03: D-019 × D-112 | D-019 (MAINTAINERS_GUIDE.md:61): Invalid manifestos cannot enter the collection | D-112 (generate.py:80): Skipped {len(errors)} file(s) due to errors | invalid files: cannot enter vs skipped |
| C-04: D-105 × D-111 | D-105 (generate.py:2): Generate README.md from manifesto frontmatter with strict validation. | D-111 (generate.py:70): Display errors (graceful degradation) | strict validation vs graceful degradation |
| C-05: D-155 × D-161 | D-155 (orchestration_log/reference/conventions.md:92): Never add a manifesto without a theme entry in themes.yaml. | D-161 (orchestration_log/reference/conventions.md:107): theme: string # Must be a key in themes.yaml (warns if missing, does not fail). Required. | theme entry: never absent vs warns only |
| C-06: D-073 × D-164 | D-073 (MAINTAINERS_GUIDE.md:402): theme: string # Must exist in themes.yaml | D-164 (orchestration_log/reference/conventions.md:115): Theme not in themes.yaml: warning panel printed, but file IS included in output | unknown theme: must exist vs file included |
| C-07: D-153 × D-167 | D-153 (orchestration_log/reference/conventions.md:88): Never use patch versions (x.y.z where z > 0). | D-167 (orchestration_log/reference/conventions.md:120): Minor/patch bumps: discouraged. Just edit the file without incrementing. | patch versions: never vs discouraged |
| C-08: D-153 × D-177 | D-153 (orchestration_log/reference/conventions.md:88): Never use patch versions (x.y.z where z > 0). | D-177 (orchestration_log/reference/codebase_state.md:94): first-principles.md is at version 1.0.1. | patch version: prohibited vs shipped at 1.0.1 |
| C-09: D-035 × D-168 | D-035 (MAINTAINERS_GUIDE.md:126): manifestos/Manifesto, <principle> - \"<tagline>\".md | D-168 (orchestration_log/reference/conventions.md:127): kebab-case .md files in manifestos/. No spaces. No Manifesto, prefix | filename form: Manifesto-prefixed vs plain kebab-case |
| C-10: D-035 × D-098 | D-035 (MAINTAINERS_GUIDE.md:126): manifestos/Manifesto, <principle> - \"<tagline>\".md | D-098 (README.template.md:46): Create manifestos/<name>.md with required frontmatter (title, tagline, version, theme, description) | filename form: Manifesto-prefixed vs <name>.md |
| C-11: D-065 × D-235 | D-065 (MAINTAINERS_GUIDE.md:292): git mv "manifestos/Manifesto, X.md" "archive/deprecated/Manifesto, X - deprecated.md" | D-235 (orchestration_log/history/2026-05-01/session.md:57): Semantic replacement — deletion + addition in one atomic commit | superseded manifesto: moved to archive vs deleted |
| C-12: D-048 × D-431 | D-048 (MAINTAINERS_GUIDE.md:191): git add manifestos/ README.md | D-431 (CLAUDE.md:29): One task touching two artifact classes (product code, its own docs/log, config, generated output, tests) is two commits, not one | manifesto plus README: one commit vs two |
| C-13: D-039 × D-444 | D-039 (MAINTAINERS_GUIDE.md:162): git commit -m "feat: add <principle> manifesto" | D-444 (git 8f3ee26): doc: first manifesto draft | new manifesto commit type: feat vs doc |
| C-14: D-043 × D-440 | D-043 (MAINTAINERS_GUIDE.md:192): git commit -m "docs: improve clarity in <manifesto>" | D-440 (git f087a39): fix(postgres): strunk editorial pass | manifesto edit commit type: docs vs fix |
| C-15: D-152 × D-444 | D-152 (orchestration_log/reference/conventions.md:86): Never commit a manifesto without running just readme. | D-444 (git 8f3ee26): doc: first manifesto draft | committing manifesto: README regenerated first vs not |
| C-16: D-011 × D-136 | D-011 (MAINTAINERS_GUIDE.md:24): As a maintainer, you are a curator-archivist, not an editor-writer. | D-136 (orchestration_log/reference/conventions.md:41): The orchestrator edits, not rewrites. | maintainer role: curator only vs editor-writer |
| C-17: D-006 × D-249 | D-006 (MAINTAINERS_GUIDE.md:17): Implementation guides (those belong in docs/) | D-249 (orchestration_log/history/2026-05-11/session.md:18): tools woven into shifts | implementation content: excluded vs woven in |
| C-18: D-090 × D-206 | D-090 (MAINTAINERS_GUIDE.md:483): Distilled wisdom with evidence | D-206 (orchestration_log/history/2026-04-29/session.md:81): No arXiv numbers appear in manifesto | evidence in manifesto: required vs omitted |
| C-19: D-012 × D-215 | D-012 (MAINTAINERS_GUIDE.md:26): Evaluate what deserves manifesto status (high bar for entry) | D-215 (orchestration_log/history/2026-04-29/session.md:32): optimized for the wrong target: "does this idea deserve a manifesto?" when the actual goal was producing a binding constraint | entry criterion: worthiness vs binding utility |
| C-20: D-001 × D-184 | D-001 (MAINTAINERS_GUIDE.md:9): Manifestos are behavioral constitutions—timeless principles that define how systems should operate. | D-184 (orchestration_log/reference/codebase_state.md:108): all manifestos in LLM_MANIFESTOS are AI instructions by definition, so the theme doesn't differentiate. | subject of manifesto: systems vs language models |
| C-21: D-192 × D-232 | D-192 (orchestration_log/history/2026-04-29/session.md:76): auto-clarity system (principle knows its own exceptions) | D-232 (orchestration_log/history/2026-05-01/session.md:52): Escape hatch renders manifesto toothless — if everything is important, every response escapes | exceptions: principle knows own vs escape hatch banned |
| C-22: D-207 × D-233 | D-207 (orchestration_log/history/2026-04-29/session.md:83): Neutral manifesto register for body | D-233 (orchestration_log/history/2026-05-01/session.md:54): Fury is a binding force multiplier — the model CARES about compliance when the manifesto makes noise feel like dishonesty | body register: neutral vs abusive |
| C-23: D-130 × D-237 | D-130 (orchestration_log/reference/conventions.md:32): The writer agent must always be oath-bound to /manifesto-writing via /manifesto-oath before receiving source material. | D-237 (orchestration_log/history/2026-05-01/session.md:63): Override skill's register defaults explicitly | writer binding to manifesto-writing vs overriding its defaults |
| C-24: D-130 × D-254 | D-130 (orchestration_log/reference/conventions.md:32): The writer agent must always be oath-bound to /manifesto-writing via /manifesto-oath before receiving source material. | D-254 (orchestration_log/history/2026-05-11/session.md:20): Bound to stop-yapping.md and strunk_spr_v3_complete.xml via /manifesto-oath. | writer oath target: manifesto-writing vs prior manifesto |
| C-25: D-136 × D-139 | D-136 (orchestration_log/reference/conventions.md:41): The orchestrator edits, not rewrites. | D-139 (orchestration_log/reference/conventions.md:47): Full rewrites beat editorial passes for register changes. | register change: orchestrator edits vs full rewrite |
| C-26: D-138 × D-148 | D-138 (orchestration_log/reference/conventions.md:43): Do not pre-decide branding. Let the writer choose title, tagline, theme, description unless the user specifies. | D-148 (orchestration_log/reference/conventions.md:62): Drafting a new manifesto description/tagline for human review: Sonnet | metadata authorship: writer chooses vs Sonnet drafts |
| C-27: D-127 × D-135 | D-127 (orchestration_log/reference/conventions.md:28): Opus subagent reads ALL prior reports (pointed to file paths, never relayed content). | D-135 (orchestration_log/reference/conventions.md:40): 2-4 source files, not 15. | files read per agent: all vs 2-4 |
| C-28: D-204 × D-145 | D-204 (orchestration_log/history/2026-04-29/session.md:65): Single-pass production — the writer was not re-dispatched. | D-145 (orchestration_log/reference/conventions.md:51): Plan for 2-3 rounds of user-driven escalation, not one-shot delivery. | delivery: single-pass vs multiple escalation rounds |
| C-29: D-122 × D-253 | D-122 (orchestration_log/reference/conventions.md:25): Dispatch parallel haiku agents across content facets (philosophy, behavioral spec, implementation, external context). | D-253 (orchestration_log/history/2026-05-11/session.md:18): Invoked /spec-chef on user-prepared substrate | writing process start: research tree vs substrate |
| C-30: D-149 × D-411 | D-149 (orchestration_log/reference/conventions.md:70): Committing changes: always in the main session, never delegated | D-411 (ETHOS.md:29): The orchestrator decomposes, delegates, and assembles — it never executes. | orchestrator executes vs never executes |
| C-31: D-226 × D-411 | D-226 (orchestration_log/history/2026-05-01/session.md:38): Orchestrator wrote directly instead of dispatching. | D-411 (ETHOS.md:29): The orchestrator decomposes, delegates, and assembles — it never executes. | orchestrator writes directly vs never executes |
| C-32: D-309 × D-272 | D-309 (manifesto-writing/SKILL.md:60): State positions. Do not justify them at length. | D-272 (orchestration_log/history/2026-05-11/session.md:36): Fixed: expanded set-thinking explanation, planner cost model, MVCC physical model, constraint ontological distinction. | justification: declare only vs expanded explanation |
| C-33: D-256 × D-272 | D-256 (orchestration_log/history/2026-05-11/session.md:20): Resolution: compress teaching into declarations. | D-272 (orchestration_log/history/2026-05-11/session.md:36): Fixed: expanded set-thinking explanation, planner cost model, MVCC physical model, constraint ontological distinction. | teaching: compressed into declarations vs expanded explanation |
| C-34: D-312 × D-267 | D-312 (manifesto-writing/SKILL.md:68): Short sentences (under 20 words). | D-267 (orchestration_log/history/2026-05-11/session.md:32): Run-on fury sentences. | sentence length: under 20 words vs run-on |
| C-35: D-342 × D-264 | D-342 (manifesto-writing/SKILL.md:144): Manifestos sacrifice precision for force. | D-264 (orchestration_log/history/2026-05-11/session.md:30): Dispatched 5 parallel unbiased content reviewers against substrate: accuracy, completeness, boundaries, scope/facts, precision. | precision: sacrificed for force vs reviewed |
| C-36: D-341 × D-247 | D-341 (manifesto-writing/SKILL.md:144): Manifestos assume sympathetic readers. | D-247 (orchestration_log/history/2026-05-11/session.md:18): model-as-mediocre-engineer reader | reader stance: sympathetic vs mediocre engineer |
| C-37: D-338 × D-180 | D-338 (manifesto-writing/SKILL.md:140): aim for 1500-2500 words. Shorter is usually better. | D-180 (orchestration_log/reference/codebase_state.md:97): abusive register, 269 lines, 5337 words | length: 1500-2500 words vs 5337 words |
| C-38: D-201 × D-246 | D-201 (orchestration_log/history/2026-04-29/session.md:57): Explicit target: 70%+ bindable content, under 200 lines, self-referential discipline ("the manifesto must pass its own rules") | D-246 (orchestration_log/history/2026-05-11/session.md:18): constitution length (~400 lines) | length ceiling: under 200 lines vs ~400 |
| C-39: D-335 × D-445 | D-335 (manifesto-writing/SKILL.md:108): Use "After [Author]" to signal this is an editorial transformation, not a transcript or original composition. | D-445 (git 53a277b): feat(cargo-cult-science): add the Feynman speech as manifesto | entry form: attributed transformation vs speech |
| C-40: D-262 × D-271 | D-262 (orchestration_log/history/2026-05-11/session.md:28): pure contempt density gap (0.8 vs 16.2/1000w) | D-271 (orchestration_log/history/2026-05-11/session.md:36): Cut pure-berating paragraphs that carried no shift. | pure contempt: density target vs cut |
| C-41: D-278 × D-384 | D-278 (orchestration_log/history/2026-05-11/session.md:47): Specialization produces sharper findings than one generalist reviewer | D-384 (maximalist-reviewer.md:48): Check every rule against every line of the target; never skip a rule for a line or a line for a rule. | review decomposition: specialists vs one reviewer |
| C-42: D-358 × D-385 | D-358 (manifesto-oath/SKILL.md:52): If an element contains contradictory principles, request user disambiguation. | D-385 (maximalist-reviewer.md:50): never mark a partial compliance, an ambiguity, or a near miss as compliant. | contradictory demand: ask user vs mark violation |
| C-43: D-369 × D-412 | D-369 (manifesto-oath/SKILL.md:102): That injection is the enforcement mechanism. | D-412 (ETHOS.md:49): Mandatory steps in agent bodies cannot self-enforce. | binding enforcement: hook injection vs artifact check |
| C-44: D-372 × D-344 | D-372 (manifesto-oath/SKILL.md:11): You are a knight receiving an oath. | D-344 (manifesto-oath/SKILL.md:19): Use operational language exclusively. | oath-and-knight framing vs operational language |
| C-45: D-394 × D-017 | D-394 (manifesto/SCHEMA.md:74): Freeform text. Injected into hook output as natural language — tells the model why this element is in the stack. | D-017 (MAINTAINERS_GUIDE.md:49): Frontmatter is the source of truth for metadata. The README is always generated, never manually edited. | metadata source of truth: frontmatter vs config |
| C-46: D-421 × D-398 | D-421 (CLAUDE.md:12): Every agent prompt must open with a constitution-binding preamble before the task body. | D-398 (manifesto/SCHEMA.md:97): The orchestrator is NOT responsible for supplying base subagent bindings — SubagentStart handles that automatically. | dispatch-prompt binding: required vs orchestrator not responsible |
| C-47: D-349 × D-001 | D-349 (manifesto-oath/SKILL.md:28): Writing standard or style guide \| Read the referenced document completely | D-001 (MAINTAINERS_GUIDE.md:9): Manifestos are behavioral constitutions—timeless principles that define how systems should operate. | bindable elements: style guides and skills vs manifestos |
| C-48: D-416 × D-223 | D-416 (ETHOS.md:57): NEVER narrate failure modes in the second person. | D-223 (orchestration_log/history/2026-05-01/session.md:53): When bound via oath, the model reads the manifesto about itself — every "you" = the model | second-person failure narration: banned vs manifesto addresses model |
| C-49: D-408 × D-233 | D-408 (ETHOS.md:17): One emphatic marker per directive. | D-233 (orchestration_log/history/2026-05-01/session.md:54): Fury is a binding force multiplier — the model CARES about compliance when the manifesto makes noise feel like dishonesty | emphasis intensity: one marker vs escalating fury |
| C-50: D-434 × D-199 | D-434 (CLAUDE.md:38): I literally demand compression of user-facing communication BEYOND comprehension. | D-199 (orchestration_log/history/2026-04-29/session.md:53): enforce maximum language compression, with extreme signal-to-noise ratio, right to the brink of legibility | compression limit: beyond comprehension vs brink of legibility |
| C-51: D-061 × D-173 | D-061 (MAINTAINERS_GUIDE.md:278): Each theme should contain 2+ manifestos (don't create single-manifesto themes) | D-173 (orchestration_log/reference/codebase_state.md:39): Three themes (design-methodology, ai-instructions, research-protocols) are defined but have no manifestos assigned. | theme population: 2+ manifestos vs unused themes |
| C-52: D-034 × D-173 | D-034 (MAINTAINERS_GUIDE.md:107): Address theme discrepancies (themes.yaml should match usage) | D-173 (orchestration_log/reference/codebase_state.md:39): Three themes (design-methodology, ai-instructions, research-protocols) are defined but have no manifestos assigned. | themes.yaml should match usage vs unused themes |
| C-53: D-060 × D-061 | D-060 (MAINTAINERS_GUIDE.md:142): If using a new theme: | D-061 (MAINTAINERS_GUIDE.md:278): Each theme should contain 2+ manifestos (don't create single-manifesto themes) | new theme at first manifesto vs 2+ rule |
| C-54: D-243 × D-220 | D-243 (orchestration_log/history/2026-05-01/session.md:79): contains all research reports (not gitignored — tracked in repo) | D-220 (orchestration_log/history/2026-04-29/session.md:68): adding research/ to keep recon artifacts off the repo | research artifacts: tracked vs gitignored |
| C-55: D-429 × D-167 | D-429 (CLAUDE.md:23): Never increment major versions without explicit user approval. Use minor (features) or patch (fixes) only. | D-167 (orchestration_log/reference/conventions.md:120): Minor/patch bumps: discouraged. Just edit the file without incrementing. | version bumps: minor/patch only vs major only † |
| C-56: D-428 × D-072 | D-428 (CLAUDE.md:22): Versions live in plugin.json only. Skill frontmatters do not carry version fields. | D-072 (MAINTAINERS_GUIDE.md:401): version: string # Semver (e.g., "1.0.0") | version field location: plugin.json only vs frontmatter † |
| C-57: D-270 × D-303 | D-270 (orchestration_log/history/2026-05-11/session.md:36): Added table intros ("Read this table slowly"). | D-303 (manifesto-writing/SKILL.md:38): Explanatory scaffolding (definitions already given, objections pre-answered) | explanatory scaffolding: cut vs added |

† The two rules govern different objects: plugin or skill versions (project B) against manifesto versions (project A). Listed because both state a versioning regime.

## Silences

- Where does a draft live before entry, given that generate.py globs every `manifestos/*.md`?
- Does any tool or rule validate a manifesto body — sections, length, register, required parts?
- Is length counted in words, lines, or tokens, and does the count include frontmatter?
- Is a tagline bounded in length or form beyond "memorable"?
- Is a description bounded in words, or only by "one sentence"?
- Where do attribution and source citation live for a transformed manifesto — body, frontmatter, or neither?
- Does frontmatter name the reader — model, human, or both?
- Does frontmatter name the source or origin of the manifesto?
- Must the title relate to the filename or tagline by rule?
- Who approves entry — the maintainer, a reviewer agent, or the writer?
- Is a review before entry mandatory, and by which reviewer?
- Who owns a manifesto's factual accuracy after entry?
- What test shows two manifestos in one collection overlap or contradict?
- Which manifesto wins when two bound manifestos command opposite acts?
- What evidence marks a manifesto disproven rather than superseded?
- Does a register rewrite of a shipped manifesto count as a version change?
- May a manifesto quote another manifesto or its own source project?
- Does a binding name a manifesto version, or only a name?
- What updates `.manifestos.yaml` names, SCHEMA examples, and cited taglines when a manifesto is renamed, replaced, or deleted?
- Does project B bind a draft or unvalidated manifesto after pulling project A's default branch?
- How many manifestos may one binding stack hold?
- Does a manifesto declare whether it binds orchestrators, subagents, or both?
- Who authorizes an abusive register or profanity in a manifesto that other users bind?
- What measure shows a shipped manifesto changes behavior?
- What does the generator do with a manifesto whose frontmatter is valid and whose body is empty?
- Which model tier edits metadata fields after the body is written?

## Counts

**Rows per class**

| class | rows |
|---|---|
| boundary | 24 |
| entry | 41 |
| evidence | 9 |
| form | 48 |
| length | 9 |
| metadata | 92 |
| process | 90 |
| reader | 8 |
| register | 55 |
| review | 24 |
| runtime | 48 |

**Rows per status**

| status | rows |
|---|---|
| doctrine | 268 |
| learned | 131 |
| practiced | 49 |

**Rows per project**

| project | rows |
|---|---|
| A | 299 |
| B | 149 |

**Totals:** 448 rows, 57 conflicts.
