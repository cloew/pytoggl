from pytoggl.helpers import KaoDescriptor

class Delete(KaoDescriptor):
    """ Represents the action to delete the Data object """
    
    def _get(self, obj, type=None):
        """ Return a method that deletes the Data Object """
        def delete():
            return obj._api.delete(obj.connection, id=obj.id)
        return delete