import pyttsx3
import eel
import time


# make assistant speak
def speak(text):   
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') # getting details of current voice
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 170)
    eel.displayMsg(text)
    print(text)       
    engine.say(text)
    engine.runAndWait()



import speech_recognition as sr


# listen to me
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        eel.displayMsg("listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, 10, 6)

    try:
        print("recognizing...")
        eel.displayMsg("recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"you : {query}")
        eel.displayMsg(query)
        time.sleep(2)

    except Exception as e:
        return ""
    
    return query.lower()


@eel.expose
def allCommands():
    try:
        query = takeCommand()
        print(query)

        if "open" in query:
            from engine.features import openCommand
            openCommand(query)
        elif "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query)
        else:
            print("not run")
    except:
        print("Error!")

    eel.showHood()