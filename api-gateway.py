import requests
import json
import sys
if len(sys.argv) < 2:
    print("Please pass the url as the parameter")
    
else:
    url = str(sys.argv[1])
    param = {"url":url}
    result = requests.get(url="https://6icve49zni.execute-api.us-west-2.amazonaws.com/default/crawler",params=param)
    print(result.json())