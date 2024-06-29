import requests
from pprint import pprint
"""
HTTP Request -> HTML Response
REST API HTTP Request -> JSON Response
"""


# URL from which we can rach the API
endpoint = "http://localhost:8000/api"
print("Sending Response")
resp = requests.get(endpoint) # sending the request
# resp = requests.get(endpoint, json = {"query" : "Hello World"}) # sending request with some data
# print(f"{type(resp.text)} : \n{resp.text}") # prints the resp json as string
print(resp.json())
# pprint(resp.text) # prints the resp json as dictionary
# print(f"Resp status code -> {resp.status_code}") # used for debugging purpose after getting response