import requests
import pprint


request = requests.get("https://api.spacexdata.com/v3/launches/1")
print(request.json())
print(request.headers)
print(request.text)


if(request.status_code == 200):
    print("Valid Link")