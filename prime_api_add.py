#!/usr/bin/env python3

import requests
import json
from requests.auth import HTTPBasicAuth

with open('/path/to/primecreds.json') as credentials:
    creds = json.load(credentials)
    
with open('/path/to/devices.json') as device:
    dev = json.load(device)
    
username = creds['username']
password = creds['password']

auth = HTTPBasicAuth(username, password)

# Currently this only supports adding a device at a time. Will need to work to allow multiple device additions
add_device = {'devicesImport': {'devices': {'device': {dev}}}}

headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
response = requests.put('https://x.x.x.x/webacs/api/v1/op/devices/bulkImport.json',
                        verify=False, auth=auth, json=add_device, headers=headers)

if response.status_code == 200:
    job_name = response.json()['mgmtResponse']['bulkImportResult']['jobName']
    print(job_name)

else:
    print(response.status_code)
    print(response.text)
