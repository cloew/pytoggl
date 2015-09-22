import sys

class JsonBase:
    """ Represents a JSON based class """
    
    def __init__(self, json=None, **kwargs):
        """ Initialize the JSON Record """
        self.__values = {}
        if json is not None:
            self.__values = json
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
            
    def toJSONDictionary(self):
        """ Retrieve the JSON values """
        return self.__values
        
    def __getattr__(self, name):
        """ Return an attribute of the JSON Base """
        if name == "_JsonBase__values":
            return self.__values
        elif name in self.__values:
            return self.__values[name]
        else:
            raise AttributeError(name)
            
    def __setattr__(self, name, value):
        """ Return an attribute of the JSON Base """
        if name == "_JsonBase__values":
            self.__dict__[name] = value
        else:
            self.__values[name] = value