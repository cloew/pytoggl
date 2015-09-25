from .model_wrapper import ModelWrapper

class ModelApi:
    """ Represents the standard Model Api base class """
    
    def __init__(self, modelCls, requestApi, connection):
        """ Initialize with the Model Class to use and the Json Api """
        self.requestApi = requestApi
        self.connection = connection
        self.buildModels = ModelWrapper(modelCls, connection)