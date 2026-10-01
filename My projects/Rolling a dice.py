import random


#my way
def rolling_dice():
    first_roll = random.randint(1,6)
    second_roll = random.randint(1,6)
    print(f"({first_roll},{second_roll})")


#rolling_dice()

#Mosh way
class Dice:
    def roll(self,):
        first_number =random.randint(1,6)
        second_number = random.randint(1,6)
        return (first_number,second_number)

rolling  = Dice()
print(rolling.roll())