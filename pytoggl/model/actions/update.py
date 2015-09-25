from pytoggl.helpers import KaoDescriptor

class Update(KaoDescriptor):
    """ Represents the action to update the Data object """
    
    def _get(self, obj, type=None):
        """ Return a method that updates the Data Object """
        def update():
            json = obj._api.update(obj.connection, obj.json, id=obj.id)
            obj.updateJson(json)
        return update