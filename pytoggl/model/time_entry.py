from json_base import JsonBase

class TimeEntry(JsonBase):
    """ Represents a Toggl Time Entry """
            
    def toJSONDictionary(self):
        """ Convert the Time Entry to JSON """
        return {"time_entry":JsonBase.toJSONDictionary(self)}
        
    def __repr__(self):
        """ String representation of the Time Entry """
        return "{0}:{1}".format(self.id, self.description)