#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = "MEX"
phone_number = ""

def main():
    dm = DataManager()
    fs = FlightSearch()
    nm = NotificationManager()

    data = dm.get()
    cities = []
    for city in data:
        # Put IATA for all the new cities added to google sheet
        if city['iataCode'] == "":
            IATA = fs.get_IATA(city['city'])
            city['iataCode'] = IATA
            dm.put(city)

        best_flight = fs.search(ORIGIN_CITY_IATA, city['iataCode'])
        
        if best_flight is not None and best_flight.price < city['lowestPrice']:
            city['lowestPrice'] = best_flight.price
            dm.put(city)
            nm.send_message(f"{phone_number}","Low price alert!",f"Only ${best_flight.price} to fly from {best_flight.city_from}-{best_flight.fly_from} to {best_flight.city_to}-{best_flight.fly_to}, from {best_flight.departure} to {best_flight.comeback}.")


    # Search the best fly prices for every city
    # for city in data:
    #     fs.search(ORIGIN_CITY_IATA, city['city'])

if __name__ == "__main__":
    main()
