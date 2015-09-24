
class ModelApi:
    """ Represents the standard Model Api base class """
    
    def __init__(self, modelCls, jsonApi, connection):
        """ Initialize with the Model Class to use and the Json Api """
        self.modelCls = modelCls
        self.jsonApi = jsonApi
        self.connection = connection
        
    def all(self):
        """ Return all the Model Objects for the list route """
        json = self.jsonApi.all(self.connection)
        return self.buildModels(json)
        
    def withId(self, id):
        """ Return the specific Model Object for the item route """
        json = self.jsonApi.get(self.connection, id=id)
        return self.buildModels([json])[0]
        
    def buildModels(self, json):
        """ Return the model objects to wrap the json """
        return [self.modelCls(connection=self.connection, **jsonElement) for jsonElement in json]