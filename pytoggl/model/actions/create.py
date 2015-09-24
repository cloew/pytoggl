
class Create:
    """ Represents the action to send Data to the Api and create the Data object """
    
    def __get__(self, obj, type=None):
        """ Return this descriptor or a method that the Data Object from the Model's Json """
        def create():
            json = obj._api.create(obj.connection, obj.json)
            obj.updateJson(json)
        
        if obj is None:
            return self
        else:
            return create