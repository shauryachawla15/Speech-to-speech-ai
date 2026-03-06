import speech_recognition as sr
import pyttsx3
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text

        except:
            return ""


def ask_gpt(prompt):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content


speak("AI assistant started")

while True:

    command = listen()

    if command == "":
        continue

    if "exit" in command.lower():
        speak("Goodbye")
        break

    response = ask_gpt(command)

    speak(response)