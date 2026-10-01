# Let's start

questions = ("How many years is engineering course in BUK?: ",
             "BUK is ranked ___ as the best universty in Nigeria?: ",
             "How many states are there in Nigeria?: ",
             "Who is the current President of Nigeria?: ",
             "How many month are there in a year?: ",)


options = (("A. 2","B. 3","C. 4","D. 5"),
           ("A. 1st ","B. 2nd","C. 3rd","D. 4th"),
           ("A. 14","B. 44","C. 36","D. 50"),
           ("A.Muhammad Buhari","B.Bola Tinubu","C. Peter Obi","D. Atiku Abubakar"),
           ("A. 24","B. 12","C. 4","D. 6"))


answers = ("D","C","C","B","B")
question_num = 0
guesses = []
scores = 0

for question in questions:
    print(question)
    print("---------------------")
    for option in options[question_num]:
        print(option)
    guess = input("Enter your choice (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        scores += 1
        print("CORRECT!")
    else:
        print(f"Incorrect, correct answer is: {answers[question_num]}")
    question_num += 1

percentage = int(scores / len(answers) * 100)

print("--------------------")
print("FINAL SCORE")
print("---------------------")
print("                            ")
print("Answers:")
for answer in answers:
    print(answer, end= " ")
print()
print("Your guesses: ")
for guess in guesses:
    print(guess, end= " ")
print()
print(f"Total score: {percentage}%")
        

 