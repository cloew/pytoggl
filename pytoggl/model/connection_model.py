
def connection_model(modelCls):
    """ Decorator to aid a wrapper method to construct the modelCLs and bind it ot the Connection instance """
    def wrapper(cls):
        def build(self, **kwargs):
            return modelCls(connection=self, **kwargs)
        setattr(cls, modelCls.__name__, build)
        return cls
    return wrapper