#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_data import UserData

ORIGIN_CITY_IATA = "MEX"
phone_number = ""

def register():
    print(
        "Welcome to Luis's Flight Club.\nWe find the best flight deals and email you."
    )
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    error = True
    while error:
        email = input("What is your email?\n")
        if(email == input("Type your email again.\n")):
            error = False
        else:
            print("different emails, try again.")
    ud = UserData(first_name,last_name,email)
    return ud

def main():
    
    dm = DataManager()
    fs = FlightSearch()
    nm = NotificationManager()

    user = register()
    dm.post("users",user)
    users = dm.get("users")

    data = dm.get("prices")
    cities = []
    for city in data:
        # Put IATA for all the new cities added to google sheet
        if city['iataCode'] == "":
            IATA = fs.get_IATA(city['city'])
            city['iataCode'] = IATA
            dm.put("prices",city)

        best_flight = fs.search(ORIGIN_CITY_IATA, city['iataCode'])
        
        if best_flight is not None and best_flight.price < city['lowestPrice']:
            city['lowestPrice'] = best_flight.price
            dm.put("prices",city)
            for user in users:
                nm.send_email(f"{user['email']}","Low price alert!",f"Only ${best_flight.price} to fly from {best_flight.city_from}-{best_flight.fly_from} to {best_flight.city_to}-{best_flight.fly_to}, from {best_flight.departure} to {best_flight.comeback}.")


if __name__ == "__main__":
    main()
