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


@pytest.mark.parametrize('project', [
    'awesome-project',
    'yet-another-project',
    'GreatestProjectOfAll',
    'emacs_with_blackjack_and_hookers',
    'VimWithBlackjackAndHookers',
])
@pytest.mark.parametrize('content, params', [(projects_example, (
    'path',
    'before',
    'after',
))])
def test_project_default_params(content, project, params, mock_config):
    mock_config('.goto-project.yaml', content)

    manager = Manager()
    project_config = manager.project_config(project)

    for param in params:
        assert param in project_config.keys()


@pytest.mark.parametrize('content, project, params', [
    ("""
VimWithBlackjackAndHookers:
  path: ~/my-projects/vim-with-blackjack_and_hookers
  clean_output_after: false
""", 'VimWithBlackjackAndHookers', {
        'path': '~/my-projects/vim-with-blackjack_and_hookers',
    }),
    ("""
yet-another-project:
  path: ~/my-projects/yet-another-project/src
""", 'yet-another-project', {
        'path': '~/my-projects/yet-another-project/src',
    }),
])
def test_project_configuration(content, project, params, mock_config):
    mock_config('.goto-project.yaml', content)

    manager = Manager()
    project_config = manager.project_config(project)

    for param, value in params.items():
        assert project_config[param] == value
