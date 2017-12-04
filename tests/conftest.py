import os
import shutil

import pytest

CONFIG_PATH = os.path.join('.', 'examples')


class FSCleaner:
    """File system cleaner.

    Remembers the specified directories for later removal.

    """

    def __init__(self):
        self._user_dirs = set()

    def __call__(self, *directories):
        """Used for remember specified directories."""
        self._user_dirs.update(directories)

    def clean(self):
        """Removes remembered directories recursively."""
        for used_dir in self._user_dirs:
            shutil.rmtree(used_dir, ignore_errors=True)


@pytest.fixture
def mock_config(mocker):
    """Fixture that creates an empty config file and remove it then."""
    cleaner = FSCleaner()
    cleaner(CONFIG_PATH)

    def conf_mocker(name: str, content: str=''):
        mocker.patch('goto_project.config_tools.CONFIG_PATH', CONFIG_PATH)
        mocker.patch('goto_project.config_tools.CONFIG_NAME', name)

        filepath = os.path.join(CONFIG_PATH, name)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w') as f:
            f.write(content)

    yield conf_mocker

    cleaner.clean()


@pytest.fixture
def config_path():
    return os.path.abspath(CONFIG_PATH)


@pytest.fixture
def mock_shell(mocker):
    mocker.patch(
        'goto_project.shell_tools.user_shell', return_value='shell-command')
