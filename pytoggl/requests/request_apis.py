from .data_api import DataApi
from .timer_api import TimerApi
from ..routes import Routes

class RequestApis:
    """ Helper class to wrap all the various Json Apis """
    Workspaces = DataApi('workspace', all=Routes.Workspaces, item=Routes.Workspace)
    Projects = DataApi('project', all=Routes.WorkspaceProjects, item=Routes.Project, create=Routes.Projects)
    Timer = TimerApi()