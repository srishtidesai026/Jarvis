import pyttsx3
import eel
import time


# make assistant speak
def speak(text): 
    text = str(text)  
    engine = pyttsx3.init()
    voices = engine.getProperty('voices') # getting details of current voice
    engine.setProperty('voice', voices[1].id) 
    engine.setProperty('rate', 170)
    eel.displayMsg(text)
    print(text)      
    engine.say(text)
    eel.receiverText(text)
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
def allCommands(message = 1):

    ## to differentiate between text and audio inputs
    if message == 1:
        query = takeCommand()
        print(query)
        eel.senderText(query)
    else:
        query = message
        eel.senderText(query)

    try:
        if "open" in query:
            from engine.features import openCommand
            openCommand(query)

        elif "on youtube" in query:
            from engine.features import playYoutube
            playYoutube(query)

        elif "send a message" in query or "voice call" in query or "video call" in query:
            from engine.features import findContact, whatsApp
            contact_no, name = findContact(query)

            if contact_no != 0:
                
                if "send a message" in query:
                    message = "message"
                    speak("what message do you want to send")
                    query = takeCommand()
                elif "voice call" in query:
                    message = 'call'
                else:
                    message = 'video call'
                
            whatsApp(contact_no, query, message, name)
                
        else:
            from engine.features import chatBot
            chatBot(query)
            
    except Exception as e:
        print(e)

    eel.showHood()