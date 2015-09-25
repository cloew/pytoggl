from .actions import AllFromWorkspaces, Get, WithName
from .api_for import api_for
from .model_api import ModelApi
from ..requests import RequestApis
from ..model import Project

@api_for(Project, RequestApis.Projects)
class ProjectsApi(ModelApi):
    """ Represents the Toggl Projects API """
    all = AllFromWorkspaces()
    withId = Get()
    withName = WithName()