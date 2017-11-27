from goto_project.manager import Manager


class GotoProject:

    def manager(self):
        return Manager()

    def list(self):
        return '\n'.join(self.manager().list_projects())

    def open(self, project_name: str):
        self.manager().open_project(project_name)
