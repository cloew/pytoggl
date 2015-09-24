
class Get:
    """ Represents the action to get the latest Json for a data object """
    
    def __get__(self, obj, type=None):
        """ Return this descriptor or a method that retrieves and updates a Model's Json """
        def get():
            json = obj._api.get(obj.connection, id=obj.id)
            obj.updateJson(json)
        
        if obj is None:
            return self
        else:
            return get