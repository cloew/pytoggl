from enum import Enum

class Routes(Enum):
    """ Represents the various routes associated with the Toggl API """
    Workspaces = "workspaces"
    Workspace = "workspaces/{id}"
    
    def build(self, **kwargs):
        """ Build the Url with the given arguments """
        return self.value.format(**kwargs)