import subprocess

import pytest

from goto_project.manager import Manager


@pytest.mark.parametrize('config, project, call_args', [
    ("""
VimWithBlackjackAndHookers:
  path: ~/my-projects/vim-with-blackjack_and_hookers
  clear_on_exit: true
  instructions:
    - source ~/Envs/vim-with-blackjack_and_hookers
    - export $PATH=$HOME/.local/bin:$PATH
  command: vim
""",

     'VimWithBlackjackAndHookers',

     ['shell-command', '-c', """cd ~/my-projects/vim-with-blackjack_and_hookers
source ~/Envs/vim-with-blackjack_and_hookers
export $PATH=$HOME/.local/bin:$PATH
vim
shell-command
clear
echo "VimWithBlackjackAndHookers" closed."""]),

    ("""
yet-another-project:
  path: ~/my-projects/yet-another-project
  instructions:
    - source ~/Envs/yet-another-project
    - git status
""",

     'yet-another-project',

     ['shell-command', '-c', """cd ~/my-projects/yet-another-project
source ~/Envs/yet-another-project
git status
shell-command
echo "yet-another-project" closed."""]),
])
def test_goto_project(config, project, call_args, mock_config, mocker):
    mock_config('goto-project.yaml', config)
    mocker.patch(
        'goto_project.shell_tools.user_shell', return_value='shell-command')

    call = mocker.MagicMock()
    subprocess.call = call

    manager = Manager()
    manager.open_project(project)

    assert call.call_count == 1
    assert call.call_args[0][0] == call_args
