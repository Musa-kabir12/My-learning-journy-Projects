# Bismillah 
import random
import time


def processing(func):
    def wrapper(*args, **kwargs):
        for i in range(2):
            print("LOADING......")
            time.sleep(1)
        print("Processing started.....")
        print()
        result = func(*args,**kwargs)
        print()
        print("Processing completed.")
        print()
        return result
    return wrapper


class BankAccount:
    number_of_acc = 0
    def __init__(self, account_number, customer_name, balance, transaction_history = None):
        if transaction_history is None:
            transaction_history =  []
        self.account_number = account_number
        self.customer_name = customer_name
        self.__balance = balance
        self.transaction_history = transaction_history
        BankAccount.number_of_acc += 1


    @classmethod
    def num_of_acc(cls):
        print(f"Total Account created: {cls.number_of_acc}")


    @staticmethod
    def is_valid(amount):
        if amount <=0:
            return False
        else:
            return True


    def get_balance(self):
        return self.__balance

    
    def change_balance(self, amount):
        self.__balance += amount


    def sub_amount(self, amount):
        self.__balance -= amount


    def get_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(F"Customer name: {self.customer_name}")
        print(F"Account Balance: {self.__balance}")
        if isinstance(self, CurrentAccount):    # don't start with the parent class and isinstance is new ilimi for me
            print(F"Account type: CurrentAccount")
        elif isinstance(self, SavingsAccount):
            print(F"Account type: SavingsAccount")
        elif isinstance(self, BankAccount):
            print(F"Account type: BankAccount")
        else:
            print("Account type not found")


    @processing
    def deposit(self, amount):
        if not self.is_valid(amount):
            print(f"${amount} is not valid")
        elif float(amount) < 100:
            print("You can't deposit less than $100")
        else:
            for _ in range(3):
                print("Processing.....")
                time.sleep(1)
            self.__balance += amount
            self.transaction_history.append(f"Deposit: {amount}")
            print(f"${amount} is deposited")
            print(F"New balance: {self.get_balance()}")

    @processing
    def withdraw(self, amount):
        if not self.is_valid(amount):
            print("Invalid amount")
        elif amount > self.__balance:
            print("Insufficient Funds")
        else:
            for _ in range(3):
                print("Processing.....")
                time.sleep(1)
            self.__balance -= amount
            self.transaction_history.append(f"Withdraw: ${amount}")
            print(f"${amount} is withdrawn")
            print(F"New balance: {self.get_balance()}")


    def transfer(self,  other_account, amount):
        if not self.is_valid(amount):
            print("Invalid amount")
        elif amount > self.get_balance():
            print("Insufficent funds")
        else:
            self.sub_amount(amount)
            for _ in range(3):
                print("Processing.....")
                time.sleep(1)
            self.transaction_history.append(f"Transferred ${amount} to {other_account.customer_name}")
            other_account.change_balance(amount)
            other_account.transaction_history.append(f"Alert of ${amount} recieved from {self.customer_name}")
            print(f"Transfer of ${amount} to {other_account.customer_name} sucessful!")
            print(F"New balance: ${self.get_balance()}")


    def get_transaction_history(self):
        if self.transaction_history == []:  #or if not self.transaction_history:
            print("No Transaction yet")
        else:
            print("=== Transaction history ===")
            for trans in self.transaction_history:
                print(trans)


class SavingsAccount(BankAccount):
    def __init__(self,interest_rate, account_number, customer_name, balance, transaction_history=None,):
        super().__init__(account_number, customer_name, balance, transaction_history)
        self.interest_rate = interest_rate


    @processing
    def apply_interest(self):
        int_amt = (self.get_balance() * (self.interest_rate / 100))
        self.change_balance(int_amt)
        for _ in range(3):
            print("Processing.....")
            time.sleep(1)
        print(F"Amount after {self.interest_rate}% interest: ${self.get_balance()}")
        self.transaction_history.append(f"interest Amount: {int_amt}")


class CurrentAccount(BankAccount):
    def __init__(self, account_number, customer_name, balance, overdraft_limit, transaction_history=None):
        super().__init__(account_number, customer_name, balance, transaction_history)
        self.overdraft_limit = overdraft_limit

    @processing
    def withdraw(self, amount):
        if amount > (self.get_balance() + self.overdraft_limit):
            print("Insufficent funds")
        elif amount <= 0:
            print("Please enter valid amount")
        else:
            self.sub_amount(amount)
            for _ in range(3):
                print("Processing.....")
                time.sleep(1)            
            print(F"${amount} withdrawn")
            print(F"New balance: ${self.get_balance()}")
            self.transaction_history.append(f"${amount} is withdrawn from CurrentAccount")


account1 = BankAccount("00001", "Ahmad Rabi'u Falalu", 5000000,None)
account2 = SavingsAccount(5, "00002", "Muhammad Abdullahi Abbas",5000000,None)
account3 = SavingsAccount(5, "00003", "Al-amin Adam",5000000,None)
account4 = CurrentAccount("00004","Musa Kabir Dandago",6000000,1000000,None)
account5 = CurrentAccount("00005","Usman Abubakar",4000000,1000000,None)


customers = {"00001":{
    "name":"Ahmad Rabi'u Falalu",
    "account": account1,
    "pin":"1234"
},
"00002":{
    "name":"Muhammad Abdullahi Abbas",
    "account": account2,
    "pin":"2345"
},
"00003":{
    "name":"Al-amin Adam",
    "account": account3,
    "pin":"3456"
},
"00004":{
    "name":"Musa Kabir Dandago",
    "account": account4,
    "pin":"4567"
},
"00005":{
    "name":"Usman Abubakar",
    "account": account5,
    "pin":"5678"
},
}



print("=" * 120)
print("WELCOME TO MUSA'S BANK".center(100))
print("=" * 120)


while True:
    print("1. Create Account")
    print("2. Already have an account")
    print("3. Exit")
    try:
        get_request = input("Please choose amoung the options: ")
        if get_request == "3":
            print("Thank you for using Musa's Bank of Nigeria😊")
            quit()
        elif get_request == "1":
            name = input("Please enter your name: ")
            while True:
                pin = input("Enter you desired pin: ")
                if not pin.isdigit():
                    print("Please enter numbers only")
                    continue
                elif len(pin) != 4:
                    print("Pin must be 4 digits")
                    continue
                else:
                    re_type = input("Please enter the pin again to confirm: ")
                    if re_type == pin:
                        break
                    else:
                        print("pin not match")
                        continue

            while True:
                print("Available account type")
                print("1. Current Account")
                print("2. Savings Account")
                account = input("Please choose among the options: ")
                if account == "1":
                    while True:
                        account_number = ""
                        for _ in range(5):
                            account_number += str(random.randint(0,9))
                        if account_number in customers:
                            continue
                        else:
                            print(f"This is you account number: {account_number}")
                            break
                    while True:
                        balance = input("Please deposite your first money: ")
                        if not balance.isdigit():
                            print("please enter a valid amount")
                            continue
                        elif int(balance) < 1000:
                            print("You can't deposite less than $1000")
                            continue
                        else:
                            print(f"""You have deposited ${balance} into your new current account
You can overdraft upto $500000""")
                            break
                    over_draft = 500000
                    account_type = CurrentAccount(account_number,name,float(balance),over_draft, None)
                    customers[account_number] = {"name":name,
                                                 "account": account_type,
                                                 "pin": pin }
                    break
                elif account == "2":
                    while True:
                        account_number = ""
                        for _ in range(5):
                            account_number += str(random.randint(0,9))
                        if account_number in customers:
                            continue
                        else:
                            print(f"This is you account number: {account_number}")
                            break
                    while True:
                        balance = input("Please deposite your first money: ")
                        if not balance.isdigit():
                            print("please enter a valid amount")
                            continue
                        elif int(balance) < 1000:
                            print("You can't deposite less than $1000")
                            continue
                        else:
                            print(f"""You have deposited ${balance} into your new Savings account
You can have intrest of upto 5%""")
                            break
                    interest = 5
                    account_type = SavingsAccount(interest,account_number, name, float(balance), None)
                    customers[account_number] = {"name":name,
                                                 "account": account_type,
                                                 "pin": pin }
                    break
                else:
                    print("Please choose amoung 1 0r 2!")
                    continue
            logged_account =  customers[account_number]["account"]

            print("==================================================")
            print(f"Welcome, {customers[account_number]['name']}!")
            print(f"Account type: {type(customers[account_number]['account']).__name__}")
            print("==================================================")

            while True:

                print("*" * 100)
                print("BANK MENUE".center(100))
                print("*" * 100)
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Transaction history")
                print("6. Account Information")
                print("7. Apply interest")
                print("8. Logout")

                try:
                    choice = int(input("Choose your option: "))

                    match choice:
                        case 1:
                            print(f"Current Balance: ${logged_account.get_balance()}")

                        case 2:

                            amount = float(input("Enter amount you want to deposit: "))
                            logged_account.deposit(amount)
                        case 3:

                            amount = float(input("Enter amount you want to withdraw: "))
                            logged_account.withdraw(amount)

                        case 4:
                            receiver_number = input("Please enter the recipent account number: ")
                            if receiver_number in customers and receiver_number != account_number:
                                for _ in range(3):
                                    pin = input("Please enter your pin: ")
                                    if pin == customers[account_number]["pin"]:
                                        amount = int(input("Please enter amount you want to Transfer: "))
                                        receiver_number = customers[receiver_number]["account"]
                                        logged_account.transfer(receiver_number, amount)
                                        break
                                    else:
                                        print("Incorrect pin")
                                else:
                                    print("Can't make transfer now!")
                                    continue
                            elif receiver_number == account_number:
                                print("Cannot transfer to yourself")
                            else:
                                print("Account not found")

                        case 5:
                            logged_account.get_transaction_history()

                        case 6:
                            logged_account.get_account_info()
                        case 7:
                            if isinstance(logged_account, SavingsAccount):
                                logged_account.apply_interest()
                            else:
                                print("This feature is not available for your account type")
                        case 8:
                            print("Bye, Come Back later")
                            break
                        case _:
                            print("Invalid input (Choose between 1-8)")


                except ValueError:
                    print("Please enter a number")

        elif get_request == "2":
            print("="* 100)
            print("Please log in your account".center(100))
            print("=" * 100)
            get_acc = input("Enter your account number: ")
            if get_acc in customers:
                for _ in range(3):
                    pin = input("Please enter your pin: ")
                    if pin == customers[get_acc]["pin"]:
                        logged_account =  customers[get_acc]["account"]
                        print("Account logged in")
                        print("==================================================")
                        print(f"Welcome, {customers[get_acc]['name']}!")
                        print(f"Account type: {type(customers[get_acc]['account']).__name__}")
                        print("==================================================")
                        break
                    else:
                        print("Incorrect pin")
                else:
                    print("Account locked!")
                    quit()
            else:
                print("Account not found")
                continue

            while True:

                print("*" * 100)
                print("BANK MENUE".center(100))
                print("*" * 100)
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer")
                print("5. Transaction history")
                print("6. Account Information")
                print("7. Apply interest")
                print("8. Logout")

                try:
                    choice = int(input("Choose your option: "))

                    match choice:
                        case 1:
                            print(f"Current Balance: ${logged_account.get_balance()}")

                        case 2:

                            amount = float(input("Enter amount you want to deposit: "))
                            logged_account.deposit(amount)
                        case 3:

                            amount = float(input("Enter amount you want to withdraw: "))
                            logged_account.withdraw(amount)

                        case 4:
                            receiver_number = input("Please enter the recipent account number: ")
                            if receiver_number in customers and receiver_number != get_acc:
                                for _ in range(3):
                                    pin = input("Please enter your pin: ")
                                    if pin == customers[get_acc]["pin"]:
                                        amount = int(input("Please enter amount you want to Transfer: "))
                                        receiver_number = customers[receiver_number]["account"]
                                        logged_account.transfer(receiver_number, amount)
                                        break
                                    else:
                                        print("Incorrect pin")
                                else:
                                    print("Account locked!")
                                    continue
                            elif receiver_number == get_acc:
                                print("Can not transfer to yourself")
                            else:
                                print("Account not found")

                        case 5:
                            logged_account.get_transaction_history()

                        case 6:
                            logged_account.get_account_info()
                        case 7:
                            if isinstance(logged_account, SavingsAccount):
                                logged_account.apply_interest()
                            else:
                                print("This feature is not available for your account type")
                        case 8:
                            print("Bye, Come Back later")
                            break
                        case _:
                            print("Invalid input (Choose between 1-8)")


                except ValueError:
                    print("Please enter a number")

        else:
            print("Please Choose among options")
            continue

    except ValueError:
        print("Please enter a digit from the options")



