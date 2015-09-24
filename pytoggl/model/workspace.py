from .model import Model
from .model_for_api import model_for_api
from ..requests import RequestApis

@model_for_api(RequestApis.Workspaces)
class Workspace(Model):
    """ Represents a Toggl Workspace """
        
    def __repr__(self):
        """ String representation of the workspace """
        return "<Workspace({0})>".format(self.name)