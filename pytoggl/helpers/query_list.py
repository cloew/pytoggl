from kao_decorators import proxy_for

@proxy_for('lst', ['__iter__', '__getitem__', '__contains__', '__len__'])
class QueryList:
    """ Helper class to allow you to access the first element of a list """
    
    def __init__(self, lst):
        """ Initialize with the list """
        self.lst = lst
       
    @property
    def first(self):
        """ Return the first element of the list if one exists """
        return self.lst[0] if len(self) > 0 else None