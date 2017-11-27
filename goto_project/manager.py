import typing

from goto_project.config_tools import load_config


class Manager:

    def __init__(self):
        self.config = load_config()

    def list_projects(self) -> typing.Iterable[str]:
        return self.config.keys()

    def project_config(self, project_name: str) -> dict:
        return self.config[project_name] or {}
