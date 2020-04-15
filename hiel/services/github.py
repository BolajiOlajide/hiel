import os
from pathlib import Path
import json

import typer
import requests


class Github:
    def __init__(self, project_name: str):
        self.access_token = None
        self.project_name = project_name

    def create_repository(self):
        self.validate_access_token()
        repository_details = self._create_repository()
        typer.secho("Successfully created the repository on Github", fg=typer.colors.GREEN, bold=True)
        return repository_details

    def _create_repository(self):
        try:
            url = "https://api.github.com/user/repos"
            data = {"name": self.project_name, "private": False}
            headers = {
                "Authorization": f"token {self.access_token}",
                "Content-Type": "application/json",
            }
            _response = requests.post(url, data=json.dumps(data), headers=headers)
            response = _response.json()
            if _response.ok:
                return response["ssh_url"]
            error_message = f"""{response["message"]}
{response["errors"][0]["message"]}
"""
        except Exception as exception:
            error_message = exception.args[0]

        typer.secho(error_message, fg=typer.colors.RED, bold=True)
        raise typer.Abort()

    def validate_access_token(self):
        home_dir = str(Path.home())
        config_path = f"{home_dir}/.hiel"
        does_config_exist = os.path.exists(config_path)
        access_token = None

        if does_config_exist:
            with open(config_path, "r") as config_file:
                access_token = config_file.readline()

        if (not does_config_exist) or (not access_token):
            message = f"Github Access token not found. Please create an `access_token` -> https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line"
            typer.secho(message, fg=typer.colors.RED, bold=True)
            access_token = typer.prompt("Enter an access token.")
            with open(config_path, "w") as config_file:
                typer.secho("Saving the access_token in $HOME/.hiel", fg=typer.colors.GREEN, bold=True)
                config_file.write(access_token)

        self.access_token = access_token
