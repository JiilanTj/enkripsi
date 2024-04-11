import random

def shuffle_key(key):
    # Randomizes the order of characters in a key
    key_list = list(key)
    random.shuffle(key_list)
    shuffled_key = ''.join(key_list)
    return shuffled_key

def crypto_encrypt(text, key):
    # Randomize the keys before use
    shuffled_key = shuffle_key(key)
    encrypted_text = ""

    for i, char in enumerate(text):
        # Adds the Unicode value of a text character to the Unicode value of a key character
        encrypted_char = ord(char) + ord(shuffled_key[i % len(shuffled_key)])

        # If the Unicode value exceeds 1114111 (Unicode limit), subtract 1114111
        if encrypted_char > 1114111:
            encrypted_char -= 1114111

        # Convert encrypted Unicode values back to characters
        encrypted_text += chr(encrypted_char)

    return encrypted_text

def crypto_decrypt(encrypted_text, key):
    # Randomize the keys before use
    shuffled_key = shuffle_key(key)
    decrypted_text = ""

    for i, char in enumerate(encrypted_text):
        # Subtracts the Unicode value of the encrypted character from the Unicode value of the key character
        decrypted_char = ord(char) - ord(shuffled_key[i % len(shuffled_key)])

        # If the Unicode value is negative, add 1114111
        if decrypted_char < 0:
            decrypted_char += 1114111

        # Convert the decrypted Unicode value back to a character
        decrypted_text += chr(decrypted_char)

    return decrypted_text
