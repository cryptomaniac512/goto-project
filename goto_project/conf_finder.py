import os.path

from goto_project.exceptions import ConfigNotFound

CONFIG_NAME = '.goto-project.yaml'
CONFIG_PATH = '~'


def find_config() -> str:
    conf_path = os.path.abspath(os.path.join(CONFIG_PATH, CONFIG_NAME))
    if not os.path.isfile(conf_path):
        raise ConfigNotFound(f'"{conf_path}" can not be found.')
    return conf_path
