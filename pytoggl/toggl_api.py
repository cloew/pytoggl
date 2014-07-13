from workspace import Workspace

import requests

class TogglAPI:
    """ Represents the top level of the Toggl API """
    url = 'https://www.toggl.com/api/v8'
    togglHeaders = {'content-type': 'application/json'}
    
    def __init__(self, apiToken=None):
        """ Initialize the Toggl API """
        self.apiToken = apiToken
        self.togglAuth = (self.apiToken, 'api_token')
        
    def getWorkspaces(self):
        """ Return all current Workspaces """
        response = requests.get(self.url+'/workspaces', headers=self.togglHeaders, auth=self.togglAuth)
        workspaces = []
        if response.status_code == 200:
            for workspaceJSON in response.json():
                workspaces.append(Workspace(workspaceJSON))
            
        return workspaces