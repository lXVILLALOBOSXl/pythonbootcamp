import random

def play(number_to_guess,DIFFICULTY):
    if DIFFICULTY == "hard":
        attemps = 5
    else:
        attemps = 10
    
    while attemps > 0:
        print(f"You have {attemps} attempts remaining to guess the number.")
        given_number = int(input("Make a guess: "))
        if given_number < number_to_guess:
            print("Too low.\nGuess again.")
            attemps -= 1
        elif given_number > number_to_guess:
            print("Too high.\nGuess again.")
            attemps -= 1
        else:
            attemps = -1
    
    if attemps == 0:
        print("You've run out of guesses, you lose.")
    else:
        print(f"You got it! The answer was {number_to_guess}.")

from art import logo
print(logo + "\nWelcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
playing = True


while playing:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    number_to_guess = random.randint(1,100)
    print(f"Pssst, the correct answer is {number_to_guess}")
    if difficulty == "easy" or difficulty == "hard":
        play(number_to_guess,difficulty)
        playing = False
    else:
        print("Incorrect answer, try again")


