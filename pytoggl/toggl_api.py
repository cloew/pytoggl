from request_helper import RequestHelper
from workspace import Workspace

class TogglAPI:
    """ Represents the top level of the Toggl API """
    
    def __init__(self, apiToken=None):
        """ Initialize the Toggl API """
        self.requestHelper = RequestHelper(apiToken)
        
    def getWorkspaces(self):
        """ Return all current Workspaces """
        response = self.requestHelper.sendRequest('workspaces')
        workspaces = []
        if response.status_code == 200:
            for workspaceJSON in response.json():
                workspaces.append(Workspace(workspaceJSON))
            
        return workspaces