from logic import crypto_encrypt

# Example of use
plain_text = "Example of the text you want to encrypt"
key = "secret_key"

# Encrypt the text using the crypto_encrypt function from the logic.py file
encrypted_text = crypto_encrypt(plain_text, key)
print("Original Text:", plain_text)
print("Keys Used:", key)
print("Encrypted Text:", encrypted_text)
