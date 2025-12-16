# {{ project.title }}

{{ project.description }}

## Quick Reference

| Manifesto | Theme | Version |
|-----------|-------|---------|
{% for m in manifestos | sort(attribute='title') -%}
| [{{ m.title }}]({{ m.path }}) | {{ themes[m.theme].name if m.theme in themes else m.theme }} | `{{ m.version }}` |
{% endfor %}

---

{% set manifesto_themes = manifestos | map(attribute='theme') | unique | list %}
{% for theme_key in manifesto_themes | sort %}
{% set theme = themes[theme_key] if theme_key in themes else {'icon': '📄', 'name': theme_key, 'description': ''} %}
## {{ theme.icon }} {{ theme.name }}

{% if theme.description %}{{ theme.description }}{% endif %}

{% for m in manifestos | selectattr('theme', 'equalto', theme_key) | sort(attribute='title') %}
### [{{ m.title }}]({{ m.path }}) `{{ m.version }}`
*"{{ m.tagline }}"*

{{ m.description }}

---

{% endfor %}
{% endfor %}

## Maintenance

> *Manifestos are precious artifacts, not documentation.*

This README is generated from manifesto frontmatter. **For complete maintainer workflows, see [MAINTAINERS_GUIDE.md](MAINTAINERS_GUIDE.md).**

**Quick workflow:**

1. Edit manifesto files in `manifestos/`
2. Run `just readme`
3. Commit changes

**Adding a new manifesto:**
- Create `manifestos/Manifesto, <name>.md` with required frontmatter (title, tagline, version, theme, description)
- If using a new theme, add it to `themes.yaml` first
- See [MAINTAINERS_GUIDE.md](MAINTAINERS_GUIDE.md) for philosophy and detailed workflows

**Schema validation:** Powered by Pydantic. Invalid frontmatter will be caught with detailed error messages.
