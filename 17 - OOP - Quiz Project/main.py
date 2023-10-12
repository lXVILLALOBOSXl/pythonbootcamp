########Custom Class#######
class User:
    pass

#######Attributes##########

user_1 = User()
user_1.id = "001"
user_1.username = "Angela"

####Constructor#######
class User:

    def __init__(self, user_id, username):
        print("initialising new user....")
        self.id = user_id
        self.username = username
        print(f"{self.username} created.")

user_1 = User("001", "angela")
user_2 = User("002", "jack")

#####Defaults##########
class User:

    def __init__(self, user_id, username):
        self.followers = 0
        self.id = user_id
        self.username = username

user_1 = User("001", "angela")
print(user_1.followers)

#######Methods##########

class User:

    def __init__(self, user_id, username):
        self.followers = 0
        self.following = 0
        self.id = user_id
        self.username = username

    def follow(self, user):
        self.following += 1
        user.followers += 1
        print(f"Successfully followed {user.username}")

user_1 = User("001", "angela")
user_2 = User("002", "jack")
print(user_1.followers)
user_2.follow(user_1)
print(user_1.followers)