# -*- coding: utf8 -*-
import requests
import json

#API URL with parameters
BASE_URL = 'https://[HOSTNAME].bridgeapp.com'
url = BASE_URL + '/api/admin/reports/' + 'SignInReport' #this is the API URI plus payload

#API Authorization in base64 format
base64string =  '[BASE_64_STRING]'

#header with authorization to access the Bridge API
bridgeHeaders = {'content-type': 'application/json', 'Authorization': 'Basic ' + str(base64string)}


#call where json is the data type sent as the payload. The response is captured in bridgeResponse
bridgeResponse = requests.get(url, headers=bridgeHeaders)

print("Bridge Response: " + str(bridgeResponse.text))

#Write Response to file
file = open('SignInReport.json','w') 
file.write('Status Code: ' + str(bridgeResponse.status_code) + '\nResponse Body ' + str(bridgeResponse.text))
file.close() 