#Without function not reusable

type = input("Enter your messsage: ")
words = type.split(" ")
emoji = {":)":"😊",":(":"😔"}
output = ""
for word in words:
    output += emoji.get(word, word) + " "
print(output)

#With function  reusable#
#message = input("Enter your message: ") here
def emoji_converter(message):
    words = message.split(" ")
    emoji = {":)":"😊",":(":"😔"}
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input("Enter your message: ") #or here
emoji = emoji_converter(message)
print(f"The message: {emoji}")
