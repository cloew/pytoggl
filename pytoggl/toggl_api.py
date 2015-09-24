from .json_api import ApiHelper
from .model_api import WorkspacesApi

class TogglAPI:
    """ Represents the top level of the Toggl API """
    apiWrappers = {"workspaces":WorkspacesApi}
    
    def __init__(self, apiToken=None):
        """ Initialize the Toggl API """
        self.apiHelper = ApiHelper(apiToken)
        for key in self.apiWrappers:
            setattr(self, key, self.apiWrappers[key](self.apiHelper))