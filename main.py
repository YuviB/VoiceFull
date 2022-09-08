import speech_recognition as sr
import pyttsx3
import pywhatkit



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
    elif 'hello' or 'hey'in command:
        speak("Hello, How can I help")

    else:
        speak('Please say the command again.')


while True:
    run_atlas()