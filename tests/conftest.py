import os
import shutil

import pytest

CONFIG_PATH = os.path.abspath(os.path.join('.', 'examples'))


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

    def conf_mocker(config_name: str):
        mocker.patch('goto_project.conf_finder.CONFIG_PATH', CONFIG_PATH)
        mocker.patch('goto_project.conf_finder.CONFIG_NAME', config_name)

        filepath = os.path.join(CONFIG_PATH, config_name)
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        with open(filepath, 'w'):
            pass

    yield conf_mocker

    cleaner.clean()
