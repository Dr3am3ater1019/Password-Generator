import random
import string

def get_characters(include_special=True, include_digits=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation
    return characters

def generate_password(length, include_special=True, include_digits=True):
    characters = get_characters(include_special, include_digits)
    password = ''.join(random.choice(characters)for _ in range(length))
    return password

length = int(input("Enter Password Lenght: "))
include_special = input("Include special characters? (y/n): ").lower() == 'y'
include_digits = input("Include digits? (y/n): ").lower() == 'y'

password = generate_password(length, include_special, include_digits)
print(f"Generated Password: {password}")