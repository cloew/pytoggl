from project import Project

class ProjectsAPI:
    """ Represents the Toggl Projects API """
    baseUrl = 'projects'
    
    def __init__(self, requestHelper):
        """ Initialize the Projects API """
        self.requestHelper = requestHelper
        
    def create(self, project):
        """ Create a new project from the given project """
        url = "{0}".format(self.baseUrl)
        response = self.requestHelper.post(url, data=project.toJSONDictionary())
        
        createdProject = None
        if response.status_code == 200 and response.json()["data"] is not None:
            createdProject = Project(json=response.json()["data"])
        print response.status_code, response
        return createdProject