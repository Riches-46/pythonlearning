import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
jsonprac = json.loads(response.text)
jsonstr = json.dumps(jsonprac, indent = 4)
with open("api response.json", "w") as f:
    f.write(jsonstr)