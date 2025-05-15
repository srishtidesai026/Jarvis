import os
import re
from shlex import quote
import sqlite3
import struct
import subprocess
import time
import webbrowser
import hugchat as hugchat
from playsound import playsound
import eel
import pyaudio
import pyautogui
from engine.commands import speak
from engine.config import ASSISTANT_NAME
import pywhatkit as kit
import pvporcupine

from engine.helper import extract_yt_term, remove_words
from hugchat import hugchat

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

## hotword detection
def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        porcupine=pvporcupine.create(keywords=["Mouse"])
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


# finding contact from database
def findContact(query):

    words_to_remove = ['make', 'a', 'phone', 'call', 'video', 'to', 'send', 'message', 'start', 'voice', 'with','whatsapp']
    query = remove_words(query, words_to_remove)
    
    try:
        query = query.strip().lower() 
        cursor.execute('SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE  ? or LOWER(name) LIKE ?', ('%' + query + '%', query + '%'))
        result = cursor.fetchall()
        print(result[0][0])
        mobile_no_str = str(result[0][0])
        if not mobile_no_str.startswith('+91'):
            mobile_no_str = '+91' + mobile_no_str
        
        return mobile_no_str, query
    
    except:
        speak("does not exist in your contacts")
        return 0, 0
    



# import os
# import time
# import pyautogui
# from urllib.parse import quote

# # Define the correct image path
# BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get current script directory
# IMAGE_PATH = os.path.join(BASE_DIR, "www", "assets", "texllate", "images")  # Full image folder path

# def click_icon(image_name, confidence=0.8):
#     """Locate an image in the specified folder and click it."""
#     image_path = os.path.join(IMAGE_PATH, image_name)

#     if not os.path.exists(image_path):
#         print(f"Error: {image_path} does not exist.")
#         return False

#     location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
    
#     if location:
#         pyautogui.click(location)
#         return True
#     else:
#         print(f"Could not find {image_name} on screen.")
#         return False

# def whatsApp(mobile_no, message, flag, name):
#     # Encode message into a URL
#     encoded_message = quote(message)
#     print(f"Encoded message: {encoded_message}")

#     # Construct WhatsApp URL
#     whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

#     # Open WhatsApp with the constructed URL
#     os.system(f'start "" "{whatsapp_url}"')
#     time.sleep(5)  # Wait for WhatsApp to load

#     if flag == 'message':
#         success = click_icon("send_icon.png")  # Click send button
#         if success:
#             speak(f"Message sent successfully to {name}")
#         else:
#             speak(f"Message could not be sent to {name}")

#     elif flag == 'call':
#         success = click_icon("call_icon.png")  # Click voice call button
#         if success:
#             speak(f"Calling {name}")
#         else:
#             speak(f"Could not start call with {name}")

#     elif flag == 'video':
#         success = click_icon("video_icon.png")  # Click video call button
#         if success:
#             speak(f"Starting a video call with {name}")
#         else:
#             speak(f"Could not start video call with {name}")

#     else:
#         print("Invalid flag provided.")




def whatsApp(mobile_no, message, flag, name):

    if flag == 'message':
        # no of times 'tab' key needs to be pressed
        target_tab = 3
        assis_msg = "message sent successfully to " + name

    elif flag == 'call':
        target_tab = 13
        message = ''
        assis_msg = "calling " + name

    else:
        target_tab = 12
        message = ''
        assis_msg = "starting a video call with " + name

    
    # encode mesaage into url
    encoded_message = quote(message)
    print(encoded_message)

    # construct url using the message
    whatsapp_url = f"whatsapp://send?phone={mobile_no}&text={encoded_message}"

    # construct full command
    full_command = f'start "" "{whatsapp_url}"'

    # wait for whatsapp to load
    time.sleep(4)

    subprocess.run(full_command, shell=True)
    time.sleep(5)
    subprocess.run(full_command, shell=True)

    pyautogui.hotkey('ctrl','f')

    for i in range(1, target_tab):
        pyautogui.hotkey('tab')
        time.sleep(1)

    pyautogui.hotkey('enter')
    speak(assis_msg)


# ai chatbot
def clean_response(text):
    # Remove markdown formatting characters
    return re.sub(r'[*_`~]', '', text).strip()

def chatBot(query):
    try:
        user_input = query.lower()
        chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
        id = chatbot.new_conversation()
        chatbot.change_conversation(id)
        response = chatbot.chat(user_input)

        cleaned_response = clean_response(str(response))
        print(cleaned_response)
        speak(cleaned_response)
        return cleaned_response

    except Exception as e:
        print(e)


# import re

# def clean_response(text):
#     """ Remove markdown formatting (like *, _, ~, `) """
#     return re.sub(r'[*_`~]', '', text).strip()

# def format_numbered_text(text):
#     """ Convert text into numbered list format for HTML """
#     lines = text.strip().split('\n')
#     html_lines = ['<ol>']
#     for line in lines:
#         if line.strip():
#             cleaned_line = re.sub(r'^\d+\.\s*', '', line)  # Remove any existing numbered points
#             html_lines.append(f'<li>{cleaned_line}</li>')
#     html_lines.append('</ol>')
#     return '\n'.join(html_lines)

# def preserve_linebreaks(text):
#     """ Convert line breaks into <br> tags """
#     return text.replace('\n', '<br>')

# def chatBot(query):
#     try:
#         user_input = query.lower()
#         chatbot = hugchat.ChatBot(cookie_path="engine\\cookies.json")
#         id = chatbot.new_conversation()
#         chatbot.change_conversation(id)
#         response = chatbot.chat(user_input)

#         cleaned_response = clean_response(str(response))
#         formatted_response = format_numbered_text(cleaned_response)  # You can also use preserve_linebreaks() instead

#         print(formatted_response)
#         eel.receiverText(formatted_response)  # Send HTML to frontend
#         speak(cleaned_response)  # Optional: speak the cleaned response

#         return formatted_response

#     except Exception as e:
#         print(e)

