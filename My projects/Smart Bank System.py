#Musa's Bank Of Nigeria
import time
import random
Customers = { "00001":{
    "name":"Ahmad Rabiu Falalu",
    "Pin": 1234,
    "balance": 5000000,
    "transaction": []
},
"00002":{
    "name":"Muhammad Abbas",
    "Pin": 2345,
    "balance": 4000000,
    "transaction": []
},
"00004":{
    "name":"Musa Kabir Dandago",
    "Pin": 3456,
    "balance": 3000000,
    "transaction": []

},

}

print("====================".center(100))
print("WELCOME TO SMARTBANK".center(100))
print("====================".center(100))

account_number= input("Enter your account number: ")
if account_number in Customers:
    try:
        for chance in range(3):
            pin = int(input("Enter your account pin: "))
            if pin ==Customers[account_number]["Pin"]:
                print("Account logged in")
                print("==================================================")
                print(f"Welcome, {Customers[account_number]["name"]}!")
                print(f"Current balance: ${Customers[account_number]["balance"]}")
                print("==================================================")
                break
            else:
                print("Incorrect Pin")
        else:
            print("Account Locked")
            quit()
    except ValueError:
        print("Invalid input")
else:
    print("No such account")
    print("Feel free to create account with us")
    quit()
    # print("Account not found")
    # while True:
    #     enter = input("You want to try again (y/n): ").lower()
    #     if enter == "n":
    #         print("Feel free to create account with us")
    #         quit()
    #     else:
    #         print("Please enter y/n")

        
    
#Defining a decoration 

def processing(func):
    def wrapper(account_number):
        for i in range(2):
            print("LOADING......")
            time.sleep(1)
        print("Processing started.....")
        print()
        result = func(account_number)
        print()
        print("Processing completed.")
        print()
        return result
    return wrapper

# 1.Deposit
@processing
def deposit(account_number):
    try:
     amount_d = int(input("Enter amount you want to deposit: "))
     if amount_d >= 100:
         new_balance = Customers[account_number]["balance"] + amount_d
         Customers[account_number]["balance"] = new_balance
         Customers[account_number]["transaction"].append({"type":"deposit","amount":amount_d})
         for _ in range(3):
            print("Processing....")
            time.sleep(1)
         print(f"{amount_d} deposited sucessfully.")
         print(f"New balance: {new_balance}")
     else:
         print("Can only deposit amount more than 100")
    except ValueError:
        print("Invalid amount. Please enter a number")

#deposit(account_number)

#2.withdrawal
@processing
def withdrawal(account_number):
    try:
        for i in range(3):
            pin = int(input("Enter your pin: "))
            if pin == Customers[account_number]["Pin"]:
                amount_w = int(input("Enter amount you want to withdraw: "))
                if amount_w <= Customers[account_number]["balance"]:
                    Customers[account_number]["balance"] -= amount_w
                    Customers[account_number]["transaction"].append({"type":"withdraw","amount":amount_w})
                    for _ in range(3):
                        print("Processing....")
                        time.sleep(1)
                    print(f"{amount_w} withdrawn sucessfully")
                    print(f"new balance: {Customers[account_number]["balance"]}")
                else:
                    print("Insufficent funds")
                break
            else:
                print("Incorrect pin")
        else:
            print("You're a thief") # i like wickedness😂
    except ValueError:
        print("Input the right value.")

#witdrawal(account_name)

#3. transfer
@processing
def transfer(account_number):
    for i in range(3):
        pin = int(input("Enter your pin: "))
        if pin == Customers[account_number]["Pin"]:
            ask = input("Enter recipient account number: ")
            if ask in Customers and ask != Customers[account_number]:
                amount_t = int(input("Enter amount: "))
                if amount_t <= Customers[account_number]["balance"]:
                    Customers[ask]["balance"] += amount_t
                    Customers[account_number]["balance"] -= amount_t
                    Customers[account_number]["transaction"].append({"type":"sent","amount":amount_t})
                    for _ in range(3):
                        print("Processing....")
                        time.sleep(1)
                    print("Transaction sucessful")
                    print(f"${amount_t} sent to {Customers[ask]["name"]}")
                    print(f"Remaining balance: ${Customers[account_number]["balance"]}")
                else:
                    print("insufficeint balance")
            elif ask in Customers and ask == Customers[account_number]:
                print("Can not send money to yourself")
            else:
                print("Account not found")
            break
        else:
            print("Incorrect password")
    else:
        print("You're a thief!") #lol😂
       
        
#transfer(account_number)

#4 transaction history
def transaction(account_number):
    print("======== TRANSACTION HISTORY=======".center(100))
    for trans in Customers[account_number]["transaction"]:
        print(f"I have {trans["type"]} ${trans["amount"]}")

#transaction(account_number)

#5.account stats
def account_statistics(account_number):
    total_trans = len(Customers[account_number]["transaction"])
    print(f"Total transaction: {total_trans}")
    for trans in Customers[account_number]["transaction"]:
        filterd_depo = filter(lambda trans: trans["type"]=="deposit",Customers[account_number]["transaction"])
        filterd_with = filter(lambda trans: trans["type"]=="withdraw",Customers[account_number]["transaction"])
        total_depo = list(map(lambda trans: trans["amount"],filterd_depo))
        total_with = list(map(lambda trans: trans["amount"],filterd_with))
        print("Total Deposit: ",sum(total_depo))
        print("Total withdrawal: ", sum(total_with))

#account_statistics(acount_number)

#6. Check balance
def check_balance(account_number):
    print(f"Current balance: ${Customers[account_number]["balance"]}")


#check_balance(account_number)

#Building body

def main():
    is_true = True
    while is_true:
        print("1. Check balance ")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. Transaction history")
        print("6. Account statistics")
        print("7. Logout")

        try: 
            choice = int(input("Choose 1-7 from the list above: "))
            if choice ==  1:
                check_balance(account_number)
            elif choice == 2:
                deposit(account_number)
            elif choice == 3:
                withdrawal(account_number)
            elif choice == 4:
                transfer(account_number)
            elif choice == 5:
                transaction(account_number)
            elif choice == 6:
                account_statistics(account_number)
            elif choice == 7:
                print("Thanks for choosing Musa's Bank of Nigeria 😊")
                is_true = False
            else:
                print("Out of range, choose between 1-7")
        except ValueError:
            print("Please enter a number from the list above")



if __name__ == "__main__":
    main()

