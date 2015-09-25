from .actions import Get, Create, Update, Delete
from .model import Model
from .model_for_api import model_for_api
from ..requests import RequestApis

@model_for_api(RequestApis.Projects)
class Project(Model):
    """ Represents a Toggl Project """
    get = Get()
    create = Create()
    update = Update()
    delete = Delete()
        
    def __repr__(self):
        """ String representation of the project """
        return "<Project({0})>".format(self.name)