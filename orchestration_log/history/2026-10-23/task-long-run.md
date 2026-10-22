# Task: long-run, received 2026-10-23

Owner's brief, received in conversation at the stamp of the events line; reference file `/Users/ryzhakar/Downloads/claude-cli-custom-system-prompt-reference.md` (verified on `claude` 2.1.308 -p, Linux; the local CLI reads 2.1.308).

## Purpose

The harness takes control of the instructional foundation of a session without anyone choosing it. The owner wants that foundation managed in a clear, simple way, and wants the system prompt built mainly from manifestos.

## Parts

1. **Launch compiler.** A plugin-shipped Python tool run with `uvx`. It compiles the flags, environment variables, and the like for the harness launcher, Claude Code first. Its setup strips every harness-injected instruction except the registries and explanations of tools, skills, and agents. Its parameters are clear and well named. It takes the compiled system prompt as a bare argument, so the prompt can be piped into it.
2. **Prompt compiler.** It compiles a system prompt from a manifesto config. It resolves full manifestos by name from the plugin's manifesto registry and by local path relative to the current folder, and resolves skills from the user's skill cache at the latest version that resolves. Beside the manifesto stack it carries a plaintext preamble, a minimal shipped default addressing harness kinks such as the source of hook injections, and a file of commitments. Tags structure everything, and the tags imitate an agent's raw output.
3. **`/compile-commitments`.** A skill or command with which a session writes the commitments file, under a fixed name, in tags that closely resemble its own raw output as an agent.

## Ergonomics

Set the manifesto config and precompile the commitments once; then:
`<prompt compiler> *args **kwargs | <launch compiler> *args **kwargs | <launcher of choice, custom ones included>`

## Known kinks from the reference (to verify locally before relying on them)

- The identity line survives every flag; `--system-prompt` with `--append-system-prompt` changes it.
- Skills and agents reach the model only with the `Skill` and `Agent` tools in the set; `--tools "default,X"` breaks; explicit lists are reliable.
- No environment variable carries prompt text.
- CLAUDE.md, the user email, and the attribution reminder sit in `messages[0]`; `CLAUDE_CODE_DISABLE_CLAUDE_MDS=1` removes CLAUDE.md; `CLAUDE_CODE_ATTRIBUTION_HEADER=0` removes the billing block.
- Interactive mode, plugins, hooks, and `--bare` were not verified by the reference.
