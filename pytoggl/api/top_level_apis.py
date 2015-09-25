from .projects_api import ProjectsApi
from .workspaces_api import WorkspacesApi

from enum import Enum

class TopLevelApis(Enum):
    """ Represents all the top level Apis that can be accessed """
    projects = ProjectsApi
    workspaces = WorkspacesApi