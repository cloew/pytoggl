from ..routes import Routes

class DataApi:
    """ Represents the various Apis that can be accessed """
    
    def __init__(self, listRoute, itemRoute):
        """ Initialize the API with the List Route and Item Route """
        self.listRoute = listRoute
        self.itemRoute = itemRoute
        
    def all(self, connection):
        """ Return all the Json for the list route """
        return connection.get(self.listRoute.build())
        
    def get(self, connection, **kwargs):
        """ Return the specific Json for the item route """
        return connection.get(self.itemRoute.build(**kwargs))
        
    def create(self, connection, data):
        """ Create a new Data Object and return its Json """
        return connection.post(self.listRoute.build(), data=data)
        
    def update(self, connection, data, **kwargs):
        """ Update the Data Object and return its Json """
        return connection.put(self.itemRoute.build(**kwargs), data=data)
        
    def delete(self, connection, **kwargs):
        """ Delete the Data Object and return its success """
        return connection.delete(self.itemRoute.build(**kwargs))