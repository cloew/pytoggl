import requests

class RequestHelper:
    """ Helper class to perfor Toggl REST requests """
    url = 'https://www.toggl.com/api/v8'
    togglHeaders = {'content-type': 'application/json'}
    
    def __init__(self, apiToken=None):
        """ Initialize the Request Helper """
        self.togglAuth = (apiToken, 'api_token')
        
    def sendRequest(self, url):
        """ Send the given request to the url provided """
        fullUrl = "{0}/{1}".format(self.url, url)
        return requests.get(fullUrl, headers=self.togglHeaders, auth=self.togglAuth)