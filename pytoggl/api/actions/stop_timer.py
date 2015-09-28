from pytoggl.helpers import KaoDescriptor

class StopTimer(KaoDescriptor):
    """ Action to stop the current Time Entry """
    
    def _get(self, obj, type=None):
        """ Return a method that stops the current Time Entry """
        def stop():
            currentEntry = obj.current()
            return currentEntry.stop()
        return stop