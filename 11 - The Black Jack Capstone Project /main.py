cards = {
    "♥️":["A",2,3,4,5,6,7,8,9,"J","Q","K"],
    "♦️":["A",2,3,4,5,6,7,8,9,"J","Q","K"],
    "♣️":["A",2,3,4,5,6,7,8,9,"J","Q","K"],
    "♠️":["A",2,3,4,5,6,7,8,9,"J","Q","K"],
}

player = []
computer = []

def remove_card(key,index):
    cards[key].pop(index)

import random

def random_card(player,computer): 
    random_key = random.choice(list(cards.keys()))
    random_index = random.randint(0, len(cards[random_key]) - 1)
    random_value = cards[random_key][random_index]

    if random_value == "A":
        if not computer:
            random_value = str(input("How do you want to use it, as '1' or as '11': ")) + "A" 
        else:
            choice = random.randint(0,1)
            if choice == 1:
                random_value = "11A"
            else:
                random_value = "1A"

    remove_card(key=random_key,index=random_index)
    player.append(str(random_value)+random_key)

import re 

def get_points(player):
    points = 0
    for item in player:
        if "J" in item or "Q" in item or "K" in item:
            points = points + 10
        else: 
            points = points + int(re.search(r'\d+', item).group())
    return points



from art import logo
print(logo)

continue_playing = True

while continue_playing:
    cards = {
        "♥️":["A",2,3,4,5,6,7,8,9,"J","Q","K"],
        "♦️":["A",2,3,4,5,6,7,8,9,"J","Q","K"],
        "♣️":["A",2,3,4,5,6,7,8,9,"J","Q","K"],
        "♠️":["A",2,3,4,5,6,7,8,9,"J","Q","K"],
    }

    player = []
    computer = []

    more_cards = True

    random_card(player,computer=False)
    random_card(player,computer=False)
    print("Your cards: " + str(player))
    random_card(computer,computer=True)
    random_card(computer,computer=True)
    print("Computer's first card: ['" + str(computer[0]) + "']")
    
    while more_cards:
        option = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if option == 'y':
            random_card(player,computer=False)
            print("Your cards: " + str(player))
            random_card(computer,computer=True)
        else:
            more_cards = False
            print("Your final hand: " + str(player))
            print("Computer's final hand: " + str(computer))

        player_points = get_points(player)
        computer_points = get_points(computer)

        if computer_points >= 21 and more_cards:
            print("Computer's final hand: " + str(computer))
        elif more_cards:
            print("Computer cards: " + str(computer[0:len(player) - 1]))

        if player_points >= 21 or computer_points >= 21 or not more_cards:

            more_cards = False
            if (player_points > computer_points and player_points < 22) or computer_points > 21:
                print("You win")
            elif (player_points < computer_points and computer_points < 22) or player_points > 21:
                print("Computer win")
            else:
                print("Nobody win, was a tie")

    option = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if option != 'y':
        continue_playing = False 