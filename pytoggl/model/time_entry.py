from .actions import Get, Create, Update, Delete, StartTimer, StopTimer
from .model import Model
from .model_for_api import model_for_api
from ..requests import RequestApis

@model_for_api(RequestApis.TimeEntries, created_with="pytoggl")
class TimeEntry(Model):
    """ Represents a Toggl Time Entry """
    get = Get()
    create = Create()
    update = Update()
    delete = Delete()
    start = StartTimer()
    stop = StopTimer()
        
    def __repr__(self):
        """ String representation of the project """
        return "<TimeEntry({0})>".format(self.description)