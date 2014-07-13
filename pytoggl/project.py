
class Project:
    """ Represents a Toggl Project """
    
    def __init__(self, json=None):
        """ Initialize a Toggl Project """
        self.id = json["id"]
        self.name = json["name"]
        
    def __repr__(self):
        """ String representation of the project """
        return "{0}:{1}".format(self.id, self.name)