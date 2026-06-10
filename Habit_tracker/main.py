import requests
import os
from datetime import datetime

TOKEN = os.getenv("TOKEN")
USERNAME = os.getenv("USERNAME")


pixela_endpoint = "https://pixe.la/v1/users"
user_params ={
    "token": TOKEN,
    "username" : USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",
}

#response = requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)

graph_endpoints = f"{pixela_endpoint}/{USERNAME}/graphs"

header = {
    "X-USER-TOKEN": TOKEN
}

graph_params = {
    "id": "graphtest1",
    "name": "test_graph",
    "unit": "unit",
    "type": "float",
    "color": "shibafu"
}

#response = requests.post(url=graph_endpoints,json=graph_params,headers=header)
#print(response.text)

pixel_creation_endpoints= f"{graph_endpoints}/graphtest1"

today = datetime.now()

pixel_creation_params ={
    "date" : today.strftime("%Y%m%d"),
    "quantity": "5",
}

response = requests.post(url=pixel_creation_endpoints,json=pixel_creation_params,headers=header)
print(response.text)