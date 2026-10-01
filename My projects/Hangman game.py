# Hangman python
import random

words = ("apple", "banana", "orange", "watermelon", "strawberry")

hangman_art = {0:("  ",
                  "  ",
                  "  "),
               1:(" O ",
                  "  ",
                  "  "),
               2:(" O ",
                  " | ",
                  "  "),
               3:(" O ",
                  "/| ",
                  "  "),
               4:(" O ",
                  "/|\\ ",
                  "  "),
               5:(" O ",
                  "/|\\ ",
                  "/ "),
               6:(" O ",
                  "/|\\ ",
                  "/ \\ ")}


def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hints):
    print(" ".join(hints))
    # for line in hints:           # My way
    #     print(line, end=" ")
    # print()


def display_answer(answer):
    print(" ".join(answer))   # so that it will take space of each _, if not they will be attached together if we print(answer)



def main():
    answer = random.choice(words)
    hints = ["_"] * len(answer)
    guessed_letter = set()
    wrong_guesses = 0
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hints)
        symbol = input("Enter a letter: ").lower()
        if len(symbol) != 1 or symbol.isdigit():
            print("Invalid input")
            continue
        if symbol in guessed_letter:
            print(f"{symbol} already choosed")
            continue
        if symbol not in answer:  #how i put it
            wrong_guesses +=1
        guessed_letter.add(symbol)
        if symbol in answer:
            for i in range(len(answer)):
                if answer[i] == symbol:
                    hints[i] = symbol
        # else:
        #     wrong_guesses += 1  how he put it
        if "_" not in hints:
            print("YOU WON!!")
            display_man(wrong_guesses)
            display_answer(answer)
            is_running = False
        elif wrong_guesses >= 6:
            display_man(wrong_guesses)
            print("Sorry you have lose, correct answer is: ")
            display_answer(answer)
            is_running = False


if __name__ == "__main__":
    main()
