import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import time
import os
import webbrowser
global t
#timer function

#f.write(r"C:\PythonData\usercheck.txt", "a")

with open(r"C:\PythonData\usercheck.txt", "w") as f:
    f.write(" ")

#read

#with open(r"C:\PythonData\usercheck.txt", "r") as f:
  # print("New text:\n",f.read())

#append

with open(r"C:\PythonData\usercheck.txt", "a") as f:
    f.write("\n 1")


#read the appended text

#with open(r"C:\PythonData\usercheck.txt", "r") as f:
   # print("Append:\n",f.read())



with open(r"C:\PythonData\usercheck.txt", "r") as f:
    pull_user_check = open(r"C:\PythonData\usercheck.txt")


print(pull_user_check)
if " 1" in pull_user_check:

    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


    def speak(text):
        engine.say(text)
        engine.runAndWait()


    def command_input_test():
        try:
            with sr.Microphone() as source:
                print('listening...')
                speak("Hello, I am ready for my next command")
                voice = listener.listen(source)
                command = listener.recognize_google(voice)
                command = command.lower()
                if 'atlas' in command:
                    command = command.replace('atlas', '')
                    print(command)
        except:
            pass
        return command


    def run_atlas():
        command = command_input_test()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'timer' in command:
            print("Opening Timer")
            os.startfile("C:\\Users\\Yuvi\\PycharmProjects\\Voice\\timer.py")


        elif "exit" in command:
            exit()


        elif 'to do list' in command:
            speak("opening to do list")
            os.startfile("C:\\Users\\Yuvi\\PycharmProjects\\Voice\\To-Do-List.py")

        elif "Hello" in command:
            speak("Hello, its a pleasure to be here")
            run_atlas()

        elif "who is " in command:
            wikipedia.search(command)
            speak(wikipedia.summary(command))

        elif 'workspaces' in command:
            speak('Sure thing, what workspace shall I open. ')
            try:
                with sr.Microphone() as source:
                    print('listening for workspace...')
                    voice = listener.listen(source)
                    workspacecommand = listener.recognize_google(voice)
                    workspacecommand = command.lower()
                    if 'math' in workspacecommand:

                        webbrowser.open('http://www.google.com/math')
                        webbrowser.open("https://classroom.google.com/u/0/w/NDUwNDA4Nzc4MjU2/t/all")

                    elif "english" in workspacecommand:
                        webbrowser.open("https://classroom.google.com/u/0/c/NDUwNDA4NjY3MzY2")
                        webbrowser.open('http://www.google.com/Google Drive')

                    elif "tech " in workspacecommand:
                        webbrowser.open("https://classroom.google.com/u/0/c/NDUwNDA4NzE0NjMz")

                    elif "none" in workspacecommand:

                        run_atlas()
            except:
                pass
            return command








        else:
            speak('Please say the command again.')



    while True:
        run_atlas()



else:
    print("Hmm it seems you arent signed in, open the sign in file to gain acssess")



    #Help from Programming Hero on Youtube
