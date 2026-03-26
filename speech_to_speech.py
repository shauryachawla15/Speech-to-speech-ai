import speech_recognition as sr
import pyttsx3

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )
        except sr.WaitTimeoutError:
            print("No speech detected")
            return ""

        try:
            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text.lower()

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            print("API error")
            return ""

def process_command(command):

    if "hello" in command:
        return "Hello! How can I help you?"

    elif "your name" in command:
        return "I am your Python voice assistant."

    elif "time" in command:
        from datetime import datetime
        return f"The time is {datetime.now().strftime('%H:%M')}"

    elif "exit" in command or "stop" in command:
        return "Goodbye"

    else:
        return "I didn't understand that."

# Main loop
speak("Voice assistant started")

while True:
    command = listen()

    if command == "":
        continue

    response = process_command(command)
    speak(response)

    if "goodbye" in response.lower():
        break
