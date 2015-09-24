from .api import WorkspacesApi
from .requests import ApiHelper

class TogglConnection:
    """ Represents a connection to the Toggl API """
    apiWrappers = {"workspaces":WorkspacesApi}
    
    def __init__(self, apiToken=None):
        """ Initialize the Toggl API """
        self.apiHelper = ApiHelper(apiToken)
        for key, wrapper in self.apiWrappers.items():
            setattr(self, key, wrapper(self))