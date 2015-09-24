from .model import Model
from ..requests import RequestApis

class Workspace(Model):
    """ Represents a Toggl Workspace """
    
    def __init__(self, **kwargs):
        """ Initialize with the keyword arguments """
        Model.__init__(self, RequestApis.Workspaces, **kwargs)
        
    def __repr__(self):
        """ String representation of the workspace """
        return "<Workspace({0})>".format(self.name)