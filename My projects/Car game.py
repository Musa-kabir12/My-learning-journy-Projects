#CAR GAME
print("Welcome to the car game, to start the game type enter")
print(input(">"))
started = False
stopped = False
while True:
    print("start- to start the car")
    print("stop- to stop the car")
    print("exit- to exit")
    choice = input(">").upper()
    if choice == "START":
        if started:
         print("Already started")
        else:
            print("Car started... Ready to go")
            started = True
    elif choice =="STOP":
        if stopped:
         print("Already stopped")
        else:
           print("Car stopped")
           stopped= True
    elif choice == "EXIT":
        print("Thanks for playing")
        break
    else:
        print("I don't understand that")


