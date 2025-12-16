#!/usr/bin/env python3
"""Generate README.md from manifesto frontmatter with strict validation."""

import re
import sys
from pathlib import Path
from typing import Literal

import frontmatter
import yaml
from jinja2 import Template
from pydantic import BaseModel, field_validator, ValidationError
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()


class ManifestoMetadata(BaseModel):
    """Strict schema for manifesto frontmatter."""

    title: str
    tagline: str
    version: str
    theme: str
    description: str

    @field_validator('version')
    @classmethod
    def validate_semver(cls, v: str) -> str:
        if not re.match(r'^\d+\.\d+\.\d+$', v):
            raise ValueError(f'Version must be semver (e.g., 1.0.0), got: {v}')
        return v


def main():
    # Load configuration
    config = yaml.safe_load(Path('config.yaml').read_text())
    themes = yaml.safe_load(Path('themes.yaml').read_text())

    # Scan manifestos (manifestos/ directory only)
    manifestos = []
    errors = []

    manifesto_dir = Path('manifestos')
    if not manifesto_dir.exists():
        console.print("[red]Error: manifestos/ directory not found[/red]")
        sys.exit(1)

    for md_file in sorted(manifesto_dir.glob('Manifesto*.md')):
        try:
            post = frontmatter.load(md_file)

            # Validate frontmatter against schema
            metadata = ManifestoMetadata(**post.metadata)

            manifestos.append({
                'path': str(md_file),
                **metadata.model_dump()
            })

        except ValidationError as e:
            errors.append((md_file, 'Schema Validation', e))
        except KeyError as e:
            errors.append((md_file, 'Missing Frontmatter', f'Missing key: {e}'))
        except Exception as e:
            errors.append((md_file, 'Parse Error', str(e)))

    # Display errors (graceful degradation)
    if errors:
        console.print()
        for path, error_type, error in errors:
            console.print(Panel(
                f"[red]{error}[/red]",
                title=f"❌ {error_type}: {path.name}",
                border_style="red"
            ))

        console.print(f"\n[yellow]⚠  Skipped {len(errors)} file(s) due to errors[/yellow]")
        console.print(f"[dim]Fix frontmatter and re-run `just readme`[/dim]\n")

    # Check theme discrepancies
    frontmatter_themes = {m['theme'] for m in manifestos}
    template_themes = set(themes.keys())
    missing_themes = frontmatter_themes - template_themes

    if missing_themes:
        console.print()
        console.print(Panel(
            f"[yellow]Themes in frontmatter but not in themes.yaml:[/yellow]\n"
            + "\n".join(f"  • {t}" for t in sorted(missing_themes))
            + "\n\n[dim]Add these to themes.yaml or they'll render without icons/names[/dim]",
            title="⚠️  Theme Discrepancy",
            border_style="yellow"
        ))

    # Exit if no manifestos
    if not manifestos:
        console.print("[red]No valid manifestos found. Exiting.[/red]")
        sys.exit(1)

    # Generate README
    data = {
        'project': config,
        'manifestos': manifestos,
        'themes': themes
    }

    template = Template(Path('README.template.md').read_text())
    readme_content = template.render(data)
    Path('README.md').write_text(readme_content)

    # Success summary
    console.print(f"\n[green]✓ Generated README.md from {len(manifestos)} manifesto(s)[/green]")

    # Show theme breakdown
    theme_counts = {}
    for m in manifestos:
        theme_counts[m['theme']] = theme_counts.get(m['theme'], 0) + 1

    table = Table(show_header=False, box=None, padding=(0, 2))
    for theme, count in sorted(theme_counts.items()):
        theme_name = themes.get(theme, {}).get('name', theme)
        icon = themes.get(theme, {}).get('icon', '📄')
        table.add_row(f"{icon} {theme_name}", f"[dim]{count} manifesto(s)[/dim]")

    console.print(table)
    console.print()


if __name__ == '__main__':
    main()
