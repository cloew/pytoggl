from request_helper import RequestHelper
from workspaces_api import WorkspacesAPI

class TogglAPI:
    """ Represents the top level of the Toggl API """
    
    def __init__(self, apiToken=None):
        """ Initialize the Toggl API """
        self.requestHelper = RequestHelper(apiToken)
        self.workspaces = WorkspacesAPI(self.requestHelper)