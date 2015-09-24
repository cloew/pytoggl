from .json_base import JsonBase

class Model:
    """ Represents a Model that wraps interaction with a JSON data object for the Toggl API """
    
    def __init__(self, api, connection=None, **kwargs):
        """ Initialize with the Api to bind to and the kwargs to populate with """
        self._api = api
        self._data = JsonBase(**kwargs)
        self.connection = connection
        
    def update(self):
        """ Update this model using the Toggl Api """
        json = self._api.update(self.connection, self.json, id=self.id)
        self.updateJson(json)
        
    def delete(self):
        """ Delete this model using the Toggl Api """
        return self._api.delete(self.connection, id=self.id)
            
    @property
    def json(self):
        """ Return the Json for this model """
        return {self._api.jsonName: self._data.json}
        
    def updateJson(self, data):
        """ Update the Json for this model """
        self._data.update(data)
        
    def __getattr__(self, name):
        """ Return an attribute of the Model """
        return getattr(self._data, name)
            
    def __setattr__(self, name, value):
        """ Set an attribute of the Model """
        if name in ["_api", "connection", "_data"]:
            self.__dict__[name] = value
        else:
            setattr(self._data, name, value)