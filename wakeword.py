import os

import speech_recognition as sr
import pyttsx3

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

global x
x = 50

def speak(text):
    engine.say(text)
    engine.runAndWait()


def command_input_test():
    try:
        with sr.Microphone() as source:
            print('listening for wake word...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Hey Atlas' or "hey atlas" in command:
                command.lower(command)

    except:
        pass
    return command


def wakeword():
    command = command_input_test()
    print(command)
    if 'hey atlas' in command:
        os.startfile("C:\\Users\\Yuvi\\PycharmProjects\\Voice\\main.py")



    elif 'exit' in command:
        exit()


    else:
        speak(' ')


while True:
        wakeword()



else:
    print("Hmm it seems you arent signed in, open the sign in file to gain acssess")






