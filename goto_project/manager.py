import subprocess
import typing

from goto_project.config_tools import load_config
from goto_project.shell_tools import ExpressionConstructor


class Manager:

    constructor = ExpressionConstructor

    def __init__(self):
        self.config = load_config()

    def list_projects(self) -> typing.Iterable[str]:
        return self.config.keys()

    def project_config(self, project_name: str) -> dict:
        return self.config[project_name] or {}

    def open_project(self, project_name: str):
        call_args = self.constructor.construct(
            project_name, self.project_config(project_name))
        subprocess.call(call_args)
