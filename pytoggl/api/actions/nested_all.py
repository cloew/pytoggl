from pytoggl.helpers import KaoDescriptor

class NestedAll(KaoDescriptor):
    """ Action to return all elements of a Data Model nested within a parent """
    
    def _get(self, obj, type=None):
        """ Return a method that retrieves and builds all the Data Model objects for a parent model """
        def all():
            json = obj.requestApi.all(obj.connection, id=obj.parent.id)
            return obj.buildModels(json)
        return all