import requests

USERNAME = "selennzl"
TOKEN = "sO08KYH67n26"
GRAPH_ID = "bookgraph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "100 Pages of Book",
    "unit": "pages",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_config = {
    "date": "20211203",
    "quantity": "126"
}

graph_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
# this endpoint is also the pixel endpoint url

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response = requests.put(url=graph_update_endpoint, json=graph_config, headers=headers)
response = requests.post(url=graph_update_endpoint, json=pixel_config, headers=headers)
print(response.text)
