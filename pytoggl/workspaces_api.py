from workspace import Workspace

class WorkspacesAPI:
    """ Represents the Toggl Workspaces API """
    baseUrl = 'workspaces'
    
    def __init__(self, requestHelper):
        """ Initialize the Workspaces API """
        self.requestHelper = requestHelper
        
    def getAll(self):
        """ Return all the workspaces """
        response = self.requestHelper.sendRequest(self.baseUrl)
        workspaces = []
        if response.status_code == 200:
            for workspaceJSON in response.json():
                workspaces.append(Workspace(workspaceJSON))
            
        return workspaces