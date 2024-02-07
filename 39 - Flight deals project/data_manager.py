import requests
import os
class DataManager:
    #This class is responsible for talking to the Google Sheet.

    #Sheety API data
    SHEETY_USERNAME = os.environ.get("SHEETY_USERNAME")
    PROJECT_NAME = os.environ.get("PROJECT_NAME")
    SHEET_NAME = os.environ.get("SHEET_NAME")
    BEARER_TOKEN = os.environ.get("BEARER_TOKEN")
    SHEETY_ENDPOINT = f"https://api.sheety.co/{SHEETY_USERNAME}/{PROJECT_NAME}/{SHEET_NAME}"

    #Bearer Token Authentication
    sheety_headers = {
        "Authorization": BEARER_TOKEN
    }     

    def put(self,flight):
        try:   
            # This will try to add info to google sheet from Sheety
            response = requests.put(
                url=f"{DataManager.SHEETY_ENDPOINT}/{flight['id']}", 
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

    def get(self):
        try:
            response = requests.get(url = DataManager.SHEETY_ENDPOINT, headers=DataManager.sheety_headers)
            response.raise_for_status()
            data = None
            if response.status_code == 200:
                data = response.json()['prices']
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