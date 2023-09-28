from art import logo, vs
from gamedata import data

import random
def get_random_datum():
    return random.choice(data)

def delete_datum(data,datum):
    data.remove(datum)

def add_datum(data,datum):
    data.append(datum)

import os
def clear_screen():
    os.system('clear')

def game():
    score = 0
    game_over = False
    incorrect_option = True


    while(not game_over):
        clear_screen()
        print(logo)
        if score > 0:
            print(f"You're right! Current score: {score}.")
        
        if not score > 0:
            datumA = get_random_datum()
        else:
            datumA = datumB

        print(f"Compare A: {datumA['name']}, {datumA['description']}, from {datumA['country']}")
        delete_datum(data,datumA)
        
        datumB = get_random_datum()
        print(F"{vs}\nAgainst B: {datumB['name']}, {datumB['description']}, from {datumB['country']}")
        add_datum(data,datumA)

        while(incorrect_option):
            selection = input("Who has more followers? Type 'A' or 'B': ").lower()
            if selection == 'a':
                incorrect_option = False
                if datumA['follower_count'] > datumB['follower_count']:
                    score += 1
                else:
                    game_over = True
            elif selection == 'b':
                print(logo)
                incorrect_option = False
                if datumB['follower_count'] > datumA['follower_count']:
                    score += 1
                else:
                    game_over = True
            else: 
                print("Incorrect option, please try again")

        incorrect_option = True
        
    clear_screen()
    print(logo)
    print(F"Sorry, that's wrong. Final score: {score}")

game()