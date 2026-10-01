import random
#● ┌ ─ ┐ ┄ └ ┘ │

"┌─────────┐"
"│         │"
"│         │"
"│         │"
"└─────────┘"

dice_art = {1:("┌─────────┐",
               "│         │",
               "│    ●    │",
               "│         │",
               "└─────────┘"),
            2:("┌─────────┐",
               "│ ●       │",
               "│         │",
               "│       ● │",
               "└─────────┘"),
            3:("┌─────────┐",
               "│ ●       │",
               "│    ●    │",
               "│       ● │",
               "└─────────┘"),
            4:("┌─────────┐",
               "│ ●    ●  │",
               "│         │",
               "│ ●    ●  │",
               "└─────────┘"),
            5:("┌─────────┐",
               "│ ●     ● │",
               "│    ●    │",
               "│ ●    ●  │",
               "└─────────┘"),
            6:("┌─────────┐",
               "│ ●  ●  ● │",
               "│ ●  ●  ● │",
               "│ ●  ●  ● │",
               "└─────────┘")
}
dice = []
total = 0
choice = int(input("How many dice?: "))

for _ in range(choice):
    di = random.randint(1,6)
    dice.append(di)
    total += di

# for die in range(choice):
#     for tuple in dice_art.get(dice[die]):
#         print(tuple)

for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

    
print(F"total: {total}")