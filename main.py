import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime

#global user_check

#f.write(r"C:\PythonData\usercheck.txt", "a")

with open(r"C:\PythonData\usercheck.txt", "w") as f:
    f.write(" ")

#read

with open(r"C:\PythonData\usercheck.txt", "r") as f:
   print("New text:\n",f.read())

#append

with open(r"C:\PythonData\usercheck.txt", "a") as f:
    f.write("\n This text was added using Append.")


#read the appended text

with open(r"C:\PythonData\usercheck.txt", "r") as f:
    print("Append:\n",f.read())

with open(r"C:\PythonData\usercheck.txt", "r") as f:
    pull_user_check = open(r"C:\PythonData\usercheck.txt")


print(pull_user_check)
if "User Signed in = 1" in pull_user_check:





    listener = sr.Recognizer()
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)


    def speak(text):
        engine.say(text)
        engine.runAndWait()


    def take_command():
        try:
            with sr.Microphone() as source:
                print('listening...')
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
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            speak('The time is ' + time)


        elif 'Workspaces' and 'Open' in command:
            speak('Sure thing, what workspace shall I open. ')

        elif 'exit' in command:
            exit()

        else:
            speak('Please say the command again.')


    while True:
        run_atlas()



else:
    print("Hmm it seems you arent signed in, open the sign in file to gain acssess")
