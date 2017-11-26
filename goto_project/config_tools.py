import os.path
from collections import OrderedDict

import yaml

from goto_project.exceptions import ConfigNotFound

CONFIG_NAME = '.goto-project.yaml'
CONFIG_PATH = '~'


def find_config() -> str:
    conf_path = os.path.abspath(os.path.join(CONFIG_PATH, CONFIG_NAME))
    if not os.path.isfile(conf_path):
        raise ConfigNotFound(f'"{conf_path}" can not be found.')
    return conf_path


def load_config() -> OrderedDict:
    with open(find_config(), 'r') as config:
        return yaml.load(config, Loader=OrderedDictYAMLLoader)


class OrderedDictYAMLLoader(yaml.Loader):
    """YAML loader that loads mappings into ordered dictionaries.

    Based on https://gist.github.com/enaeseth/844388

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for tag in ('tag:yaml.org,2002:map', 'tag:yaml.org,2002:omap'):
            self.add_constructor(tag, self.__class__.construct_yaml_map)

    def construct_yaml_map(self, node):
        data = OrderedDict()
        yield data
        value = self.construct_mapping(node)
        data.update(value)

    def construct_mapping(self, node, deep=False):
        self.flatten_mapping(node)

        mapping = OrderedDict()
        for key_node, value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            value = self.construct_object(value_node, deep=deep)
            mapping[key] = value

        return mapping
