from .data_api import DataApi
from ..routes import Routes

class Apis:
    """ Helper class to wrap all the various Json Apis """
    Workspaces = DataApi(Routes.Workspaces, Routes.Workspace)