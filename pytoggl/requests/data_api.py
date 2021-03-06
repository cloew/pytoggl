from ..routes import Routes

class DataApi:
    """ Represents the various Apis that can be accessed """
    
    def __init__(self, jsonName, *, all, item, create=None):
        """ Initialize the API with the List Route and Item Route """
        self.jsonName = jsonName
        self.listRoute = all
        self.itemRoute = item
        self.createRoute = create if create is not None else all
        
    def all(self, connection, **kwargs):
        """ Return all the Json for the list route """
        return connection.get(self.listRoute.build(**kwargs))
        
    def get(self, connection, **kwargs):
        """ Return the specific Json for the item route """
        return connection.get(self.itemRoute.build(**kwargs))
        
    def create(self, connection, data):
        """ Create a new Data Object and return its Json """
        return connection.post(self.createRoute.build(), data=data)
        
    def update(self, connection, data, **kwargs):
        """ Update the Data Object and return its Json """
        return connection.put(self.itemRoute.build(**kwargs), data=data)
        
    def delete(self, connection, **kwargs):
        """ Delete the Data Object and return its success """
        return connection.delete(self.itemRoute.build(**kwargs))