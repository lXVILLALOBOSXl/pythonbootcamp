rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
modes = [rock, paper, scissors]

option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

print(modes[option] + "\n\nComputer chose:\n\n")

computer_option = random.randint(0, len(modes) - 1)

print(modes[computer_option])

if (option == 0):
    if(computer_option == 1):
        print("\nYou lose\n")
    elif (computer_option == 2):
        print("\nYou win\n")
    else:
        print("\nTie\n")
if (option == 1):
    if(computer_option == 2):
        print("\nYou lose\n")
    elif (computer_option == 0):
        print("\nYou win\n")
    else:
        print("\nTie\n")
if (option == 2):
    if(computer_option == 0):
        print("\nYou lose\n")
    elif (computer_option == 1):
        print("\nYou win\n")
    else:
        print("\nTie\n")

