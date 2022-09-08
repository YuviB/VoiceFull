import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime


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
