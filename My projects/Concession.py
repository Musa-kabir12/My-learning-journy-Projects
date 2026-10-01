menu = {"POPCORN":4.00,
        "HOT DOG":2.70,
        "PIZZA":3.95,
        "BURGER":3.60,
        "SODA":1.60,
        "BOTTLED WATER":1.00}
cart = []
total = 0
print("------------------")
print("---  MENU  ---")
for key, value in menu.items():
    print(F"{key}: ${value}")
print("------------------")
while True:
    order = input("Enter what you want to buy (q to quite): ").upper()
    if order == "Q":
        break
    elif menu.get(order):
        cart.append(order)
        print("Order added to cart")
        price = menu[order]
        total += price
    else:
        print(f"{order} is not available in the menu")

print("--------------------")
print("---- YOUR CART  ----")
print("--------------------")
for item in cart:
    print(item)
print()
print(f"YOUR TOTAL IS: ${total}")