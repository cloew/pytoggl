from pytoggl.helpers import KaoDescriptor

class AllFromWorkspaces(KaoDescriptor):
    """ Action to return all elements of a Data Model by retrieving them from each of the workspaces """
    
    def _get(self, obj, type=None):
        """ Return a method that retrieves all the Data Model objects from each of the workspaces """
        def all():
            projects = []
            for workspace in obj.connection.workspaces.all():
                json = obj.requestApi.all(obj.connection, id=workspace.id)
                projects += obj.buildModels(json)
            return projects
        return all