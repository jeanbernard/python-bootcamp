import caesar_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_len = len(alphabet)

def show_start_screen():
    print(caesar_art.logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    return direction, text, shift

def reset(decision):
    if decision == 'yes':
        direction, text, shift = show_start_screen()
        caesar(text, shift, direction)

def caesar(text, shift, direction):
    rslt_text = ""

    if direction == "encode":
        for char in text:
            if char not in alphabet:
                rslt_text += char
                continue

            cipher_idx = alphabet.index(char) + shift
            if cipher_idx >= alphabet_len:
                cipher_idx = cipher_idx - alphabet_len
            rslt_text += alphabet[cipher_idx]

    elif direction == "decode":
        for char in text:
            if char not in alphabet:
                rslt_text += char
                continue

            cipher_idx = alphabet.index(char) - shift
            if cipher_idx < 0:
                cipher_idx = cipher_idx + alphabet_len
            rslt_text += alphabet[cipher_idx]

    print(f"The {direction}d text is {rslt_text}")
    restart = input("Restart program? 'yes' or 'no' ").lower()
    reset(restart)

direction, text, shift = show_start_screen()
caesar(text, shift, direction)
