import pyttsx3
import pyjokes
import wikipedia
import webbrowser
import pywhatkit
import os
from datetime import datetime

engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

talk("Welcome to the Voice Assistant.")

time = datetime.now().strftime("%I:%M %p")
talk(f"The current time is {time}.")

today = datetime.now().strftime("%A, %B %d, %Y")
talk(f"Today is {today}.")

talk(pyjokes.get_joke())

result = wikipedia.summary("Python programming language", sentences=2)
talk(result)

webbrowser.open("https://www.google.com")
webbrowser.open("https://www.youtube.com")

pywhatkit.search("Artificial Intelligence")
pywhatkit.playonyt("Believer")

os.system("notepad.exe")

def start_listening():
    status.configure(text="Status: Listening...")
    threading.Thread(target=run_assistant, args=(add_message, ), daemon=True).start()