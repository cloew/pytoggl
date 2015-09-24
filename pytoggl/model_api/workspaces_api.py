from .model_api import ModelApi
from ..json_api import Apis
from ..model import Workspace

class WorkspacesApi(ModelApi):
    """ Represents the Toggl Workspaces API """
    
    def __init__(self, apiHelper):
        """ Initialize the Workspaces API """
        ModelApi.__init__(self, Workspace, Apis.Workspaces, apiHelper)
        
    def withName(self, name):
        """ Return the workspaces with the given name """
        return [workspace for workspace in self.all() if workspace.name == name]