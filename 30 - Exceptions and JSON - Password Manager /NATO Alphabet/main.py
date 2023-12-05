import pandas

data = pandas.read_csv("/Users/luisvillalobos/Documents/Programacion/Self Study/Udemy/Python Bootcamp/30 - Exceptions and JSON - Password Manager /NATO Alphabet/nato_phonetic_alphabet.csv")

phonetic_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

def generate_phonetic():
    word = input("Enter a word: ").upper()

    try:
        output_list = [phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)
    
generate_phonetic()
