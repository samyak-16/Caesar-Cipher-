import os
import string

ALPHABET = string.ascii_uppercase


def welcome():
    """
    display a welcome message
    """
    print("Welcome to the Caesar Cipher")
    print("This program encrypts and decrypts text with the Caesar Cipher.")


def get_shift():
    """
    prompt the user for a valid shift number.

    Returns:
        int: The shift value.
    """
    while True:
        try:
            shift = int(input("What is the shift number: "))
            return shift
        except ValueError:
            print("Invalid Shift")


def enter_message():
    """
    Prompt the user for mode, message and shift.

    Returns:
        tuple: (mode, message, shift)
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

        if mode in ("e", "d"):
            break

        print("Invalid Mode")

    if mode == "e":
        message = input("What message would you like to encrypt: ").upper()
    else:
        message = input("What message would you like to decrypt: ").upper()

    shift = get_shift()

    return mode, message, shift


def encrypt(message, shift):
    """
    Encrypt a message using Caesar Cipher.

    Args:
        message (str): Message to encrypt.
        shift (int): Shift amount.

    Returns:
        str: Encrypted message.
    """
    encrypted_message = ""

    for character in message.upper():
        if character not in ALPHABET:
            encrypted_message += character
        else:
            index = ALPHABET.index(character)
            new_index = (index + shift) % 26
            encrypted_message += ALPHABET[new_index]

    return encrypted_message


def decrypt(message, shift):
    """
    Decrypt a Caesar Cipher message.

    Args:
        message (str): Message to decrypt.
        shift (int): Shift amount.

    Returns:
        str: Decrypted message.
    """
    decrypted_message = ""

    for character in message.upper():
        if character not in ALPHABET:
            decrypted_message += character
        else:
            index = ALPHABET.index(character)
            new_index = (index - shift) % 26
            decrypted_message += ALPHABET[new_index]

    return decrypted_message


def process_file(filename, mode, shift):
    """
    Read messages from a file and process them.

    Args:
        filename (str): Input filename.
        mode (str): 'e' or 'd'.
        shift (int): Shift amount.

    Returns:
        list: Processed messages.
    """
    processed_messages = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if mode == "e":
                processed_messages.append(encrypt(line, shift))
            else:
                processed_messages.append(decrypt(line, shift))

    return processed_messages


def is_file(filename):
    """
    Check if a file exists.

    Args:
        filename (str): Filename to check.

    Returns:
        bool: True if file exists.
    """
    return os.path.isfile(filename)


def write_messages(messages):
    """
    Write messages to results.txt.

    Args:
        messages (list): Messages to write.
    """
    with open("results.txt", "w", encoding="utf-8") as file:
        for message in messages:
            file.write(message + "\n")


def message_or_file():
    """
    Gather information about processing method.

    Returns:
        tuple: (mode, message, filename)
    """
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()

        if mode in ("e", "d"):
            break

        print("Invalid Mode")

    while True:
        source = input(
            "Would you like to read from a file (f) or the console (c)? "
        ).lower()

        if source in ("f", "c"):
            break

        print("Invalid Option")

    if source == "c":
        if mode == "e":
            message = input("What message would you like to encrypt: ").upper()
        else:
            message = input("What message would you like to decrypt: ").upper()

        return mode, message, None

    while True:
        filename = input("Enter a filename: ")

        if is_file(filename):
            return mode, None, filename

        print("Invalid Filename")


def main():
    """
    Main program loop.
    """
    welcome()

    while True:
        mode, message, filename = message_or_file()

        shift = get_shift()

        if filename is not None:
            processed_messages = process_file(filename, mode, shift)

            write_messages(processed_messages)

            print("Output written to results.txt")

        else:
            if mode == "e":
                print(encrypt(message, shift))
            else:
                print(decrypt(message, shift))

        while True:
            choice = input(
                "Would you like to encrypt or decrypt another message? (y/n): "
            ).lower()

            if choice in ("y", "n"):
                break

            print("Invalid Option")

        if choice == "n":
            print("Thanks for using the program, goodbye!")
            break


main()
