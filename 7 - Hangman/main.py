#Step 1 



lives = 6
#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
from hangman_words import word_list

chosen_word = word_list[random.randint(0,len(word_list) - 1)].lower()

from hangman_art import logo, stages

print(logo)

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# #TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# #TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# #Step 2

# #TODO-1: - Create an empty List called display.
# #For each letter in the chosen_word, add a "_" to 'display'.
# #So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# #TODO-2: - Loop through each position in the chosen_word;
# #If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# #e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

# #TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# #Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
# print(display)

#Step 3

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

#Step 4

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

#Create blanks
display = []
for letter in chosen_word:
    display.append("_") 

actual_word = "".join(display)
guessed_correct = False

while(actual_word != chosen_word  and lives > 0):
    guess = input("\nGuess a letter: ").lower()

    if(guess in display):
        guessed_correct
    else:
        #Check guessed letter
        for position in range(len(chosen_word)):
            if guess == chosen_word[position]:
                display[position] = guess
                guessed_correct = True


    if (not guessed_correct):    
        #TODO-2: - If guess is not a letter in the chosen_word,
        #Then reduce 'lives' by 1. 
        #If lives goes down to 0 then the game should stop and it should print "You lose."
        lives -= 1

    #Join all the elements in the list and turn it into a String.
    actual_word = "".join(display)
    #Check if user has got all letters.

    if lives > 0 and not guessed_correct:
        #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
        print(stages[lives])

    print(display)

    if actual_word == chosen_word and lives > 0:
        print("You win.")
        lives = 0
    elif lives == 0:
        print(stages[lives])
        print(f"You lose.\nthe word was {chosen_word}")
       
    guessed_correct = False