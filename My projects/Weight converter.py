weight = int(input("Enter your weight: "))
unit = input("Enter your unit (L)bs or (K)g: ")
if unit.upper() == "L":
    wight_kg = weight * 0.47
    print(f"{wight_kg}kg")
elif unit.upper() == "K":
    print(f"{weight * 0.5}lbs")
else:
    print("Wrong Si unit")


