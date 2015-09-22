from .api import ApiHelper, ProjectsAPI, TimerAPI, WorkspacesAPI

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