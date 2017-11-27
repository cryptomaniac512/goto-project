import pytest

from goto_project.manager import Manager


projects_example = """
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


@pytest.mark.parametrize('content, expected_projects', [(projects_example, (
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
