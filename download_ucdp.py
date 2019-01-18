'''
    download.py: Code for fetching data from a REST API.
    This script uses real UCDP data: http://ucdp.uu.se/apidocs/
    Only to be used for educational purposes. Distribution or publication without
    written permission from the author is not allowed.
    Written by Teun van Gils. All rights reserved, 2016.
'''

from urllib import parse, request
import json

def request_page(**kwargs):
    '''Request a page of data from the UCDP database.'''

    # Below are the parameters for the REST request
    # Information about possible parameters can be found at:
    #   http://ucdp.uu.se/apidocs/
    kwargs['page'] = 0 if 'page' not in kwargs else kwargs['page']
    kwargs['pagesize'] = 1000 if 'pagesize' not in kwargs else kwargs['pagesize']
    req_string = parse.urlencode(kwargs) # will encode the parameters in the right format

    # Below, we prepare the request to the REST webpage that will return our data
    req = request.Request('http://ucdpapi.pcr.uu.se/api/gedevents/5.0?' + req_string)

    # Submit the request and retrieve the response:
    with request.urlopen(req) as rawdata:
        data = rawdata.read().decode('utf8') # decode the raw response
        response = json.loads(data) # parse the json from the response

    return response

# Request some data from the online database
result = request_page(page=0, pagesize=1000, country=482)

with open('sample.json', 'w') as file: # open a file for writing
    json.dump(result, file, indent=4) # save the result as json in this file
