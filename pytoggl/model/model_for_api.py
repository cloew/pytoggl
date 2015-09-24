from .model import Model

def model_for_api(api):
    """ Add the proper init overload to properly initialize the Model Subclass """
    def wrap(cls):
        def load(self, **kwargs):
            """ Initialize with the keyword arguments """
            Model.__init__(self, api, **kwargs)
        cls.__init__ = load
        return cls
    return wrap