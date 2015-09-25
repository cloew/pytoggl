from pytoggl.helpers import KaoDescriptor

class Get(KaoDescriptor):
    """ Represents the action to get the latest Json for a data object """
    
    def _get(self, obj, type=None):
        """ Return a method that retrieves and updates a Model's Json """
        def get():
            json = obj._api.get(obj.connection, id=obj.id)
            obj.updateJson(json)
        return get