from pytoggl.api.projects_api import ProjectsAPI
from pytoggl.api.timer_api import TimerAPI
from pytoggl.api.workspaces_api import WorkspacesAPI

from pytoggl.api.api_helper import ApiHelper

class TogglAPI:
    """ Represents the top level of the Toggl API """
    apiWrappers = {"workspaces":WorkspacesAPI,
                   "projects":ProjectsAPI,
                   "timer":TimerAPI}
    
    def __init__(self, apiToken=None):
        """ Initialize the Toggl API """
        self.apiHelper = ApiHelper(apiToken)
        for key in self.apiWrappers:
            setattr(self, key, self.apiWrappers[key](self.apiHelper))