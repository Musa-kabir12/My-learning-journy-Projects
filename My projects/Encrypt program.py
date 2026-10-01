import random
import string

char = string.punctuation + string.ascii_letters +  string.digits + " "

char = list(char)

key = char.copy()

random.shuffle(key)

# ENCRYPT
plain_text = input("Enter what you want to encrypt: ")

encrypted = ""
for text in plain_text:
    location = char.index(text)
    encrypted += key[location]

print(F"Original text: {plain_text}")
print(F"Encrypted version: {encrypted}")

#Decrypted
encrypted_text = input("Enter what you want to Decrypt: ")

decrypted = ""
for text in encrypted_text:
    location = key.index(text)
    decrypted += char[location]

print(F"Encrypted version: {encrypted_text}")
print(F"Original text: {decrypted}")