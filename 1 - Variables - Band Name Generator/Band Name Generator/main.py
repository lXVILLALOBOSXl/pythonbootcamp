print("Welcome to the Band Name Generator.")

#The following sentence is the same like make it like this: 

# city_name = input("What's the name of the city you grew up in?\n")
# print("Your band name could be " + city_name)
# >>Your band name could be city_name

#The way that python executes the function into a function and concat is:
#First, executes the functions into the function, next save the result as
#varaible to use in the main function

print("Your band name could be " + input("What's name of the city you grew up in?\n") +
      " " + input("What's your pet's name?\n"))
