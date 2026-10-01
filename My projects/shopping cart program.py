foods = []
prices = []
total = 0
while True:
    food = input("Enter the food you want to buy (q to quite): ")
    if food == "":
        print("You did'nt type anything")
    elif food.upper() == "Q":
        break
    else:
        price = float(input(f"Enter the price of {food}: $"))
        prices.append(price)
        foods.append(food) 

print("----- YOUR CART -----")
for food1,price1  in zip(foods,prices): #zip() to return each at same time if not it will return pairs of same variable
    print(f"{food1}: ${price1}") # without zip() yam: $orange 4.0: $3.44
for price1 in prices:
    total += price1
print(f"Your Total is: {total: .2f}")