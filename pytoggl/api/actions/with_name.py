from pytoggl.helpers import KaoDescriptor, QueryList

class WithName(KaoDescriptor):
    """ Action to return elements of a Data Model with a particular name """
    
    def _get(self, obj, type=None):
        """ Return a method that retrieves all the Data Model objects with the given name """
        def get(name):
            return QueryList([model for model in obj.all() if model.name == name])
        return get