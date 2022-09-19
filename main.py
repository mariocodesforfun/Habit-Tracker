# https://pixe.la/v1/users/franci/graphs/graph1.html -- graph url

from email import header
from math import pi
import requests
from datetime import datetime


TOKEN = "kjhoiudrfjksdgfucnoeakj"
USERNMAE = "franci"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNMAE,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}



# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


# https://pixe.la/@franci

# graph_endpoint = f"https://pixe.la/v1/{USERNMAE}-know/graphs"

graph_endpoint = f"{pixela_endpoint}/{USERNMAE}/graphs"


graph_config = {
    "id": "graph1",
    "name": "Running",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)        
# print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNMAE}/graphs/{GRAPH_ID}"


today = datetime(year=2022, month=9, day=18)
# print(today.strftime("%Y%m%d"))

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "9.4",

}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)



# UPDATE A PIXEL --- PUT REQUEST 

pixel_update_endpoint = f"{pixela_endpoint}/{USERNMAE}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_data = {
    "quantity": "4.7",

}


# response = requests.put(url=pixel_update_endpoint, json=update_data, headers=headers)
# print(response.text)


delete_endpoint = f"{pixela_endpoint}/{USERNMAE}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)

