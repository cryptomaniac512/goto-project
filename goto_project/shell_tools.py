import os
import typing


def user_shell():
    return os.environ['SHELL']


class ExpressionConstructor:
    """Class for constructing shell expression by project configuration."""

    def __init__(self, project_name: str, project_conf: dict):
        self.project_name = project_name
        self.project_conf = project_conf

    def expand_path(self) -> str:
        return f'cd {self.project_conf["path"]}'

    def expand_instructions(self) -> str:
        return '\n'.join(self.project_conf['instructions'])

    def expand_command(self) -> str:
        return self.project_conf['command']

    def expand_clear_on_exit(self) -> str:
        return 'clear'

    def on_close_message(self) -> str:
        return f'echo "{self.project_name}" closed.'

    def construct_expression_part(self):
        expression = []

        for key in ('path', 'instructions', 'command'):
            if key not in self.project_conf:
                continue
            method = getattr(self, f'expand_{key}')
            expression.append(method())

        expression.append(user_shell())

        if self.project_conf.get('clear_on_exit') is True:
            expression.append(self.expand_clear_on_exit())

        expression.append(self.on_close_message())

        return '\n'.join(expression)

    def __call__(self) -> typing.List[str]:
        return [user_shell(), '-c', self.construct_expression_part()]

    @classmethod
    def construct(
            cls, project_name: str, project_conf: dict) -> typing.List[str]:
        instance = cls(project_name, project_conf)
        return instance()
