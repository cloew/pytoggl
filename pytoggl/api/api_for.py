from .model_api import ModelApi

def api_for(model, requestsApi):
    """ Add the proper init overload to properly initialize the ModelApi Subclass """
    def wrap(cls):
        def init(self, connection):
            """ Initialize with the keyword arguments """
            ModelApi.__init__(self, model, requestsApi, connection)
        cls.__init__ = init
        return cls
    return wrap