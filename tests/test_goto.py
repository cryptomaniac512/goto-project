import subprocess

import pytest

from goto_project.goto import GotoProject


projects_example = """
awesome-project:
yet-another-project:
GreatestProjectOfAll:
emacs_with_blackjack_and_hookers:
VimWithBlackjackAndHookers:
"""


@pytest.mark.parametrize('content, project_list', [(
    projects_example,
    """awesome-project
yet-another-project
GreatestProjectOfAll
emacs_with_blackjack_and_hookers
VimWithBlackjackAndHookers""",
)])
def test_listing(content, project_list, mock_config):
    mock_config('.goto-project.yaml', content)

    goto = GotoProject()
    assert goto.list() == project_list


@pytest.mark.parametrize('project', [
    'awesome-project',
    'yet-another-project',
    'GreatestProjectOfAll',
    'emacs_with_blackjack_and_hookers',
    'VimWithBlackjackAndHookers',
])
def test_open(project, mocker, mock_config):
    mock_config('.goto-project.yaml', projects_example)

    open_project = mocker.MagicMock()
    with mocker.patch('goto_project.goto.Manager.open_project', open_project):
        goto = GotoProject()
        goto.open(project)

        assert open_project.call_count == 1
        assert open_project.call_args[0][0] == project


def test_cli():
    proc = subprocess.run(
        ['./goto_project/gt', '-h'], stdout=subprocess.PIPE)

    help_text = 'Project to open. List all available project if empty,'
    assert help_text in str(proc.stdout)
