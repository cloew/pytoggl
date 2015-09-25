
class KaoDescriptor:
    """ Helper class for generating descriptors that return themselves when accessed via a class """
    
    def __get__(self, obj, type=None):
        """ Call the _get method or return this descriptor if no obj was provided """
        if obj is None:
            return self
        else:
            return self._get(obj, type)