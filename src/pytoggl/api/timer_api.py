from pytoggl.model.time_entry import TimeEntry

class TimerAPI:
    """ Represents the Toggl Timer API """
    baseUrl = 'time_entries'
    
    def __init__(self, apiHelper):
        """ Initialize the Timer API """
        self.apiHelper = apiHelper
        
    def startTimer(self, timeEntry):
        """ Start the Timer """
        url = "{0}/start".format(self.baseUrl)
        json = self.apiHelper.post(url, data=timeEntry.toJSONDictionary(), getData=True)
        return TimeEntry(json=json)
        
    def stopTimer(self, timeEntry):
        """ Stop the Timer """
        url = "{0}/{1}/stop".format(self.baseUrl, timeEntry.id)
        json = self.apiHelper.put(url, getData=True)
        return TimeEntry(json=json)
        
    def current(self):
        """ Return the current Time Entry """
        url = "{0}/current".format(self.baseUrl)
        json = self.apiHelper.get(url, getData=True)
        return TimeEntry(json=json)