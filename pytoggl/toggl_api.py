from projects_api import ProjectsAPI
from workspaces_api import WorkspacesAPI

from request_helper import RequestHelper

class TogglAPI:
    """ Represents the top level of the Toggl API """
    
    def __init__(self, apiToken=None):
        """ Initialize the Toggl API """
        self.requestHelper = RequestHelper(apiToken)
        self.projects = ProjectsAPI(self.requestHelper)
        self.workspaces = WorkspacesAPI(self.requestHelper)