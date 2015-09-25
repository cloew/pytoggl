from pytoggl.helpers import KaoDescriptor

class All(KaoDescriptor):
    """ Action to return all elements of a Data Model """
    
    def _get(self, obj, type=None):
        """ Return a method that retrieves and updates a Model's Json """
        def all():
            json = obj.jsonApi.all(obj.connection)
            return obj.buildModels(json)
        return all