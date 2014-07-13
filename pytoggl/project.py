
class Project:
    """ Represents a Toggl Project """
    
    def __init__(self, id=None, json=None):
        """ Initialize a Toggl Project """
        if json is not None:
            self.id = json["id"]
            self.name = json["name"]
        else:
            self.id = id
        
    def __repr__(self):
        """ String representation of the project """
        return "{0}:{1}".format(self.id, self.name)