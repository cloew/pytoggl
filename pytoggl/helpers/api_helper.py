from .request_helper import RequestHelper

class ApiHelper:
    """ Helper class to perform Toggl API requests """
    
    def __init__(self, apiToken=None):
        """ Initialize the API Helper """
        self.requestHelper = RequestHelper(apiToken)
        
    def get(self, url):
        """ Return the response JSON from a get request """
        response = self.requestHelper.get(url)
        return self.process(response)
        
    def put(self, url, data=None):
        """ Return the response JSON from a get request """
        response = self.requestHelper.put(url, data=data)
        return self.process(response)
        
    def post(self, url, data=None):
        """ Return the response JSON from a get request """
        response = self.requestHelper.post(url, data=data)
        return self.process(response)
        
    def delete(self, url):
        """ Return the response success from a delete request """
        response = self.requestHelper.delete()
        return response.status_code == 200
    
    def process(self, response):
        """ Process a given response """
        if response.status_code == 200:
            json = response.json()
            if type(json) == list:
                return json
            else:
                return self.processData(json)
        else:
            pass
            # Raise Exception
            
    def processData(self, json):
        """ Process the given json for its data """
        if json["data"] is not None:
            return json["data"]
        else:
            pass
            # Raise Exception