from time_entry import TimeEntry

class TimerAPI:
    """ Represents the Toggl Timer API """
    baseUrl = 'time_entries'
    
    def __init__(self, requestHelper):
        """ Initialize the Timer API """
        self.requestHelper = requestHelper
        
    def current(self):
        """ Return the current Time Entry """
        url = "{0}/current".format(self.baseUrl)
        response = self.requestHelper.sendRequest(url)
        
        currentTimeEntry = None
        if response.status_code == 200:
            currentTimeEntry = TimeEntry(json=response.json())
            
        return currentTimeEntry