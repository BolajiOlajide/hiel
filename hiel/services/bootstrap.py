import os

import typer

from hiel.utils import PYTHON_EDITOR_CONFIG, JAVASCRIPT_EDITOR_CONFIG, ProjectTypes


class Bootstrap:
    def __init__(self, project_name: str, progress, project_type: ProjectTypes):
        self.project_name = project_name
        self.project_type = project_type
        self.progress = progress
        self.progress.update(8)  # total = 10
        self.project_location = None

    def create(self):
        self.progress.update(5)  # total = 15
        self.create_project_directory()
        if self.project_type:
            self.create_editorconfig()

    def create_project_directory(self):
        self.project_location = os.path.join(os.getcwd(), self.project_name)
        if os.path.exists(self.project_location):
            message = f"The directory {self.project_name} already exists. Try again with another project name."
            typer.secho(message, fg=typer.colors.RED, bold=True)
            raise typer.Exit()
        typer.secho("\nCreating project directory.", fg=typer.colors.GREEN, bold=True)
        os.mkdir(self.project_location)
        self.create_readme()

    def create_readme(self):
        readme_location = f"{self.project_location}/README.md"
        with open(readme_location, 'w') as readme:
            readme.write(f"# {self.project_name.upper()}")
            readme.write("")

    def create_editorconfig(self):
        editorconfig_location = f"{self.project_location}/.editorconfig"
        with open(editorconfig_location, 'w') as editorconfig:
            if self.project_type == ProjectTypes.js:
                editorconfig.write(JAVASCRIPT_EDITOR_CONFIG)
            elif self.project_type == ProjectTypes.py:
                editorconfig.write(PYTHON_EDITOR_CONFIG)
            editorconfig.write("")
