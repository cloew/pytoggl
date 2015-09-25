from enum import Enum

class Routes(Enum):
    """ Represents the various routes associated with the Toggl API """
    Workspaces = "workspaces"
    Workspace = "workspaces/{id}"
    WorkspaceProjects = "workspaces/{id}/projects"
    Projects = "projects"
    Project = "projects/{id}"
    TimeEntries = "time_entries"
    TimeEntry = "time_entries/{id}"
    StartTimer = "time_entries/start"
    StopTimer = "time_entries/{id}/stop"
    CurrentTimer = "time_entries/current"
    
    def build(self, **kwargs):
        """ Build the Url with the given arguments """
        return self.value.format(**kwargs)