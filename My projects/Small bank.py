
def show_balance():
    print(f"Your balance is: ${balance: .2f}")


def deposit():
    amount = float(input("Enter amount you want to deposit: "))
    if amount > 0:
        return amount
    else:
        print("Please enter a real amount")
        return 0



def witdraw():
    amount = float(input("Enter amount you want to withdraw: "))
    if amount > balance:
        print("Your capacity no reach😂")
        return 0
    elif amount < balance and amount > 0:
        return amount
    else:
        print("Please enter a real amount")
        return 0


balance = 0
is_true = True

while is_true:
    print("Welcome to python Bank")
    print("1. show_balance")
    print("2. Deposit")
    print("3. withdraw")
    print("4. exit")
    choice = input("Enter option between (1 - 4): ")
    match choice:
        case "1":
            show_balance()
        case "2":
            balance += deposit()
        case "3":
            balance -= witdraw()
        case "4":
            is_true = False
        case _:
            print("Invalid option, please choose between 1  - 4")

print("Thanks for banking with us")