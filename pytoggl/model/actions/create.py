from pytoggl.helpers import KaoDescriptor

class Create(KaoDescriptor):
    """ Represents the action to send Data to the Api and create the Data object """
    
    def _get(self, obj, type=None):
        """ Return a method that the Data Object from the Model's Json """
        def create():
            json = obj._api.create(obj.connection, obj.json)
            obj.updateJson(json)
        return create