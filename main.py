import os
import eel
from engine.features import *
from engine.commands import *
from engine.auth import recognize

def start():
    
    eel.init("www")
    playAssistantSound()

    @eel.expose
    def init():

        eel.hideLoader()
        speak("Ready for Face Authentication...")

        flag = recognize.AuthenticateFace()
        if(flag==1):
            eel.hideFaceAuth()
            speak("Face Authentication Successful!")
            eel.hideFaceAuthSuccess()
            speak("Hi Srishti! I'm Mai, your desktop assistant, how can I help you today?")
            playAssistantSound()
            eel.hideStart()
        else:
            speak("Face Authentication Failed!")
    
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    
    eel.start('index.html', mode=None, host = 'localhost', block=True)
