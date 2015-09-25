from .model_api import ModelApi
from .nested_api import NestedApi

def api_for(model, requestsApi):
    """ Add the proper init overload to properly initialize the ModelApi Subclass """
    def wrap(cls):
        def init(self, connection):
            """ Initialize with the keyword arguments """
            ModelApi.__init__(self, model, requestsApi, connection)
        cls.__init__ = init
        return cls
    return wrap

def nested_api_for(model, requestsApi):
    """ Add the proper init overload to properly initialize the NestedApi Subclass """
    def wrap(cls):
        def init(self, connection, parent):
            """ Initialize with the keyword arguments """
            NestedApi.__init__(self, model, requestsApi, connection, parent)
        cls.__init__ = init
        return cls
    return wrap