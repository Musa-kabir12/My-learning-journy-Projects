# Python alarm clock
import time
import datetime
import pygame
import playsound3


def set_alarm(alarm_time):
    print(F"Alarm set for {alarm_time}")
    sound_file = "PROJECT/Bro code/Audio1.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if current_time == alarm_time:
            pygame.mixer.init()  # just use the defult
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            print("WAKE UP!!")
            is_running = False

            pygame.mixer.music.play()  # select specific seconds

            pygame.time.wait(5000)  # 5,000 milliseconds = 5 seconds

            pygame.mixer.music.stop()
            # while pygame.mixer.music.get_busy():    till the music finish
            #     time.sleep(1)



if __name__ ==  "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)