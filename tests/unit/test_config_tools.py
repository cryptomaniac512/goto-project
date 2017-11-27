import os.path

import pytest

from goto_project.config_tools import find_config, load_config
from goto_project.exceptions import ConfigNotFound

config_names = (
    '.goto-project.yaml',
    'projects.yml',
    '.my-projects',
)


@pytest.mark.parametrize('config_name', config_names)
def test_find_config_includes_config_name(config_name, mock_config):
    mock_config(config_name)

    assert config_name in find_config()


@pytest.mark.parametrize('config_name', config_names)
def test_find_config_returns_string(config_name, mock_config):
    mock_config(config_name)

    assert isinstance(find_config(), str)


@pytest.mark.parametrize('config_name', config_names)
def test_find_config_returns_abs_path(config_name, mock_config, config_path):
    mock_config(config_name)

    assert find_config() == os.path.join(config_path, config_name)


@pytest.mark.parametrize('config_name', config_names)
def test_find_config_raises_exception_if_config_does_not_exist(config_name):
    with pytest.raises(ConfigNotFound):
        find_config()


@pytest.mark.parametrize('content, expected', (
    ("""
one: blah
two: blah
three: blah
    """, {'one': 'blah', 'two': 'blah', 'three': 'blah'}),
    ("""
9: blah
7: blah
5: blah
    """, {9: 'blah', 7: 'blah', 5: 'blah'}),
))
def test_load_config_returns_ordered_dict(content, expected, mock_config):
    mock_config('.goto-project.yaml', content)

    assert load_config() == expected
