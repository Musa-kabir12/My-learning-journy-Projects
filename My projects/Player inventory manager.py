#Player inventory Manager
players = {"Warrior": {
    "Coins": 1200,
    "inventory": ["Swords", "Sheild", "Helment", "Swords"]
    },
    "Mage": {
        "Coins": 1600,
        "inventory": ["Spell Book","Magical Stick","Potion"]
    },
    "Archer": {
        "Coins": 1500,
        "inventory": ["Bow", "Potion","Arrow", "Potion"]
    }
}
print("==== CHOOSE YOUR ROLE ====".center(50))
print("1. Warrior")
print("2. Mage")
print("3. Archer")
try:
    name = int(input("Choose Between 1 to 3: "))
    if name == 1:
        name = "Warrior"
        print("                                       ")
        print(f"Welcome, Warrior! ")
        print(f"coins: {players["Warrior"]['Coins']}")
        print(f"inventory: ")
        for item in players["Warrior"]["inventory"]:
            print(item)
    elif name == 2:
        name = "Mage"
        print("                                       ")
        print(f"Welcome, Mage! ")
        print(f"coins: {players["Mage"]['Coins']}")
        print(f"inventory:")
        for item in players["Mage"]["inventory"]:
            print(item)
    elif name == 3:
        name = "Archer"
        print("                                       ")
        print(f"Welcome, Archer! ")
        print(f"coins: {players["Archer"]['Coins']}")
        print(f"inventory:")
        for item in players["Archer"]["inventory"]:
            print(item)
    else:
        print(" Role not found. Choose from 1 to 3")

except ValueError:
    print("Invalid input")

#1.Custom Function of Inventory
def show_inventory(name):
    print("====INVENTORY====".center(60))
    for item in players[name]["inventory"]:
        print(item)
#show_inventory(name)


#2.Custom Function of count_item
def count_item(name):
    total_inv = len(players[name]["inventory"])
    print(f"Total items: {total_inv}")
#count_item(name)


#3.Custom Function of Unique items
def unique_items(name):
    unique = set(players[name]["inventory"])
    print("unique items:")
    for uni in unique:
        print(uni)
#unique_item(name)
#4. Custom Function of getting a Potion
def get_potion(name):
    get= players[name]["inventory"]
    potion = [p for p in get if p == "Potion" ]
    how = len(potion)
    print(f"Potion owned {how}")
#get_potion(name)
#5. Custom Functiom of adding item
def add_item(name):
    adding = input("Enter Item you want to add: ")
    players[name]["inventory"].append(adding)
    print(f"{adding} added to inventory.")
#add_item(name)


#6. Custom Fumction of Removing Item
def remove_item(name):
    try:
        item = input("Enter item you want to remove: ")
        removing = players[name]["inventory"]
        removing.remove(item)
        print(f"{item} removerd.")
    except ValueError:
        print("Item not Found")
#remove_item(name)


#7.Custom Function of buying a material
market = {
    "Swords":500,
    "Spell Book": 900,
    "Potion": 800,
    "Bow": 450
}
def buy_item(name):
    print(market)
    purchesing = input("Enter item you want to buy: ")
    if purchesing in market and players[name]["Coins"]>= market[purchesing]:
            new_Coins = players[name]["Coins"] - market[purchesing]
            players[name]["Coins"] = new_Coins
            players[name]["inventory"].append(purchesing)
            print(f"{purchesing} purchesd!")
            print(f"Remaining Coins: {new_Coins}")
    elif purchesing in market and players[name]["Coins"]< market[purchesing]:
            print("Not enough coins")
    else:
            print("item not found")
#buy_item(name)


while True:
    print("=====WARRIOR MENUE=====".center(67))
    print("1.Show inventory")
    print("2.Count items")
    print("3.Show unique items")
    print("4.Show potion")
    print("5.Add item")
    print("6.Remove item")
    print("7.Buy item")
    print("8.Exit")
    print("                                      ")
    try:
           #calling functions
         choice = int(input("Choose from 1 to 8: "))
         # match statement instead of if/elif statement
         match choice:
            case 1:
                show_inventory(name)
            case 2:
                count_item(name)
            case 3:
                unique_items(name)
            case 4:
                get_potion(name)
            case 5:
                add_item(name)
            case 6:
                remove_item(name)
            case 7:
                buy_item(name)
            case 8:
                print("Thanks for playing :)")
                break
            case _:
                print("Invalid input, choose between 1 to 8")
    except ValueError:
        print("Please enter a number")
         
        


        
        
    
        
      
        
        
          




