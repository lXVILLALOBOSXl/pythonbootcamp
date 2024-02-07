class FlightData:
    #This class is responsible for structuring the flight data.

    def __init__(self, fly_from, city_from, fly_to, city_to, price, departure, comeback):
        self.fly_from = fly_from       # IATA code of the departure airport
        self.city_from = city_from     # Name of the departure city
        self.fly_to = fly_to           # IATA code of the arrival airport
        self.city_to = city_to         # Name of the arrival city
        self.price = price             # Price of the flight
        self.departure = departure     # Departure date and time
        self.comeback = comeback      # Arrival date and time

    def __str__(self):
        return (f"FlightData(fly_from='{self.fly_from}', city_from='{self.city_from}', "
                f"fly_to='{self.fly_to}', city_to='{self.city_to}', price={self.price}, "
                f"departure='{self.departure}', return='{self.comeback}')")

    pass