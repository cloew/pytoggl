from pytoggl.helpers import KaoDescriptor
from pytoggl.requests import RequestApis

class StopTimer(KaoDescriptor):
    """ Represents the action to stop the Timer """
    
    def _get(self, obj, type=None):
        """ Return a method that stops the Timer """
        def stop():
            json = RequestApis.Timer.stop(obj.connection, id=obj.id)
            obj.updateJson(json)
        return stop