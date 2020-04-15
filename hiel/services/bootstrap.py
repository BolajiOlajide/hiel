import os

import typer

from hiel.services.github import Github
from hiel.utils import (
    PYTHON_EDITOR_CONFIG,
    JAVASCRIPT_EDITOR_CONFIG,
    ProjectTypes,
    PYTHON_GITIGNORE,
    JAVASCRIPT_GITIGNORE,
)


class Bootstrap:
    def __init__(self, project_name: str, progress, project_type: ProjectTypes):
        self.cwd = os.getcwd()
        self.project_name = project_name
        self.project_type = project_type
        self.progress = progress
        self.progress.update(8)  # total = 10
        self.project_location = None
        self.repository = None

    def create(self):
        self.progress.update(5)  # total = 15
        self.create_project_directory()
        self.repository = Github(self.project_name).create_repository()
        if self.project_type:
            self.create_editorconfig()
            self.create_gitignore()
            self.initialize_project()
        self.initialize_git()
        self.push_to_github()
        os.chdir(self.project_location)

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
        message = f"Creating a `README.md` for {self.project_name}."
        typer.secho(message, fg=typer.colors.GREEN, bold=True)

        readme_location = f"{self.project_location}/README.md"
        with open(readme_location, "w") as readme:
            readme.write(f"# {self.project_name.upper()}")
            readme.write("")

    def create_editorconfig(self):
        message = f"Creating a `.editorconfig` for {self.project_name}."
        typer.secho(message, fg=typer.colors.GREEN, bold=True)

        editorconfig_location = f"{self.project_location}/.editorconfig"
        with open(editorconfig_location, "w") as editorconfig:
            if self.project_type == ProjectTypes.js:
                editorconfig.write(JAVASCRIPT_EDITOR_CONFIG)
            elif self.project_type == ProjectTypes.py:
                editorconfig.write(PYTHON_EDITOR_CONFIG)
            editorconfig.write("")

    def create_gitignore(self):
        message = f"Creating a `.gitignore` for {self.project_name}."
        typer.secho(message, fg=typer.colors.GREEN, bold=True)

        gitignore_location = f"{self.project_location}/.gitignore"
        with open(gitignore_location, "w") as gitignore:
            if self.project_type == ProjectTypes.js:
                gitignore.write(JAVASCRIPT_GITIGNORE)
            elif self.project_type == ProjectTypes.py:
                gitignore.write(PYTHON_GITIGNORE)
            gitignore.write("")

    def initialize_git(self):
        message = f"Initializing `git` for {self.project_name}."
        typer.secho(message, fg=typer.colors.GREEN, bold=True)

        os.chdir(self.project_location)
        os.system("git init")
        os.system(f"git remote add origin {self.repository}")

    def push_to_github(self):
        message = f"Committing and pushing to `git` for the first time."
        typer.secho(message, fg=typer.colors.GREEN, bold=True)

        os.system("git add .")
        os.system("git commit -m \"initial commit ✨\"")
        os.system("git push origin master")

    def initialize_project(self):
        message = f"Initializing project. 😍"
        typer.secho(message, fg=typer.colors.GREEN, bold=True)
        if self.project_type == ProjectTypes.js:
            self._initialize_js_project()
        elif self.project_type == ProjectTypes.py:
            self._initialize_py_project()

    def _initialize_js_project(self):
        os.chdir(self.project_location)
        os.system("yarn init -y")

    def _initialize_py_project(self):
        os.chdir(self.project_location)
        os.system("pipenv shell --python=python3")
