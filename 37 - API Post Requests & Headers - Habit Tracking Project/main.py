import requests
from datetime import datetime

# !!!!get RECOVER INFO in the api, it returns the info that we wanted
# !!!!Post MAKE A QUERY in the api, it returns if it was succesfuly or not
# !!!!Put EDIT INFO in the api, it returns if it was succesfuly or not
# !!!!delete DELETE INFO in the api, it returns if it was succesfuly or not

# Make a query to create a User in pixela
PIXELA_USERNAME = "lvillalobos17"
PIXELA_TOKEN = ""
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_USER_PARAMS = {
    "token":PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": 'yes',
    "notMinor": "yes"
}

response = requests.post(url=PIXELA_ENDPOINT, json=PIXELA_USER_PARAMS)

# Make a query to create a Graph in pixela
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
PIXELA_GRAPH_ID = "graph1"
PIXELA_GRAPH_PARAMS = {
    "id":PIXELA_GRAPH_ID,
    "name": "Studying Graph",
    "Unit": "Minutes",
    "Type": "int",
    "color": "ajisai"
}
PIXELA_GRAPH_HEADERS = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.post(url=PIXELA_GRAPH_ENDPOINT,json=PIXELA_GRAPH_PARAMS, headers=PIXELA_GRAPH_HEADERS)

# Make a query to create a Graph point in pixela
PIXELA_PIXEL_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{PIXELA_GRAPH_ID}"
today = datetime.now()
formatted_date = today.strftime('%Y%m%d')
PIXELA_PIXEL_PARAMS = {
    "date":formatted_date,
    "quantity": input("How many days did you study today? : "),
}

response = requests.post(url=PIXELA_PIXEL_ENDPOINT,json=PIXELA_PIXEL_PARAMS, headers=PIXELA_GRAPH_HEADERS)

# # Make a query to edit a Graph point in pixela
# PIXELA_EDIT_PIXEL_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{PIXELA_GRAPH_ID}/{formatted_date}"
# PIXELA_EDIT_PIXEL_PARAMS = {
#     "quantity": "35",
# }

# response = requests.put(url=PIXELA_EDIT_PIXEL_ENDPOINT,json=PIXELA_EDIT_PIXEL_PARAMS, headers=PIXELA_GRAPH_HEADERS)


# # Make a query to delete a Graph point in pixela
# PIXELA_DELETE_PIXEL_ENDPOINT = f"{PIXELA_GRAPH_ENDPOINT}/{PIXELA_GRAPH_ID}/{formatted_date}"

# response = requests.delete(url=PIXELA_DELETE_PIXEL_ENDPOINT, headers=PIXELA_GRAPH_HEADERS)
# print(response.text)