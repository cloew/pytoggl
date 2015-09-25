from ..routes import Routes

class TimerApi:
    """ Represents the Toggl Timer API """
    
    def start(self, connection, data):
        """ Start the Time Entry """
        url = Routes.StartTimer.build()
        return connection.post(url, data=data)
    
    def stop(self, connection, *, id):
        """ Stop the Time Entry """
        url = Routes.StopTimer.build(id=id)
        return connection.put(url)
    
    def current(self, connection):
        """ Return the current Time Entry """
        url = Routes.CurrentTimer.build()
        return connection.get(url)