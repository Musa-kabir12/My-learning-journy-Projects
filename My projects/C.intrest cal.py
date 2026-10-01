#Compound Calculator project
import math
print("Welcome to compund intrest calculator".upper())

principal = int(input("Please enter amount you want to deposite: "))

while principal  < 100:
    print("You can only deposite $1000 and above")
    principal = int(input("Please enter amount you want to deposite: "))


rate = int(input("Enter at which rate you want your account to run (%): "))

while rate < 0 or rate > 100:
    print("Available rate is between 1% to 50%")
    rate = int(input("Enter at which rate you want your account to run (%): "))


time = int(input("Enter years to take before withdrawing: "))

while time <= 0:
    print("You can only withdraw after 1 year. ")
    time = int(input("Enter years to take before withdrawing: "))

amount = principal * pow(1 + (rate / 100), time)

print(F"""Your estimated amount after:
{time} years
At {rate}% rate
With the principal of  ${principal} is
Amount: ${amount: .2f}""")
