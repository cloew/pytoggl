from ..model_wrapper import ModelWrapper

class NestedApi:
    """ Represents an Api that is nested within another Model """
    
    def __init__(self, modelCls, requestApi, connection, parent):
        """ Initialize with the Model Class, Request Api, connection and parent record """
        self.requestApi = requestApi
        self.connection = connection
        self.parent = parent
        self.buildModels = ModelWrapper(modelCls, connection)