alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(text, shift):

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

    encoded_word = ""
    
    for letter in text:
        new_index = alphabet.index(letter) + shift

        if(new_index > len(alphabet) - 1):
            new_index = (len(alphabet) - new_index)

        encoded_word += alphabet[new_index]

    print(f"The encoded text is {encoded_word}")


#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(text, shift):

  #TODO-2: Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.  
  #e.g. 
  #cipher_text = "mjqqt"
  #shift = 5
  #plain_text = "hello"
  #print output: "The decoded text is hello"
    decoded_word = ""
    
    for letter in text:
        new_index = alphabet.index(letter) - shift

        if(new_index < 0):
            new_index = (new_index + len(alphabet))

        decoded_word += alphabet[new_index]

    print(f"The decoded text is {decoded_word}")

def caesar(text,shift,direction):
    if (direction == "encode"):
        encrypt(text,shift)
    elif (direction == "decode"):
        decrypt(text,shift)

from art import logo

print(logo)

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if (direction == "encode" or direction == "decode"):
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text,shift,direction)
    else:
        print("Wrong answer")

    

    play_again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if play_again == "yes":
        continue
    else:
        break

