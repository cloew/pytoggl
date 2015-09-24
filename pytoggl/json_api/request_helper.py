import json
import requests

class RequestHelper:
    """ Helper class to perform Toggl REST requests """
    url = 'https://www.toggl.com/api/v8'
    togglHeaders = {'content-type': 'application/json'}
    
    def __init__(self, apiToken=None):
        """ Initialize the Request Helper """
        self.togglAuth = (apiToken, 'api_token')
        
    def get(self, url):
        """ Send a get request to the url provided """
        fullUrl = "{0}/{1}".format(self.url, url)
        return requests.get(fullUrl, headers=self.togglHeaders, auth=self.togglAuth)
        
    def post(self, url, data=None):
        """ Send a post request to the url provided """
        fullUrl = "{0}/{1}".format(self.url, url)
        return requests.post(fullUrl, headers=self.togglHeaders, auth=self.togglAuth, data=json.dumps(data))
        
    def put(self, url, data=None):
        """ Send a put request to the url provided """
        fullUrl = "{0}/{1}".format(self.url, url)
        return requests.put(fullUrl, headers=self.togglHeaders, auth=self.togglAuth, data=json.dumps(data))