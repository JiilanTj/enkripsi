from logic import crypto_decrypt

# The encrypted text you want to decrypt
encrypted_text = "The result of your encryption"
key = "secret_key"

# The text description uses the bcrypt decrypt function of the logic.py file
decrypted_text = crypto_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
