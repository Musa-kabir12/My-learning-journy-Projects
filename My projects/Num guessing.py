#Number guessing game
import random

lowest_number = 10
highest_number = 30
chances = 5
guessing = 0
answer = random.randint(lowest_number, highest_number)
print("WELCOME TO PYTHON NUMBER GUESSING GAME")
print(F"SELECT BETWEEN {lowest_number} and {highest_number}")
while guessing < chances:
    guess = int(input(f"Guess the number between {lowest_number} and {highest_number}: "))
    print(f"You answer it under {guessing} guessing!")
    if guess == answer:
        print(f"Congratulation! {guess} is the correct answer")
        break
    elif guess < lowest_number or guess > highest_number:
        print(f"Out of range, choose between {lowest_number} and {highest_number}")
        guessing += 1
    elif guess  < answer:
        print("Too low, try again")
        guessing += 1
    elif guess > answer:
        print("Too high, try again")
        guessing += 1
else: 
    print(f"You run out of chances, correct answer is: {answer}")
    