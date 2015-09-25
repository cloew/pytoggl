from .connection_model import connection_models

from .project import Project
from .time_entry import TimeEntry
from .workspace import Workspace

all_models = [Project, Workspace]

wrap_models = connection_models(all_models)