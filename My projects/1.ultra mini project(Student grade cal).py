name = input("Enter your full name: ")
a = int(input("Enter your first score: "))
b = int(input("Enter your second score: "))
c = int(input("Enter your third score: "))
d = int(input("Enter your fouth score: "))
e = int(input("Enter your fifth score: "))
total = a + b + c + d + e
average = total/5
if average >= 70:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 50:
    grade = "C"
elif average >=45:
    grade = "D"
elif average >= 40:
    grade = "E"
else:
    grade = "F"
#Determine wether average is Excellent, VERY GOOD, GOOD, Passed, CONDITIONAL PASS or Failed
if average >= 70:
    result = "Excellent"
elif average >= 60:
    result = "VERY GOOD"
elif average >= 50:
    result = "GOOD"
elif average >= 45:
    result = "PASSED"
elif average >= 40:
    result = "CONDITIONAL PASS"
else:
    result = "FAILED"
#Displaying the  results
print(f"Student: {name}")
print(f"Total: {total}")
print(f"Average: {average}")
print(f"Grade: {grade}")
print(f"Status: {result}")