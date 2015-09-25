
class ModelWrapper:
    """ Helper class to wrap json with Model Classes """
    
    def __init__(self, modelCls, connection):
        """ Intialize with the Model Class and Connection """
        self.modelCls = modelCls
        self.connection = connection
        
    def __call__(self, json):
        """ Wrap the json with the Model Class """
        return [self.modelCls(connection=self.connection, **jsonElement) for jsonElement in json]