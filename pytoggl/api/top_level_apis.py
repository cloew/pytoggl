from .workspaces_api import WorkspacesApi

from enum import Enum

class TopLevelApis(Enum):
    """ Represents all the top level Apis that can be accessed """
    workspaces = WorkspacesApi