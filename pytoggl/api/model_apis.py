from ..routes import Routes
from ..model import Workspace
from enum import Enum

class ModelApis(Enum):
    """ Represents the various Apis that can be accessed """
    Workspaces = Workspace, Routes.Workspaces, Routes.Workspace
    
    def __init__(self, modelCls, listRoute, itemRoute):
        """ Initialize the API with the List Route and Item Route """
        self.modelCls = modelCls
        self.listRoute = listRoute
        self.itemRoute = itemRoute
        
    def all(self, apiHelper):
        """ Return all the Model Objects for the list route """
        json = apiHelper.get(self.listRoute.build())
        return self.buildModels(json)
        
    def get(self, apiHelper, **kwargs):
        """ Return the specific Model Object for the item route """
        json = apiHelper.get(self.itemRoute.build(**kwargs), getData=True)
        return self.buildModels([json])
        
    def buildModels(self, json):
        """ Return the model objects to wrap the json """
        return [self.modelCls(jsonElement) for jsonElement in json]