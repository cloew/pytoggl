from .actions import All, Get, WithName
from .model_api import ModelApi
from ..requests import RequestApis
from ..model import Workspace

class WorkspacesApi(ModelApi):
    """ Represents the Toggl Workspaces API """
    all = All()
    withId = Get()
    withName = WithName()
    
    def __init__(self, connection):
        """ Initialize the Workspaces API """
        ModelApi.__init__(self, Workspace, RequestApis.Workspaces, connection)