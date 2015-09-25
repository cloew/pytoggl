from .api.top_level_apis import TopLevelApis
from .helpers import ApiHelper
from .model import wrap_models

from kao_decorators import proxy_for

@proxy_for('apiHelper', ['get', 'post', 'put', 'delete'])
@wrap_models
class TogglConnection:
    """ Represents a connection to the Toggl API """
    
    def __init__(self, apiToken=None):
        """ Initialize the Toggl API """
        self.apiHelper = ApiHelper(apiToken)
        for api in TopLevelApis:
            setattr(self, api.name, api.value(self))