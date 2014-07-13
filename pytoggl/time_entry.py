
class TimeEntry:
    """ Represents a Toggl Time Entry """
    
    def __init__(self, json=None):
        """ Initialize a Toggl Time Entry """
        json = json["data"]
        self.id = json["id"]
        self.description = json["description"]
        
    def __repr__(self):
        """ String representation of the Time Entry """
        return "{0}:{1}".format(self.id, self.description)