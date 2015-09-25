
def connection_models(modelClasses):
    """ Decorator to add Model Class wrapper methods to a Connection """
    def wrap(cls):
        for modelCls in modelClasses:
            cls = connection_model(modelCls)(cls)
        return cls
    return wrap

def connection_model(modelCls):
    """ Decorator to aid a wrapper method to construct the modelCLs and bind it ot the Connection instance """
    def wrap(cls):
        def build(self, **kwargs):
            return modelCls(connection=self, **kwargs)
        setattr(cls, modelCls.__name__, build)
        return cls
    return wrap