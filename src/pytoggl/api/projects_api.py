from ..model import Project

class ProjectsAPI:
    """ Represents the Toggl Projects API """
    baseUrl = 'projects'
    
    def __init__(self, apiHelper):
        """ Initialize the Projects API """
        self.apiHelper = apiHelper
        
    def create(self, project):
        """ Create a new project from the given project """
        url = "{0}".format(self.baseUrl)
        json = self.apiHelper.post(url, data=project.toJSONDictionary(), getData=True)
        return Project(json=json)