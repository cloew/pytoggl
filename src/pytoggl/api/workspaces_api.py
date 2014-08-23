from pytoggl.model.project import Project
from pytoggl.model.workspace import Workspace

class WorkspacesAPI:
    """ Represents the Toggl Workspaces API """
    baseUrl = 'workspaces'
    
    def __init__(self, apiHelper):
        """ Initialize the Workspaces API """
        self.apiHelper = apiHelper
        
    def getAll(self):
        """ Return all the workspaces """
        json = self.apiHelper.get(self.baseUrl)
        
        workspaces = []
        for workspaceJSON in json:
            workspaces.append(Workspace(json=workspaceJSON))
            
        return workspaces
        
    def getProjects(self, workspace):
        """ Return all projects for the given workspace """
        url = "{0}/{1}/projects".format(self.baseUrl, workspace.id)
        json = self.apiHelper.get(url)
        
        projects = []
        for projectJSON in json:
            projects.append(Project(json=projectJSON))
            
        return projects