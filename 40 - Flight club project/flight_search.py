from datetime import datetime, timedelta
from flight_data import FlightData
import requests
import os

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    #Tequila API data
    TEQUILA_KEY = os.environ.get("TEQUILA_KEY")
    TEQUILA_LOCATION_ENDPOINT = "https://tequila-api.kiwi.com"
    TEQUILA_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2"

    tequila_headers = {
        "apikey": TEQUILA_KEY
    }

    def get_IATA(self, city_name):
        try:
            location_endpoint = f"{FlightSearch.TEQUILA_LOCATION_ENDPOINT}/locations/query"
            query = {"term": city_name, "location_types": "city"}
            response = requests.get(url=location_endpoint, headers=FlightSearch.tequila_headers, params=query)
            response.raise_for_status()
            data = None
            if response.status_code == 200:
                results = response.json()["locations"]
                data = results[0]["code"]
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
        
    def search(self, fly_from, fly_to):
        try:
            location_endpoint = f"{FlightSearch.TEQUILA_SEARCH_ENDPOINT}/search"
            
            date_from = (datetime.now() + timedelta(days=1)).strftime('%d/%m/%Y')
            date_to = (datetime.now() + timedelta(days=183)).strftime('%d/%m/%Y')
            query = {
                "fly_from": fly_from, 
                "fly_to": fly_to, 
                "date_from": date_from, 
                "date_to": date_to,
                "nights_in_dst_from": 7,
                "nights_in_dst_to": 28,
                "flight_type": "round",
                "one_for_city": 1,
                "max_stopovers": 0,
                "curr": "MXN"
            }
            
            response = requests.get(url=location_endpoint, headers=FlightSearch.tequila_headers, params=query)
            response.raise_for_status()

            data = None
            if response.status_code == 200:
                results = response.json()["data"]
                data = results[0]

                flight = FlightData(
                    fly_from,
                    data["cityFrom"],
                    fly_to,
                    data["cityTo"],
                    data["price"],
                    data["route"][0]["local_departure"].split("T")[0],
                    data["route"][1]["local_departure"].split("T")[0]
                )
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None
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
            return flight
    pass