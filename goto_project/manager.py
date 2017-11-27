import typing
from collections import OrderedDict

from goto_project.config_tools import load_config


class Manager:

    default_params = OrderedDict(
        path=None,
        before=[],
        after=[],
    )

    def __init__(self):
        self.config = load_config()

    def list_projects(self) -> typing.Iterable[str]:
        return self.config.keys()

    def project_config(self, project_name: str) -> OrderedDict:
        default_conf = self.default_params.copy()
        default_conf.update(self.config[project_name] or {})
        return default_conf
