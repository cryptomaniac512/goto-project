import pytest

from goto_project.conf_finder import find_config
from goto_project.exceptions import ConfigNotFound

config_names = (
    '.goto-project.yaml',
    'projects.yml',
    '.my-projects',
)


@pytest.mark.parametrize('config_name', config_names)
def test_path_contains_config_name(config_name, mock_config):
    mock_config(config_name)
    assert config_name in find_config()


@pytest.mark.parametrize('config_name', config_names)
def test_returns_string(config_name, mock_config):
    mock_config(config_name)
    assert isinstance(find_config(), str)


@pytest.mark.parametrize('config_name', config_names)
def test_raises_exception_if_config_does_not_exist(config_name):
    with pytest.raises(ConfigNotFound):
        find_config()
