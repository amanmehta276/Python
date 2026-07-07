import speech_recognition as sr
import pyttsx3
import webbrowser

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Speed of speech

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Recognize speech from the microphone."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for background noise
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.UnknownValueError:
            speak("Sorry, I didn't understand.")
            return ""
        except sr.RequestError:
            speak("Could not connect to the internet.")
            return ""

# Main loop
if __name__ == "__main__":
    speak("Hello! How can I help you?")
    while True:
        command = listen()
        if "exit" in command or "bye" in command:
            speak("Goodbye! Have a great day!")
            break
        elif "your name" in command:
            speak("My name is Vyom. I am your AI assistant bro.")
        elif "how are you" in command:
            speak("I am doing great! How about you?")
        else:
            speak("Sorry, I don't understand that command.")