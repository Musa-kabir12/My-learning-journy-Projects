import pygame
from gtts import gTTS
from gtts import tts
import time
from deep_translator import GoogleTranslator
from deep_translator import exceptions
import requests
from deep_translator import GoogleTranslator







def voice(word, kind):
    voice = gTTS(text=word, lang=kind )

    voice.save("Audio1.mp3")

    file = "Audio1.mp3"

    print("speaking.....")

    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():   # till the text finish
            time.sleep(0.1)

    pygame.mixer.music.unload()   # to remove the current file to avoid error

def main():
    print("*" * 130)
    print("== Welcome to Text to voice converter App ==".center(100))
    print("*" * 130)

    while True:
        print("1. Covert text to voice")
        print("2. Exit")
        choice = input("Enter option: ")
        match choice:
             
            case "1":
                word = input("Enter what you want to say: ")
                voice(word, "en")

            case "2":
                  print("Bye")
                  break

if  __name__ == "__main__": main()



# def voice(word, kind):
#     voice = gTTS(text=word, lang=kind )

#     voice.save("Audio1.mp3")

#     file = "Audio1.mp3"

#     print("speaking.....")

#     pygame.mixer.init()
#     pygame.mixer.music.load(file)
#     pygame.mixer.music.play()

#     while pygame.mixer.music.get_busy():   # till the text finish
#             time.sleep(0.1)

#     pygame.mixer.music.unload()   # to remove the current file to avoid error

# def main():
#     print("*" * 130)
#     print("== Welcome to Text to voice converter App ==".center(100))
#     print("*" * 130)

#     while True:
#         print("1. Covert text to voice")
#         print("2. Exit")
#         choice = input("Enter option: ")
#         match choice:
             
#             case "1":
#                 word = input("Enter what you want to say: ")
#                 try:
#                     while True:
#                         print("1. Hear in English")
#                         print("2. Hear in Arabic")
#                         print("3. Hear in French")
#                         print("4. Hear in Hausa")
#                         choice_1 = input("Enter your option: ")
#                         match choice_1:
#                                 case "1":
#                                     voice(word, "en")
#                                     break
#                                 case "2":
#                                     arabic_word = GoogleTranslator(source= "en", target= "ar").translate(word)
#                                     kind = "ar"
#                                     voice(arabic_word, kind)
#                                     break
#                                 case "3":
#                                     french_word = GoogleTranslator(source= "en", target= "fr").translate(word)
#                                     kind = "fr"
#                                     voice(french_word, kind)
#                                     break
#                                 case "4":
#                                     hausa_word = GoogleTranslator(source= "en", target= "ha").translate(word)
#                                     voice(hausa_word, "ha")
#                                     break
#                                 case _:
#                                     print("Please choose between 1-4")

#                 except exceptions.TooManyRequests:
#                      print("Temporary not available, but english is available")

#                 except tts.gTTSError, requests.exceptions.ConnectionError:
#                      print("Faild to process, check yout network")            
                          

#             case "2":
#                   print("Bye, Hope you enjoyed the app")
#                   quit()
#             case _:
#                   print("Please choose between 1-2")
            


# if __name__ == "__main__":
#      main()