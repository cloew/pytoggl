
class Update:
    """ Represents the action to update the Data object """
    
    def __get__(self, obj, type=None):
        """ Return this descriptor or a method that updates the Data Object """
        def update():
            json = obj._api.update(obj.connection, obj.json, id=obj.id)
            obj.updateJson(json)
        
        if obj is None:
            return self
        else:
            return update