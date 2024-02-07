import requests
import os
from flight_data import FlightData
from user_data import UserData
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    #Sheety API data
    SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
    PROJECT_NAME = os.environ.get("PROJECT_NAME")
    BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
    SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}"

    #Bearer Token Authentication
    sheety_headers = {
        "Authorization": BEARER_TOKEN
    }    

    def post(self,sheety_name,user:UserData):
        try:   
            # This will try to add info to google sheet from Sheety
            response = requests.post(
                url=f"{DataManager.SHEETY_ENDPOINT}/{sheety_name}", 
                json= {
                    "user":{
                        "firstName":user.first_name,
                        "lastName":user.last_name,
                        "email":user.email
                    }
                }, 
                headers=DataManager.sheety_headers
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # Prints the HTTP status code and the reason
            print(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
        except requests.exceptions.RequestException as e:
            # Catches other Requests-related exceptions
            print(f"Error occurred: {e}")
        except Exception as e:
            # Catches any other exceptions
            print(f"An unexpected error occurred: {str(e)}")
        else:
                print("You're in the club!")
        pass     

    def put(self,sheety_name,flight:FlightData):
        try:   
            # This will try to add info to google sheet from Sheety
            response = requests.put(
                url=f"{DataManager.SHEETY_ENDPOINT}/{sheety_name}/{flight['id']}", 
                json= {
                    "price":flight
                }, 
                headers=DataManager.sheety_headers
            )
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # Prints the HTTP status code and the reason
            print(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
        except requests.exceptions.RequestException as e:
            # Catches other Requests-related exceptions
            print(f"Error occurred: {e}")
        except Exception as e:
            # Catches any other exceptions
            print(f"An unexpected error occurred: {str(e)}")
        else:
            print(f"Fly {flight['id']} edited succesfully")

    def get(self, sheety_name):
        try:
            response = requests.get(url = f"{DataManager.SHEETY_ENDPOINT}/{sheety_name}", headers=DataManager.sheety_headers)
            response.raise_for_status()
            data = None
            if response.status_code == 200:
                data = response.json()[sheety_name]
                # Do something with the data
        except requests.exceptions.HTTPError as e:
            # Prints the HTTP status code and the reason
            print(f"HTTP Error: {e.response.status_code} - {e.response.reason}")
        except requests.exceptions.RequestException as e:
            # Catches other Requests-related exceptions
            print(f"Error occurred: {e}")
        except Exception as e:
            # Catches any other exceptions
            print(f"An unexpected error occurred: {str(e)}")
        else:
                return data



    pass