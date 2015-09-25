from .actions import All, Get, WithName
from .api_for import api_for
from .model_api import ModelApi
from ..requests import RequestApis
from ..model import Workspace

@api_for(Workspace, RequestApis.Workspaces)
class WorkspacesApi(ModelApi):
    """ Represents the Toggl Workspaces API """
    all = All()
    withId = Get()
    withName = WithName()