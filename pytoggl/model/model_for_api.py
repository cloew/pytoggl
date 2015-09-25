from .model import Model

def model_for_api(api, **defaults):
    """ Add the proper init overload to properly initialize the Model Subclass """
    def wrap(cls):
        def load(self, **kwargs):
            """ Initialize with the keyword arguments """
            keywords = dict(defaults)
            keywords.update(kwargs)
            Model.__init__(self, api, **keywords)
        cls.__init__ = load
        return cls
    return wrap