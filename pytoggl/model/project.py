import sys
class Project(object):
    """ Represents a Toggl Project """
    
    def __init__(self, json=None, **kwargs):
        """ Initialize a Toggl Project """
        self.__values = {}
        if json is not None:
            self.__values = json
        else:
            for key, value in kwargs.iteritems():
                setattr(self, key, value)
            
    def toJSONDictionary(self):
        """ Convert the Time Entry to JSON """
        return {"project":self.__values}
        
    def __getattr__(self, name):
        """ Return an attribute of the project """
        if name == "_Project__values":
            return self.__values
        elif name in self.__values:
            return self.__values[name]
        else:
            raise AttributeError(name)
            
    def __setattr__(self, name, value):
        """ Return an attribute of the project """
        if name == "_Project__values":
            self.__dict__[name] = value
        else:
            self.__values[name] = value
        
    def __repr__(self):
        """ String representation of the project """
        return "{0}:{1}".format(self.id, self.name)