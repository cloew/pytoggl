
class All:
    """ Action to return all elements of a Data Model """
    
    def __get__(self, obj, type=None):
        """ Return this descriptor or a method that retrieves and updates a Model's Json """
        def all():
            json = obj.jsonApi.all(obj.connection)
            return obj.buildModels(json)
        
        if obj is None:
            return self
        else:
            return all