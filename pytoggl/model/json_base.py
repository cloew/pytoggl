import sys

class JsonBase:
    """ Represents a JSON based class """
    
    def __init__(self, **kwargs):
        """ Initialize the JSON Record """
        self._values = {}
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    @property
    def json(self):
        """ Return the Json for this model """
        return self._values
        
    def __getattr__(self, name):
        """ Return an attribute of the JSON Base """
        if name in self._values:
            return self._values[name]
        else:
            raise AttributeError(name)
            
    def __setattr__(self, name, value):
        """ Return an attribute of the JSON Base """
        if name == "_values":
            self.__dict__[name] = value
        else:
            self._values[name] = value