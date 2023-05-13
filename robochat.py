# for mac operating system
# import os

# if __name__ == '__main__':
#     print("Welcome to chatboat 1.2 created by parmeshwar")
#     while True:
#         x = input("Enter what you want to speak")
#         if x == 'q':
#             os.system("say 'bye bye friend'")
#             break
#         comand = f"say {x}"
#         os.system(comand)

# for window operating system
import pyttsx3
if __name__ == '__main__':
    text_to_speech = pyttsx3.init()
    while(True):
        word = input("Enter your command: ")
        if word == 'q':
            break
        text_to_speech.say(word)
        text_to_speech.runAndWait()
