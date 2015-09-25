from pytoggl.helpers import KaoDescriptor

class AccessApi(KaoDescriptor):
    """ Represents an action to access a Nested Api """
    
    def __init__(self, apiCls):
        """ Initialize with the Api to access """
        self.apiCls = apiCls
    
    def _get(self, obj, type=None):
        """ Return a method that the Data Object from the Model's Json """
        return self.apiCls(obj.connection, obj)