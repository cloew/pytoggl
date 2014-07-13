
class Workspace:
    """ Represents a Toggl Workspace """
    
    def __init__(self, json=None):
        """ Initialize a Toggl Workspace """
        self.id = json["id"]
        self.name = json["name"]
        
    def __repr__(self):
        """ String representation of the workspace """
        return "{0}:{1}".format(self.id, self.name)