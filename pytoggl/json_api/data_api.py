from ..routes import Routes
from ..model import Workspace
from enum import Enum

class DataApi:
    """ Represents the various Apis that can be accessed """
    
    def __init__(self, listRoute, itemRoute):
        """ Initialize the API with the List Route and Item Route """
        self.listRoute = listRoute
        self.itemRoute = itemRoute
        
    def all(self, apiHelper):
        """ Return all the Json for the list route """
        return apiHelper.get(self.listRoute.build())
        
    def get(self, apiHelper, **kwargs):
        """ Return the specific Json for the item route """
        return apiHelper.get(self.itemRoute.build(**kwargs), getData=True)
        
    def create(self, apiHelper, data):
        """ Create a new Data Object and return its Json """
        return apiHelper.post(self.listRoute.build(), data=data, getData=True)
        
    def update(self, apiHelper, data, **kwargs):
        """ Update the Data Object and return its Json """
        return apiHelper.put(self.itemRoute.build(**kwargs), data=data, getData=True)
        
    def delete(self, apiHelper, **kwargs):
        """ Delete the Data Object and return its success """
        return apiHelper.delete(self.itemRoute.build(**kwargs))