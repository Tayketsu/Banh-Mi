##############################################################################
# libaries for connecting to server and using JSON
import http.client
import json


##############################################################################
###### Functions to communicate with server #######

def send_recbook_to_server(recbook):
    
    # Create Connection
    headers = {'Content-type': 'application/json'}
    c = http.client.HTTPConnection('localhost', 8080)
    
    # Send request and listen for result (true if successfull)
    c.request('POST', '/recbook', json.dumps(recbook), headers)
    return json.loads(c.getresponse().read())







## Example:
# =============================================================================
# dummy = {"name":"abc"}
# headers = {'Content-type': 'application/json'}
# 
# c = http.client.HTTPConnection('localhost', 8080)
# c.request('POST', '/recbook', json.dumps(dummy), headers)
# doc = c.getresponse().read()
# print(doc)
# #thisdict = json.loads(doc)
# #print(thisdict["model"])
# input("Press Enter to continue...")
# 
# =============================================================================