import pytest

from goto_project.manager import Manager


project_list_example = """
awesome-project:
yet-another-project:
GreatestProjectOfAll:
emacs_with_blackjack_and_hookers:
VimWithBlackjackAndHookers:
"""

project_example = """
VimWithBlackjackAndHookers:
  path: ~/my-projects/vim-with-blackjack_and_hookers
  clean_output_after: false
"""


@pytest.mark.parametrize('content, expected_projects', [
    (project_list_example, (
        'awesome-project',
        'yet-another-project',
        'GreatestProjectOfAll',
        'emacs_with_blackjack_and_hookers',
        'VimWithBlackjackAndHookers',
    ))])
def test_project_listing(content, expected_projects, mock_config):
    mock_config('.goto-project.yaml', content)

    manager = Manager()
    projects = manager.list_projects()

    assert tuple(projects) == expected_projects


@pytest.mark.parametrize('content, project, params', [
    ("""
VimWithBlackjackAndHookers:
  path: ~/my-projects/vim-with-blackjack_and_hookers
  clear_on_exit: true
""", 'VimWithBlackjackAndHookers', {
        'path': '~/my-projects/vim-with-blackjack_and_hookers',
        'clear_on_exit': True,
    }),

    ("""
yet-another-project:
  path: ~/my-projects/yet-another-project/src
""", 'yet-another-project', {
        'path': '~/my-projects/yet-another-project/src',
    }),

    ("""
GreatestProjectOfAll:
  path: ~/my-projects/yet-another-project/src
  instructions:
    - source ~/Envs/GreatestProjectOfAll
    - find ./ -type f -name "*.pyc" -delete
  command: vim
""", 'GreatestProjectOfAll', {
        'path': '~/my-projects/yet-another-project/src',
        'instructions': [
            'source ~/Envs/GreatestProjectOfAll',
            'find ./ -type f -name "*.pyc" -delete',
        ],
        'command': 'vim',
    }),
])
def test_project_configuration(content, project, params, mock_config):
    mock_config('.goto-project.yaml', content)

    manager = Manager()

    assert manager.project_config(project) == params


@pytest.mark.parametrize('project, config, call_args', [
    ('VimWithBlackjackAndHookers',

     """
VimWithBlackjackAndHookers:
  path: ~/my-projects/vim-with-blackjack_and_hookers
  clear_on_exit: true
  instructions:
    - source ~/Envs/vim-with-blackjack_and_hookers
    - export $PATH=$HOME/.local/bin:$PATH
  command: vim
""",

     ['shell-command', '-c', """cd ~/my-projects/vim-with-blackjack_and_hookers
source ~/Envs/vim-with-blackjack_and_hookers
export $PATH=$HOME/.local/bin:$PATH
vim
shell-command
clear
echo "VimWithBlackjackAndHookers" closed."""]),

    ('yet-another-project',

     """
yet-another-project:
  path: ~/my-projects/yet-another-project
  instructions:
    - source ~/Envs/yet-another-project
    - git status
""",

     ['shell-command', '-c', """cd ~/my-projects/yet-another-project
source ~/Envs/yet-another-project
git status
shell-command
echo "yet-another-project" closed."""]),
])
@pytest.mark.usefixtures('mock_shell')
def test_open_project(project, config, call_args, mock_config, mocker):
    mock_config('goto-project.yaml', config)

    call = mocker.MagicMock()
    with mocker.patch('subprocess.call', call):
        manager = Manager()
        manager.open_project(project)

        assert call.call_count == 1
        assert call.call_args[0][0] == call_args
