from .nested_api import NestedApi

def nested_api_for(model, requestsApi):
    """ Add the proper init overload to properly initialize the NestedApi Subclass """
    def wrap(cls):
        def init(self, connection, parent):
            """ Initialize with the keyword arguments """
            NestedApi.__init__(self, model, requestsApi, connection, parent)
        cls.__init__ = init
        return cls
    return wrap