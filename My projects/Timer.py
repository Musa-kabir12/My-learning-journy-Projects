import time

my_time = int(input("Enter your time in seconds: "))

for i in reversed(range(0, my_time)):
    seconds = i %  60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
print("Time's up!")

