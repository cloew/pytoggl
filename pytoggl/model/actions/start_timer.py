from pytoggl.helpers import KaoDescriptor
from pytoggl.requests import RequestApis

class StartTimer(KaoDescriptor):
    """ Represents the action to start the Timer """
    
    def _get(self, obj, type=None):
        """ Return a method to start the Timer """
        def start():
            json = RequestApis.Timer.start(obj.connection, obj.json)
            obj.updateJson(json)
        return start