import requests
import json

def jprint(obj):
    # Create a formatted string of a Python JSON object

    text = json.dumps(obj,sort_keys=True,indent = 4)

    print(text)

response = requests.get('http://192.168.54.102/api/sensor/action-triggers')

print(response.status_code)

jprint(response.json())