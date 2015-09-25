from pytoggl.helpers import KaoDescriptor

class WithName(KaoDescriptor):
    """ Action to return elements of a Data Model with a particular name """
    
    def _get(self, obj, type=None):
        """ Return a method that retrieves and updates a Model's Json """
        def get(name):
            return [model for model in obj.all() if model.name == name]
        return get