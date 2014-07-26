from pytoggl.api.projects_api import ProjectsAPI
from pytoggl.api.timer_api import TimerAPI
from pytoggl.api.workspaces_api import WorkspacesAPI

from request_helper import RequestHelper

class TogglAPI:
    """ Represents the top level of the Toggl API """
    apiWrappers = {"workspaces":WorkspacesAPI,
                   "projects":ProjectsAPI,
                   "timer":TimerAPI}
    
    def __init__(self, apiToken=None):
        """ Initialize the Toggl API """
        self.requestHelper = RequestHelper(apiToken)
        for key in self.apiWrappers:
            setattr(self, key, self.apiWrappers[key](self.requestHelper))