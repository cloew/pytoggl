from ..model import Project, Workspace

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
        
    def findByName(self, name):
        """ Return the workspace with the given name """
        allWorkspaces = self.getAll()
        match = None
        matches = [workspace for workspace in allWorkspaces if workspace.name == name]
        
        if len(matches) > 0:
            match = matches[0]
        return match