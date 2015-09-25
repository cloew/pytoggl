from .actions import GetCurrentTimer
from .api_for import api_for
from .model_api import ModelApi
from ..requests import RequestApis
from ..model import TimeEntry

@api_for(TimeEntry, RequestApis.Timer)
class TimerApi:
    """ Represents the Toggl Timer API """
    current = GetCurrentTimer()