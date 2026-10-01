import pygame
from gtts import gTTS
from gtts import tts
import time
import requests

def translate_text(word, target):

    url = "https://api.mymemory.translated.net/get"
    translate_word = {
        "q": word,
        "langpair": f"en|{target}"          # the api understands "q" as the key to contain the word and "langpair" for convertion
    }

    response = requests.get(url, params=translate_word)  # saves the translated word in dicitonary form

    response.raise_for_status()   

    data = response.json()                     #json() is the data type that python is fimilar with and work with dictionary, so we save the resoponse there


# now we have something like data = {"responseData":{"translatedText", response}} # here response is the translated word
    return data["responseData"]["translatedText"]     # now data is dictionary, and the word is saved in a key that is a value to "responseData" called "translatedText"


def voice(word, kind):

    voice = gTTS(
        text=word,
        lang=kind
    )

    voice.save("Audio1.mp3")

    file = "Audio1.mp3"

    print("Speaking.....")

    pygame.mixer.init()

    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    pygame.mixer.music.unload()
    pygame.mixer.quit()


def main():

    print("*" * 130)
    print("== Welcome to Text to Voice Converter App ==".center(100))
    print("*" * 130)

    while True:
      # just trying module knowdledge

        print("1. Convert text to voice")
        print("2. Exit")

        choice = input("Enter option: ")

        match choice:

            case "1":

                word = input("Enter what you want to say: ")

                while True:

                    print("1. Hear in English")
                    print("2. Hear in Arabic")
                    print("3. Hear in French")
                    print("4. Hear in Hausa")
                    print("5. Back")

                    choice_1 = input("Enter your option: ")

                    try:

                        match choice_1:

                            case "1":

                                voice(word, "en")
                                
                            case "2":

                                arabic_word = translate_text(
                                    word,
                                    "ar"
                                )

                                print("Arabic:", arabic_word)

                                voice(
                                    arabic_word,
                                    "ar"
                                )

                            case "3":

                                french_word = translate_text(
                                    word,
                                    "fr"
                                )

                                print("French:", french_word)

                                voice(
                                    french_word,
                                    "fr"
                                )

                            case "4":

                                hausa_word = translate_text(
                                    word,
                                    "ha"
                                )

                                print("Hausa:", hausa_word)

                                voice(
                                    hausa_word,
                                    "ha"
                                )

                            case "5":

                                break

                            case _:

                                print("Please choose between 1-5")

                    except requests.exceptions.ConnectionError:

                        print(
                            "Failed to connect to the translation "
                            "or text-to-speech service."
                        )

                    except requests.exceptions.HTTPError as error:

                        print(
                            "Translation service returned an error:",
                            error
                        )

                    except tts.gTTSError:

                        print(
                            "Text-to-speech failed. "
                            "Check your internet connection."
                        )

                    except Exception as error:

                        print("Something went wrong:", error)

                    if choice_1 == "5":
                        break

            case "2":
                voice("Bye, see you later", "en")
                print("Bye, Hope you enjoyed the app!")
                break

            case _:

                print("Please choose between 1-2")


if __name__ == "__main__":
    main()



















