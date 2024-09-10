alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def shift():

    offset = int(input("Enter the shift offset (positive for right shift, negative for left shift):\n"))
    message = input("Input the message you would like encrypted:\n")
    new_message = ''

    for letter in message:
        letter = letter.lower()

        if letter.isalpha():
            shift_pos = (alphabet.index(letter) + offset) % 26
            new_pos = alphabet[shift_pos]
            new_message += new_pos

        elif letter.isspace() or letter.isnumeric(): 
            new_message += letter
        else:
            print(f"An unexpected character '{letter}' was found. Skipping.")

    print(f"Encrypted message: {new_message}")

shift()
