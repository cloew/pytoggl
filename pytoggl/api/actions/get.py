from pytoggl.helpers import KaoDescriptor

class Get(KaoDescriptor):
    """ Action to return an element of a Data Model with a particular id """
    
    def _get(self, obj, type=None):
        """ Return a method that retrieves and updates a Model's Json """
        def get(id):
            json = obj.requestApi.get(obj.connection, id=id)
            return obj.buildModels([json])[0]
        return get