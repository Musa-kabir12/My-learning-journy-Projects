#Guessing game
import random
chances = 0
while chances < 3:
    number = int(input("Guess: "))
    if number == random.randint(1,10):
        print("ongratulation, you're are genuis!")
        break
    chances += 1
else:
    print(f"Sorry you have faild. the number is {random.randint(1,10)}")
#better version
secret_number = random.randint(1,10)
guess_chances = 0
guess_limit = 3
while guess_chances < guess_limit:
    guess = int(input("Guess number:"))
    if guess == secret_number:
        print("Congratulation, you're are genuis!")
        break
    guess_chances += 1
else:
    print(f"Sorry you have faild.  the number is {secret_number}")