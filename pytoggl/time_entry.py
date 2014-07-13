
class TimeEntry:
    """ Represents a Toggl Time Entry """
    
    def __init__(self, description=None, project=None, json=None):
        """ Initialize a Toggl Time Entry """
        if json is not None:
            json = json["data"]
            self.id = json["id"]
            self.description = json["description"]
        else:
            self.pid = project.id
            self.description = description
            
    def toJSONDictionary(self):
        """ Convert the Time Entry to JSON """
        return {"time_entry":{"description":self.description, "pid":self.pid}}
        
    def __repr__(self):
        """ String representation of the Time Entry """
        return "{0}:{1}".format(self.id, self.description)