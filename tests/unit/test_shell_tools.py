import pytest

from goto_project.shell_tools import ExpressionConstructor, user_shell


def test_user_shell():
    """There is no good way to mock user shell, but I need know that functions
    works."""
    assert isinstance(user_shell(), str)


@pytest.mark.parametrize('name, conf, expected', [
    ('VimWithBlackjackAndHookers', dict(
        path='~/my-projects/vim-with-blackjack_and_hookers',
        clear_on_exit=True,
        instructions=[
            'source ~/Envs/vim-with-blackjack_and_hookers',
            'export $PATH=$HOME/.local/bin:$PATH',
        ],
        command='vim',
    ), ['shell-command', '-c', """cd ~/my-projects/vim-with-blackjack_and_hookers
source ~/Envs/vim-with-blackjack_and_hookers
export $PATH=$HOME/.local/bin:$PATH
vim
shell-command
clear
echo "VimWithBlackjackAndHookers" closed."""]),

    ('yet-another-project', dict(
        path='~/my-projects/yet-another-project',
        instructions=[
            'source ~/Envs/yet-another-project',
            'git status',
        ],
    ), ['shell-command', '-c', """cd ~/my-projects/yet-another-project
source ~/Envs/yet-another-project
git status
shell-command
echo "yet-another-project" closed."""]),

    ('GreatestProjectOfAll', dict(
        path='~/my-projects/GreatestProjectOfAll',
        clear_on_exit=True,
        instructions=[
            'source ~/Envs/GreatestProjectOfAll',
            'find ./ -type f -name "*.pyc" -delete',
            'git status',
        ],
    ), ['shell-command', '-c', """cd ~/my-projects/GreatestProjectOfAll
source ~/Envs/GreatestProjectOfAll
find ./ -type f -name "*.pyc" -delete
git status
shell-command
clear
echo "GreatestProjectOfAll" closed."""]),

    ('awesome-project', dict(
        path='~/my-projects/awesome-project',
    ), ['shell-command', '-c', """cd ~/my-projects/awesome-project
shell-command
echo "awesome-project" closed."""]),
])
def test_construct_expression(name, conf, expected, mocker):
    mocker.patch(
        'goto_project.shell_tools.user_shell', return_value='shell-command')

    got = ExpressionConstructor.construct(name, conf)

    assert got == expected
