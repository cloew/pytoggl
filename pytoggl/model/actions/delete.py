
class Delete:
    """ Represents the action to delete the Data object """
    
    def __get__(self, obj, type=None):
        """ Return this descriptor or a method that deletes the Data Object """
        def delete():
            return obj._api.delete(obj.connection, id=obj.id)
        
        if obj is None:
            return self
        else:
            return delete