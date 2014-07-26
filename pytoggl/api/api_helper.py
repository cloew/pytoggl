
class ApiHelper:
    """ Helper class to perform Toggl API requests """
    
    def __init__(self, apiToken=None):
        """ Initialize the API Helper """
        self.requestHelper = RequestHelper(apiToken)
        self.processor = {True:self.processResponseData,
                          False:self.processResponse}
        
    def get(self, url, getData=False):
        """ Return the response JSON from a get request """
        response = self.requestHelper.get(url)
        self.processor[getData](response)
        
    def put(self, url, data=None, getData=False):
        """ Return the response JSON from a get request """
        response = self.requestHelper.put(url, data=data)
        self.processor[getData](response)
        
    def post(self, url, data=None, getData=False):
        """ Return the response JSON from a get request """
        response = self.requestHelper.post(url, data=data)
        self.processor[getData](response)
    
    def processResponse(self, response):
        """ Process a given response """
        if response.status_code == 200:
            return response.json()
        else:
            pass
            # Raise Exception
            
    def processResponseData(self, response):
        """ Process the given response for its data """
        json = self.processResponse(response)
        if json["data"] is not None:
            return json["data"]
        else:
            pass
            # Raise Exception