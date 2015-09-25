from pytoggl.helpers import KaoDescriptor

class GetCurrentTimer(KaoDescriptor):
    """ Action to return the Time Entry for the Current Timer """
    
    def _get(self, obj, type=None):
        """ Return a method that retrieves the Time Entry for the current Timer """
        def get():
            json = obj.requestApi.current(obj.connection)
            return obj.buildModels([json])[0]
        return get