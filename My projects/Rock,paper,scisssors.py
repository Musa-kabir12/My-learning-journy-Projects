# ROCK, PAPER SCICSSORS game
import random

options = ("rock","paper","scissors")

chances =  5
used = 0
users_score = 0 
computer_score = 0
print("----  WELCOME TO PYTHON ROCK, PAPER, SCISSORS GAME  ----")
while used < chances:
    choice = input("Enter your choice (rock,paper,scissors): ").lower()
    com_choice = random.choice(options)
    used +=1
    if choice == com_choice:
        print(f"computer choice: {com_choice}")
        print("Draw")
    elif choice == "rock" and com_choice == "scissors":
        print(f"computer choice: {com_choice}")
        print("You win this round")
        users_score += 1
    elif choice == "paper" and com_choice == "rock":
        print(f"computer choice: {com_choice}")
        print("You win this round")
        users_score += 1
    elif choice == "scissors" and com_choice == "paper":
        print(f"computer choice: {com_choice}")
        print("You win this round")
        users_score += 1
    elif choice not in options:
        print("Please choose between rock,paper or scissors")
    else:
        print(f"Computer choice: {com_choice}")
        computer_score += 1
        print("You lose this round")
print("----  HERE IS YOUR TOTAL SCORE ----")
print(F"Your total: {users_score}")
print(F"Computer score: {computer_score}")
if users_score > computer_score:
    print("You're the winner")
elif users_score == computer_score:
    print("The game is a draw")
else:
    print("Computer wins, try again.")


