from .actions import All, Get
from .model_api import ModelApi
from ..requests import RequestApis
from ..model import Workspace

class WorkspacesApi(ModelApi):
    """ Represents the Toggl Workspaces API """
    all = All()
    withId = Get()
    
    def __init__(self, connection):
        """ Initialize the Workspaces API """
        ModelApi.__init__(self, Workspace, RequestApis.Workspaces, connection)
        
    def withName(self, name):
        """ Return the workspaces with the given name """
        return [workspace for workspace in self.all() if workspace.name == name]