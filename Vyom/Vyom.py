"""
╔══════════════════════════════════════════════════════╗
║          Vyom - Personal AI Voice Assistant          ║
║         Built by Aman Mehta | VyomsTech              ║
╚══════════════════════════════════════════════════════╝

"""

import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import sys
import time
import subprocess
import json

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False


# ─────────────────────────────────────────────
#  CONFIGURATION
# ─────────────────────────────────────────────

ASSISTANT_NAME   = "Vyom"
WAKE_WORD        = "vyom"            # Say this to activate
OPENWEATHER_KEY  = " "        # Optional: paste your free key from openweathermap.org
DEFAULT_CITY     = "Raipur"         # Your city for weather

# Shortcuts — add/remove as you like
WEBSITES = {
    "youtube"    : "https://youtube.com",
    "google"     : "https://google.com",
    "github"     : "https://github.com",
    "instagram"  : "https://instagram.com",
    "twitter"    : "https://twitter.com",
    "x"          : "https://twitter.com",
    "facebook"   : "https://facebook.com",
    "linkedin"   : "https://linkedin.com",
    "reddit"     : "https://reddit.com",
    "netflix"    : "https://netflix.com",
    "spotify"    : "https://open.spotify.com",
    "chatgpt"    : "https://chat.openai.com",
    "claude"     : "https://claude.ai",
    "amazon"     : "https://amazon.in",
    "flipkart"   : "https://flipkart.com",
    "vyoms2tech" : "https://vyomtech.netlify.app",
    "gmail"      : "https://mail.google.com",
    "maps"       : "https://maps.google.com",
}


# ─────────────────────────────────────────────
#  TEXT-TO-SPEECH ENGINE
# ─────────────────────────────────────────────

engine = pyttsx3.init()

def setup_voice():
    voices = engine.getProperty("voices")
    engine.setProperty("rate", 175)       # Speed (words/min)
    engine.setProperty("volume", 1.0)

    # Try to find an English voice
    for v in voices:
        if "english" in v.name.lower() or "en_" in v.id.lower():
            engine.setProperty("voice", v.id)
            break

setup_voice()

def speak(text: str):
    """Convert text to speech."""
    print(f"\n🤖 {ASSISTANT_NAME}: {text}")
    engine.say(text)
    engine.runAndWait()


# ─────────────────────────────────────────────
#  SPEECH RECOGNITION
# ─────────────────────────────────────────────

recognizer = sr.Recognizer()
recognizer.pause_threshold = 1.0
recognizer.energy_threshold = 300

def listen(timeout: int = 5, phrase_limit: int = 8) -> str:
    """Listen from microphone and return recognized text (lowercase)."""
    with sr.Microphone() as source:
        print("\n🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        try:
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
            text  = recognizer.recognize_google(audio, language="en-IN")
            print(f"👤 You said: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("Speech service is unavailable. Check your internet.")
            return ""


# ─────────────────────────────────────────────
#  FEATURE HANDLERS
# ─────────────────────────────────────────────

def open_website(site_name: str) -> bool:
    """Open a known website by keyword."""
    for key, url in WEBSITES.items():
        if key in site_name:
            speak(f"Opening {key}.")
            webbrowser.open(url)
            return True
    return False

def youtube_search(query: str):
    """Search YouTube for a query."""
    search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
    speak(f"Searching YouTube for {query}.")
    webbrowser.open(search_url)

def google_search(query: str):
    """Google search."""
    search_url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    speak(f"Googling {query}.")
    webbrowser.open(search_url)

def get_time() -> str:
    now = datetime.datetime.now()
    return now.strftime("%I:%M %p")

def get_date() -> str:
    now = datetime.datetime.now()
    return now.strftime("%A, %d %B %Y")

def get_weather(city: str = DEFAULT_CITY) -> str:
    if not REQUESTS_AVAILABLE:
        return "Requests library not installed. Run: pip install requests"
    if not OPENWEATHER_KEY:
        return "Weather API key not set. Add your OpenWeatherMap key in config."
    try:
        url  = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_KEY}&units=metric"
        data = requests.get(url, timeout=5).json()
        if data.get("cod") != 200:
            return f"Could not get weather for {city}."
        temp  = data["main"]["temp"]
        desc  = data["weather"][0]["description"]
        feels = data["main"]["feels_like"]
        return f"In {city}, it is {temp}°C with {desc}. Feels like {feels}°C."
    except Exception:
        return "Could not fetch weather. Check your internet or API key."

def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None — that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "I told my computer I needed a break. Now it won't stop sending me Kit-Kat ads.",
        "There are 10 types of people — those who understand binary, and those who don't.",
    ]
    import random
    return random.choice(jokes)

def open_app(app_name: str):
    """Try to open common desktop apps."""
    apps = {
        "notepad"     : "notepad.exe",
        "calculator"  : "calc.exe",
        "paint"       : "mspaint.exe",
        "vs code"     : "code",
        "vscode"      : "code",
        "file manager": "explorer.exe",
        "explorer"    : "explorer.exe",
        "cmd"         : "cmd.exe",
        "terminal"    : "cmd.exe",
        "task manager": "taskmgr.exe",
    }
    for key, cmd in apps.items():
        if key in app_name:
            try:
                speak(f"Opening {key}.")
                subprocess.Popen(cmd, shell=True)
                return True
            except Exception:
                speak(f"Could not open {key}.")
                return True
    return False

def volume_control(cmd: str):
    """Basic volume control on Windows."""
    if "mute" in cmd:
        os.system("nircmd.exe mutesysvolume 1")   # needs nircmd
        speak("Volume muted.")
    elif "unmute" in cmd:
        os.system("nircmd.exe mutesysvolume 0")
        speak("Volume unmuted.")
    elif "volume up" in cmd:
        speak("Turning volume up.")
        for _ in range(5):
            os.system("nircmd.exe changesysvolume 4000")
    elif "volume down" in cmd:
        speak("Turning volume down.")
        for _ in range(5):
            os.system("nircmd.exe changesysvolume -4000")

def system_control(cmd: str):
    """Shutdown / restart / sleep."""
    if "shutdown" in cmd or "shut down" in cmd:
        speak("Shutting down your PC in 5 seconds.")
        os.system("shutdown /s /t 5")
    elif "restart" in cmd or "reboot" in cmd:
        speak("Restarting your PC in 5 seconds.")
        os.system("shutdown /r /t 5")
    elif "sleep" in cmd:
        speak("Putting your PC to sleep.")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
    elif "cancel" in cmd:
        os.system("shutdown /a")
        speak("Shutdown cancelled.")


# ─────────────────────────────────────────────
#  COMMAND ROUTER
# ─────────────────────────────────────────────

def process_command(cmd: str):
    """Route a voice command to the correct handler."""

    # ── Time & Date ──────────────────────────
    if "time" in cmd:
        speak(f"The time is {get_time()}.")

    elif "date" in cmd or "today" in cmd:
        speak(f"Today is {get_date()}.")

    # ── Greetings ────────────────────────────
    elif any(w in cmd for w in ["hello", "hi", "hey"]):
        speak(f"Hello! I'm {ASSISTANT_NAME}, your personal assistant. How can I help?")

    elif "how are you" in cmd:
        speak("I'm fully operational and ready to assist you!")

    # ── YouTube ──────────────────────────────
    elif "play" in cmd and "youtube" in cmd:
        query = cmd.replace("play", "").replace("on youtube", "").replace("youtube", "").strip()
        if query:
            youtube_search(query)
        else:
            speak("What do you want me to play on YouTube?")
            query = listen()
            if query:
                youtube_search(query)

    elif "open youtube" in cmd or "youtube" in cmd:
        speak("Opening YouTube.")
        webbrowser.open("https://youtube.com")

    # ── Google Search ────────────────────────
    elif "search" in cmd or "google" in cmd:
        query = (cmd.replace("search", "")
                    .replace("google", "")
                    .replace("for", "")
                    .strip())
        if not query:
            speak("What should I search?")
            query = listen()
        if query:
            google_search(query)

    # ── Open Websites ────────────────────────
    elif "open" in cmd:
        site = cmd.replace("open", "").strip()
        if not open_website(site):
            if not open_app(site):
                speak(f"I don't know how to open {site}.")

    # ── Weather ──────────────────────────────
    elif "weather" in cmd:
        city = DEFAULT_CITY
        if "in " in cmd:
            city = cmd.split("in ")[-1].strip()
        speak(get_weather(city))

    # ── Joke ─────────────────────────────────
    elif "joke" in cmd:
        speak(tell_joke())

    # ── System Controls ──────────────────────
    elif any(w in cmd for w in ["shutdown", "shut down", "restart", "reboot", "sleep"]):
        system_control(cmd)

    elif "cancel" in cmd and "shutdown" in cmd:
        system_control("cancel")

    # ── Volume ───────────────────────────────
    elif any(w in cmd for w in ["mute", "unmute", "volume up", "volume down"]):
        volume_control(cmd)

    # ── Goodbye ──────────────────────────────
    elif any(w in cmd for w in ["bye", "goodbye", "exit", "quit", "stop"]):
        speak("Goodbye! Have a great day!")
        sys.exit(0)

    # ── Help ─────────────────────────────────
    elif "help" in cmd or "what can you do" in cmd:
        help_text = (
            "I can: tell the time and date, search Google and YouTube, "
            "open websites like YouTube Google GitHub Instagram and more, "
            "open desktop apps like VS Code and Notepad, "
            "check the weather, tell jokes, control system shutdown or restart. "
            "Just ask!"
        )
        speak(help_text)

    # ── Fallback → Google it ─────────────────
    else:
        speak(f"I'm not sure about that. Let me Google it for you.")
        google_search(cmd)


# ─────────────────────────────────────────────
#  WAKE-WORD MODE  vs  ALWAYS-ON MODE
# ─────────────────────────────────────────────

def run_always_on():
    """Listen for commands continuously without a wake word."""
    speak(f"Hello! I'm {ASSISTANT_NAME}. I'm listening. Say 'help' to see what I can do.")
    while True:
        cmd = listen(timeout=10, phrase_limit=10)
        if cmd:
            process_command(cmd)
        time.sleep(0.3)


def run_wake_word():
    """Wait for the wake word, then process a command."""
    print(f"\n🔵 Waiting for wake word: '{WAKE_WORD.upper()}'  |  Ctrl+C to exit\n")
    while True:
        trigger = listen(timeout=10, phrase_limit=3)
        if WAKE_WORD in trigger:
            speak("Yes? How can I help?")
            cmd = listen(timeout=8, phrase_limit=10)
            if cmd:
                process_command(cmd)
        time.sleep(0.2)


# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────

if __name__ == "__main__":
    print("╔══════════════════════════════════════════════════════╗")
    print("║          Vyom - Personal AI Voice Assistant          ║")
    print("║              VyomsTech | Aman Mehta                  ║")
    print("╚══════════════════════════════════════════════════════╝")
    print()
    print("Choose mode:")
    print("  1 → Always-on (every sentence is a command)")
    print("  2 → Wake-word mode (say 'Vyom' first)")
    print()

    mode = input("Enter 1 or 2 (default 1): ").strip()

    try:
        if mode == "2":
            run_wake_word()
        else:
            run_always_on()
    except KeyboardInterrupt:
        speak("Shutting down. Goodbye!")
        sys.exit(0)