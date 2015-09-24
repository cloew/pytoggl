from .data_api import DataApi
from ..routes import Routes

class RequestApis:
    """ Helper class to wrap all the various Json Apis """
    Workspaces = DataApi('workspace', Routes.Workspaces, Routes.Workspace)