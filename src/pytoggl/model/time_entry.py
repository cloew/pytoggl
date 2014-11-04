from json_base import JsonBase

class TimeEntry(JsonBase):
    """ Represents a Toggl Time Entry """
    
    def __init__(self, json=None, created_with="pytoggl", **kwargs):
        """ Initialize the Time Entry """
        JsonBase.__init__(self, json=json, created_with=created_with, **kwargs)
            
    def toJSONDictionary(self):
        """ Convert the Time Entry to JSON """
        return {"time_entry":JsonBase.toJSONDictionary(self)}
        
    def __repr__(self):
        """ String representation of the Time Entry """
        return "{0}:{1}".format(self.id, self.description)