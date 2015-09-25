from .actions import NestedAll, WithName
from .api_for import nested_api_for
from .nested_api import NestedApi
from ..requests import RequestApis
from ..model.project import Project

@nested_api_for(Project, RequestApis.Projects)
class WorkspaceProjectsApi(NestedApi):
    """ Represents the Toggl Projects API nested within Workspaces """
    all = NestedAll()
    withName = WithName()