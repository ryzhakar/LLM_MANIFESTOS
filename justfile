# Generate README from manifesto frontmatter
readme:
    uv run --with pyyaml --with python-frontmatter --with pydantic --with jinja2 --with rich generate.py
