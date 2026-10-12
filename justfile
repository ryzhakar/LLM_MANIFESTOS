# Generate README from manifesto frontmatter
readme:
    uv run --with pyyaml --with python-frontmatter --with pydantic --with jinja2 --with rich generate.py

# Put the digest-eval launcher on the PATH as `digest-eval` (symlink into ~/.local/bin)
install-digest-eval:
    mkdir -p ~/.local/bin
    ln -sf "{{justfile_directory()}}/tools/digest-eval/digest-eval" ~/.local/bin/digest-eval

# Run the digest-eval tests (offline, on the pilot data)
test-digest-eval:
    python3 -I tools/digest-eval/tests/test_digest_eval.py < /dev/null
