import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
from datetime import datetime
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 170)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to voice
def listen_voice():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        return r.recognize_google(audio, language="en-IN").lower()
    except:
        return None

# Function to process commands
def process_command(command):
    if command is None or command == "":
        return "No command received"

    # ---- TIME ----
    if "time" in command:
        return "Time is " + datetime.now().strftime("%H:%M")

    # ---- WEB ----
    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    # ---- WINDOWS SYSTEM ----
    elif "open this pc" in command or "open my computer" in command:
        os.system("explorer")
        return "Opening This PC"

    elif "open downloads" in command:
        os.system("explorer shell:downloads")
        return "Opening Downloads"

    elif "open documents" in command:
        os.system("explorer shell:documents")
        return "Opening Documents"

    elif "open control panel" in command:
        os.system("control")
        return "Opening Control Panel"

    elif "open settings" in command:
        os.system("start ms-settings:")
        return "Opening Settings"

    elif "open calculator" in command:
        os.system("calc")
        return "Opening Calculator"

    elif "open chrome" in command:
        os.system("start chrome")
        return "Opening Chrome"

    # ---- WIKIPEDIA ----
    elif "wikipedia" in command:
        query = command.replace("wikipedia", "")
        try:
            return wikipedia.summary(query, sentences=2)
        except:
            return "No result found"

    # ---- POWER COMMANDS (SAFE) ----
    elif "shutdown" in command:
        return "Shutdown command detected. Please confirm manually."

    elif "restart" in command:
        return "Restart command detected. Please confirm manually."

    # ---- PERSONAL QUESTIONS ----
    elif "who is your creator" in command or "who created you" in command:
        return "I was created by Nusaik Ahamath, a data science student from Sri Lanka."

    elif "what can you do" in command or "tell me about yourself" in command:
        return ("I am SARA, a hybrid AI assistant. "
                "I can open websites like Google and YouTube, "
                "system folders like This PC, Downloads, Documents, "
                "Windows apps like Calculator, Control Panel, Settings, "
                "search Wikipedia, tell time, and respond to voice or text commands.")

    elif "what files can you open" in command or "what can you open" in command:
        return ("I can open Google, YouTube, Chrome browser, This PC, Downloads folder, "
                "Documents folder, Calculator, Control Panel, and Windows Settings.")

    # ---- EXIT ----
    elif "stop" in command or "exit" in command:
        return "exit"

    else:
        return "Command not recognized"
