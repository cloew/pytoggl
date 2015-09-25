
class ModelApi:
    """ Represents the standard Model Api base class """
    
    def __init__(self, modelCls, requestApi, connection):
        """ Initialize with the Model Class to use and the Json Api """
        self.modelCls = modelCls
        self.requestApi = requestApi
        self.connection = connection
        
    def buildModels(self, json):
        """ Return the model objects to wrap the json """
        return [self.modelCls(connection=self.connection, **jsonElement) for jsonElement in json]