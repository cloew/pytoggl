
class ProjectsAPI:
    """ Represents the Toggl Projects API """
    baseUrl = 'projects'
    
    def __init__(self, requestHelper):
        """ Initialize the Projects API """
        self.requestHelper = requestHelper