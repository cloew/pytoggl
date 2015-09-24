from ..routes import Routes
from ..model import Workspace
from enum import Enum

class ModelApis(Enum):
    """ Represents the various Apis that can be accessed """
    Workspaces = Routes.Workspaces, Routes.Workspace
    
    def __init__(self, listRoute, itemRoute):
        """ Initialize the API with the List Route and Item Route """
        self.listRoute = listRoute
        self.itemRoute = itemRoute
        
    def all(self, apiHelper):
        """ Return all the Model Objects for the list route """
        return apiHelper.get(self.listRoute.build())
        
    def get(self, apiHelper, **kwargs):
        """ Return the specific Model Object for the item route """
        return apiHelper.get(self.itemRoute.build(**kwargs), getData=True)