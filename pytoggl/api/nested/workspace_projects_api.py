from .nested_api import NestedApi
from .nested_api_for import nested_api_for
from ..actions import NestedAll, WithName

from pytoggl.requests import RequestApis
from pytoggl.model.project import Project

@nested_api_for(Project, RequestApis.Projects)
class WorkspaceProjectsApi(NestedApi):
    """ Represents the Toggl Projects API nested within Workspaces """
    all = NestedAll()
    withName = WithName()