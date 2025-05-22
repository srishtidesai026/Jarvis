import os
import eel
from engine.features import *
from engine.commands import *
from engine.auth import recognize

def start():
    
    eel.init("www")

    playAssistantSound()
    flag = recognize.AuthenticateFace()
    
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    
    eel.start('index.html', mode=None, host = 'localhost', block=True)
