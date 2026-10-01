name = input("Enter your name:")
grade = []
grade.append(int(input("Enter your first score:")))
grade.append(int(input("Enter your second score:")))
grade.append(int(input("Enter your third score:")))
grade.append(int(input("Enter your fouth score:")))
grade.append(int(input("Enter your fifth score:")))
max= max(grade)
def total_average(grade):
    total = sum(grade)
    average = total/ len(grade)
    return total, average
x,y = total_average(grade)
#Here x is total and y is average

#I make it that pass is 50 and above while fail is below 50
def scores_50(grade):
    higer = 0
    lower = 0
    for i in grade:
        if i>= 50:
            higer += 1
        else:
            lower += 1
    return  higer, lower
a,b = scores_50(grade)
#Here a is number grade more than 50 and b grade lower than 50
def specific(grade):
    has_90 = False
    for s in grade:
        if s >= 90:
            return True
    return has_90
m = specific(grade)
#catch yah... hhhh
#To have excellent you have to score at least 90 or above at least once
print(f"SCORE REPORT OF {name}")
print("------------------------")
print(f"Total: {x}")
print(f"Average: {y}")
print(f"Passed: {a}")
print(f"Failed: {b}")
print(f"Higest score: {m}") #check for bug. Bug corrected, lol