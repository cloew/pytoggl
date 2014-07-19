from json_base import JsonBase

class Workspace(JsonBase):
    """ Represents a Toggl Workspace """
        
    def __repr__(self):
        """ String representation of the workspace """
        return "{0}:{1}".format(self.id, self.name)