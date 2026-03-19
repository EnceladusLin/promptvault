"""CLI for PromptVault."""
import click
from rich.console import Console
from rich.table import Table

from promptvault.store import create_prompt, list_prompts, search_prompts, export_json

console = Console()


@click.group()
def main():
    """PromptVault - local-first prompt manager."""
    pass


@main.command()
@click.argument('title')
@click.option('--content', prompt=True)
@click.option('--tag', 'tags', multiple=True)
def add(title, content, tags):
    """Add a new prompt."""
    path = create_prompt(title, content, list(tags))
    console.print(f'[green]Saved prompt:[/green] {path}')


@main.command('list')
def list_cmd():
    """List prompts."""
    prompts = list_prompts()
    table = Table(title='PromptVault')
    table.add_column('Title')
    table.add_column('Tags')
    table.add_column('Updated')
    for p in prompts:
        table.add_row(p['title'], ', '.join(p.get('tags', [])), p.get('updated_at', ''))
    console.print(table)


@main.command()
@click.argument('query')
def search(query):
    """Search prompts."""
    results = search_prompts(query)
    for p in results:
        console.print(f"[bold]{p['title']}[/bold] [dim]{', '.join(p.get('tags', []))}[/dim]")
        console.print(p['content'][:200])
        console.print()


@main.command()
def export():
    """Export prompts as JSON."""
    console.print(export_json())


if __name__ == '__main__':
    main()
