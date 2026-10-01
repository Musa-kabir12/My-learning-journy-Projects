students = {}
for i in range(2):
    names = input("Enter name: ").upper()
    scores = []
    for j in range(3):
        score = int(input("Enter your marks: "))
        scores.append(score)
    students[names] = scores
#print(students.items()) everything working
def analyze_student(name):
    Is_pass = False
    scores = students[name]
    average = sum(scores)/len(scores)
    if average >= 50:
        Is_pass = True
    higest = max(scores)
    return average, Is_pass, higest
def is_excellent(scores):
    Is_false = False
    for score in scores:
        if score >= 90:
         return True
    return Is_false
try:
    print(students)
    name = input("Enter the name you want to see: ").upper()
    x,y,z = analyze_student(name)
    w = is_excellent(students[name])
    if name in students:
        print(f"Student Profile of: {name}")
        print(f"Your average is: {x}")
        print(f"Passed(your average more than or eqaul 50): {y}")
        print(f"Your highest score is: {z}")
        print(f"Excellent result(You have at least one 90): {w}")
        #x is average
        #y is Is_pass
        #z is Higest mark scored
        #w is if you at least have one 90
except KeyError:
    print("Students not found")

#I hope it works.. please you must work (:
#It did not, but i will correct again now.
#Third correction