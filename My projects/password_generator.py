import string
from random import *


def generate_password():
    letter = string.ascii_letters
    digit = string.digits
    ascc = string.punctuation

    chars = letter + digit + ascc

    min_length = 6

    max_length = 15


    password = ""
    for _ in range(randint(min_length, max_length)):
        password += choice(chars)

    print(f"Your new password is: {password}")


generate_password()


