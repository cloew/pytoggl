from .json_base import JsonBase

class Project(JsonBase):
    """ Represents a Toggl Project """
            
    def toJSONDictionary(self):
        """ Convert the Project to JSON """
        return {"project":JsonBase.toJSONDictionary(self)}
        
    def __repr__(self):
        """ String representation of the project """
        return "{0}:{1}".format(self.id, self.name)