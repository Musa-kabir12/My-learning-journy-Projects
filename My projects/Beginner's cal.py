#Very easy calculator
print("Market calculator")
print("1. add")
print("2. subtract")
print("3. multiply")
print("4. divide")
choice = int(input("Enter between 1 - 4: "))
if choice == 1:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 + num2)
elif choice == 2:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 - num2)
elif choice == 3:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(num1 * num2)
elif choice == 4:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print(round(num1 / num2, 1))
else:
    print("Invalid: Choose between 1 - 4")