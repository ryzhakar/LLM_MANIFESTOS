# {{ project.title }}

{{ project.description }}

## Quick Reference

| Manifesto | Theme | Version | Register | Reader |
|-----------|-------|---------|----------|--------|
{% for m in manifestos | sort(attribute='title') -%}
| [{{ m.title }}]({{ m.path }}){% if m.kind == 'canon' %} `canon`{% endif %} | {{ themes[m.theme].name if m.theme in themes else m.theme }} | `{{ m.version }}` | {{ m.register or '' }} | {{ m.reader or '' }} |
{% endfor %}
---
{%- for theme_key in manifestos | map(attribute='theme') | unique | list | sort %}
{%- set theme = themes[theme_key] if theme_key in themes else {'icon': '📄', 'name': theme_key, 'description': ''} %}

## {{ theme.icon }} {{ theme.name }}
{% if theme.description -%}
{{ theme.description }}
{% endif -%}
{%- for m in manifestos | selectattr('theme', 'equalto', theme_key) | sort(attribute='title') %}

### [{{ m.title }}]({{ m.path }}){% if m.kind == 'canon' %} `canon`{% endif %} `{{ m.version }}`{% if m.register %} · {{ m.register }}{% endif %}{% if m.reader %} · {{ m.reader }}{% endif %}
*"{{ m.tagline }}"*

{{ m.description }}
{%- if not loop.last %}

---
{%- endif -%}
{%- endfor -%}
{%- endfor %}

## Maintenance

> *Manifestos are precious artifacts, not documentation.*

This README is generated from manifesto frontmatter. **For complete maintainer workflows, see [MAINTAINERS_GUIDE.md](MAINTAINERS_GUIDE.md).**

**Quick workflow:**

1. Edit manifesto files in `manifestos/`
2. Run `just readme`
3. Commit changes

**Adding a new manifesto:** pass the entry gate in [MAINTAINERS_GUIDE.md](MAINTAINERS_GUIDE.md) (Workflows, The Entry Gate).

**Schema validation:** Powered by Pydantic. Invalid frontmatter will be caught with detailed error messages.
