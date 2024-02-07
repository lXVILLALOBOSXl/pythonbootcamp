class UserData:
    #This class is responsible for structuring the flight data.

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

    def __str__(self):
        return f"Person(first_name='{self.first_name}', last_name='{self.last_name}', email='{self.email}')"

    pass