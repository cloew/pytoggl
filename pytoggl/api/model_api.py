
class ModelApi:
    """ Represents the standard Model Api base class """
    
    def __init__(self, modelCls, requestApi, connection):
        """ Initialize with the Model Class to use and the Json Api """
        self.modelCls = modelCls
        self.requestApi = requestApi
        self.connection = connection
        
    def withId(self, id):
        """ Return the specific Model Object for the item route """
        json = self.requestApi.get(self.connection, id=id)
        return self.buildModels([json])[0]
        
    def buildModels(self, json):
        """ Return the model objects to wrap the json """
        return [self.modelCls(connection=self.connection, **jsonElement) for jsonElement in json]