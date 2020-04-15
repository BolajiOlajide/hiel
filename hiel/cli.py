import typer

from hiel import __version__
from hiel.services.bootstrap import Bootstrap
from hiel.utils import ProjectTypes


app = typer.Typer()


def version_callback(value: bool):
    if value:
        typer.echo(f"Hiel Version: {__version__}")
        raise typer.Exit()


@app.command()
def create(
    name: str,
    type: ProjectTypes = typer.Option(None),
    # private: bool = typer.O
    version: bool = typer.Option(None, "--version", callback=version_callback),
) -> None:
    """Bootstrap a project and push to Github"""
    with typer.progressbar(range(100), label="Processing") as progress:
        if not name:
            name = typer.prompt("What is the name of your project?")
        typer.secho(f"Bootstrapping project: {name}", fg=typer.colors.MAGENTA)
        Bootstrap(name, progress, type).create()


def main():
    app()
