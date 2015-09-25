from .model_api import ModelApi
from .nested_api import NestedApi

def api_for(model, requestsApi):
    """ Add the proper init overload to properly initialize the ModelApi Subclass """
    return base_api_for(model, requestsApi, ModelApi)

def nested_api_for(model, requestsApi):
    """ Add the proper init overload to properly initialize the NestedApi Subclass """
    return base_api_for(model, requestsApi, NestedApi)

def base_api_for(model, requestsApi, baseCls):
    """ Add the proper init overload to properly initialize the baseCls Subclass """
    def wrap(cls):
        def init(self, connection, parent):
            """ Initialize with the keyword arguments """
            baseCls.__init__(self, model, requestsApi, connection, parent)
        cls.__init__ = init
        return cls
    return wrap