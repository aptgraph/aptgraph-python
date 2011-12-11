import json
from urllib2 import urlopen, HTTPError


class PyAptgraph(object):

    def __init__(self, apiKey, debug=False):
        '''
        Connect to the Aptgraph API

        @param string $apikey Your Aptgraph apikey
        @param boolean $debug Turn on/off debugging messages
        '''
        self.apiKey = apiKey
        self.debug = debug
        self.version = 0.3
        self.errorMessage = ''
        self.errorCode = ''
        self.apiUrl = 'http://aptgraph.cascade/api/v1/'

        # Default to a 300 second timeout on server calls
        self.timeout = 300

        # This will hold the requests until they are sent
        self.payLoad = []

    def add(self, graphid, value, timestamp=False):
        '''
        Add a stat (value) to a graph

        @param string graphid the id of the graph to add the value to
        @param number value the numeric value to add to the graph
        @param string If you want you can pass a timestamp
        @return boolean True on success
        '''
        params = {}
        params["section"] = 'statistic'
        params["action"] = 'add'
        params["graphid"] = graphid
        params["value"] = value
        params["apikey"] = self.apiKey

        if timestamp != False:
            params["timestamp"] = timestamp

        # Save the item into payLoad
        self.payLoad.append(params)

    def send(self):
        '''
        Compile the pay load into JSON and send it to the API.

        '''
        # Send the data via POST as JSON
        jsonData = json.dumps(self.payLoad)

        # Make sure the content-type is set to JSON
        headers = {'content-type': 'application/json',
            'User-Agent': 'PyAptgraph v.%s' % self.version}

        try:
            reqest = urllib2.Request(self.apiUrl, jsonData, headers)
            response = urllib2.urlopen(reqest)
            if self.debug:
                print response.read()
        except HTTPError, e:
            print(e.read())

        if self.debug:
            print 'Request sent and received successfully...'
