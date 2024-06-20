from dict import morse

def encode(message:str):
    code = []
    for letter in message:
        code.append(morse[letter])
    return code

def main():
    message = input('Write a message: ')
    message = message.lower()
    code = encode(message)
    print(f'message in morse is: {code}')
    pass

if __name__ == '__main__':
    main()

# if __name__ == '__main__':
#     main()

# from dict import morse

# def encode(message: str) -> list:
#     return [morse[letter] for letter in message]

# def main():
#     message = input('Write a message: ').lower()
#     code = encode(message)
#     print(f'Message in Morse code is: {code}')

# if __name__ == '__main__':
#     main()