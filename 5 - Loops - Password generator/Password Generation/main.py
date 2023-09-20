#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
import random


password = ""
i = 0
word_len = nr_letters + nr_symbols + nr_numbers
while i < word_len:

    ran = random.randint(0,2)

    if ran == 0:
        if nr_letters == 0:
            i
        else:
            nr_letters -= 1
            password += letters[random.randint(0,len(letters) - 1)]
            i += 1
    elif ran == 1:
        if nr_symbols == 0:
            i
        else:
            nr_symbols -= 1
            password += symbols[random.randint(0,len(symbols) - 1)]
            i += 1
    elif ran == 2:
        if nr_numbers == 0:
            i
        else:
            nr_numbers -= 1
            password += numbers[random.randint(0,len(numbers) - 1)]
            i += 1

print(password)