import random
import time



# My version 95% myself without AI
# items = ("🍪", "🍩", "🍔", "🍕", "🍟")

# cookies = ("🍪", "🍪", "🍪")
# donot = ("🍩", "🍩", "🍩")
# burger = ("🍔", "🍔", "🍔")
# pizza = ("🍕", "🍕", "🍕")
# chips = ("🍟", "🍟", "🍟")

# balance = 100.00

# print("---  SLOT MACHINE  ---")
# print("Symbols: 🍪 🍩 🍔 🍕 🍟")
# print(f"Balance: ${balance}")

# while balance > 0:
#     choice =int(input("What amount you want to bet: "))
#     if choice <= balance:
#         for _ in range(2):
#             print("spinning.....")
#             time.sleep(1)
#         item = random.choices(items, k= 3)
#         balance -= choice
#         if item == cookies or item == donot or item == burger or item == pizza or item == chips:
#             for object in item:
#                 print(object, end= " | ")
#             print("You have won!!")
#             prize = 50
#             balance += prize
#             print(f"you have won: ${prize: .2f}")
#             print(F"Curret value: ${balance: .2f}")
#         else:
#             for object in item:
#                 print(object, end= " | ")
#             print("You have lose this round")
#             print(F"Current value ${balance}")
#     elif choice > balance:
#         print("Insufficent funds")
#         print("Current balance",  balance)  # remebering old days.... lol
#     else:
#         print("Invalid input")
#     while True:
#         spin = input("you want to continue playing (y/n)").lower()
#         if spin == "y" or spin == "n":
#             break
#         else:
#             print("Please choose y/n: ")
#     if spin == "n":
#         print("Thanks for playing")
#         print(f"Your balance: ${balance}")
#         break
#     elif balance <= 0:
#        print("You are out of balance, Thanks for playing")
#        break



# Tutorial version


def spin_row():
    symbols = ("🍪", "🍩", "🍔", "🍕")
    choice = [random.choice(symbols) for _ in range(3)]
    return choice



def print_row(choice):
    for _ in range(3):
        print("Spinning.........")
        time.sleep(1)
    print(" | ".join(choice))

def pay_out(choice, bet):
    if choice[0] == choice[1] == choice[2]:
        if choice[0] ==  "🍪":
            return bet * 3
        elif choice[0] == "🍩":
            return bet * 5
        elif choice[0] == "🍔":
            return bet * 7
        elif choice[0] == "🍕":
            return bet * 10
        elif choice[0] == "🍟":
            return bet * 5
    else:
        return 0

def main():
    balance = 100
    print("*" * 40)
    print("Welcome to python slot machine game")
    print("Symbols: 🍪 🍩 🍔 🍕 🍟")
    print("*" * 40)
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("How much you want to bet on: ")
        if not bet.isdigit():
            print("Invalid amount")
            continue
        bet = int(bet)
        if bet > balance:
            print("Insufficent amount")
            continue
        elif bet <= 0:
            print("Bet must be greater than 0")
            continue
        balance -= bet
        choice = spin_row()
        print_row(choice)
        cashOut = pay_out(choice, bet)
        if cashOut > 0:
            print(F"You have won ${cashOut}")
        else:
            print("Sorry you lost this round")
        balance += cashOut
        play_again = input("Did you want to play (y/n): ").lower()
        if play_again != "y":
            break
    print(f"""Thanks for playing
You remaing balance: ${balance}""")

if __name__ == "__main__":
    main()