import requests
import json

def jprint(obj):
    # Create a formatted string of a Python JSON object

    text = json.dumps(obj,sort_keys=True,indent = 4)

    print(text)

def fileWrite(obj):
    file = open("response.json", "w+")
    text = json.dumps(obj,sort_keys=True, indent = 4)
    file.write(text)
    file.close()

requests.delete('http://192.168.54.102/api/sensor/action-triggers')
response = requests.get('http://192.168.54.102/api/sensor/action-triggers')

#print(response.status_code)
jprint(response.json())

actionTrigger = {
                    "uuid": "3f26aff4-8650-42a0-b319-51776c443fbc",
                    "event": "trigger_0_edge_falling",
                    "actions": [
                        {
                            "name": "enable_switching_output",
                            "arguements": {}
                        }
                    ]
                }
headers =  {"Content-Type":"application/json"}

requests.post('http://192.168.54.102/api/sensor/action-triggers', data = json.dumps(actionTrigger), headers = headers)

response = requests.get('http://192.168.54.102/api/sensor/action-triggers')
print(response.status_code)
jprint(response.json())

fileWrite(response.json())