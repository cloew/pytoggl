from .actions import Get, Update, AccessApi
from .model import Model
from .model_for_api import model_for_api
from ..api.nested import WorkspaceProjectsApi
from ..requests import RequestApis

@model_for_api(RequestApis.Workspaces)
class Workspace(Model):
    """ Represents a Toggl Workspace """
    get = Get()
    update = Update()
    projects = AccessApi(WorkspaceProjectsApi)
        
    def __repr__(self):
        """ String representation of the workspace """
        return "<Workspace({0})>".format(self.name)