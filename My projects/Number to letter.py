numbers = input("Phone: ")
numlet = {"0":"zero",
        "1":"one",
        "2":"Two",
        "3":"Three",
        "4":"Four",
        "5":"Five",
        "6":"six",
        "7":"Seven",
        "8":"Eight",
        "9":"Nine"
}
letters = ""
for number in numbers:
    letter = numlet.get(number, "Only numbers")
    letters += letter + " "
print(letters)

