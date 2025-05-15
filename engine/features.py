import os
import re
import sqlite3
import struct
import time
import webbrowser
from playsound import playsound
import eel
import pyaudio
from engine.commands import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import pvporcupine

from engine.helper import extract_yt_term

con = sqlite3.connect("mai.db")
cursor = con.cursor()

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\texllate\\audio\\start_sound.mp3"
    playsound(music_dir)


def openCommand(query):
    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip().lower()

    if app_name != "":

        try:
            cursor.execute(
                "SELECT path FROM sys_command WHERE name IN (?)", (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening " + query)
                os.startfile(results[0][0])    # results is returned as tuple

            elif len(results) == 0:
                cursor.execute(
                    "SELECT url FROM web_command WHERE name IN (?)", (app_name,))
                results = cursor.fetchall()

                if len(results) != 0:
                    speak("Opening " + query)
                    webbrowser.open(results[0][0])

                else:
                    speak("Opening " + query)
                    try:
                        os.system('start' + query)  # opening app via command prompt 
                    except:
                        speak("not found")
        
        except:
            speak("something went wrong")


def playYoutube(query):
    search_term = extract_yt_term(query)
    speak("playing " + search_term + " on Youtube")
    kit.playonyt(search_term)


def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        porcupine=pvporcupine.create(keywords=["grapefruit"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels =1, format = pyaudio.paInt16, input= True, frames_per_buffer=porcupine.frame_length )

        # keep checking for mai keyword
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)

            keyword_index = porcupine.process(keyword)

            if keyword_index == 0:
                print("hotword detected")

                # process keyboard shortcut
                import pyautogui as autogui
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")

    except:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()