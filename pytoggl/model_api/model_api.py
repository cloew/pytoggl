
class ModelApi:
    """ Represents the standard Model Api base class """
    
    def __init__(self, modelCls, jsonApi, apiHelper):
        """ Initialize with the Model Class to use and the Json Api """
        self.modelCls = modelCls
        self.jsonApi = jsonApi
        self.apiHelper = apiHelper
        
    def all(self):
        """ Return all the Model Objects for the list route """
        json = self.jsonApi.all(self.apiHelper)
        return self.buildModels(json)
        
    def withId(self, id):
        """ Return the specific Model Object for the item route """
        json = self.jsonApi.get(self.apiHelper, id=id)
        return self.buildModels([json])[0]
        
    def buildModels(self, json):
        """ Return the model objects to wrap the json """
        return [self.modelCls(jsonElement) for jsonElement in json]