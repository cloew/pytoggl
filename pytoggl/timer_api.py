from time_entry import TimeEntry

class TimerAPI:
    """ Represents the Toggl Timer API """
    baseUrl = 'time_entries'
    
    def __init__(self, requestHelper):
        """ Initialize the Timer API """
        self.requestHelper = requestHelper
        
    def startTimer(self):
        """ Start the Timer """
        
    def current(self):
        """ Return the current Time Entry """
        url = "{0}/current".format(self.baseUrl)
        response = self.requestHelper.get(url)
        
        currentTimeEntry = None
        if response.status_code == 200 and response.json()["data"] is not None:
            currentTimeEntry = TimeEntry(json=response.json())
            
        return currentTimeEntry