import speech_recognition as sr
from openai import OpenAI
import tempfile
import pygame

client = OpenAI()
recognizer = sr.Recognizer()
pygame.mixer.init()


def speak(text):
    print("Bot:", text)

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
        filename = f.name

    audio = client.audio.speech.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text
    )

    audio.stream_to_file(filename)

    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue

def listen():
    with sr.Microphone() as source:
        print("Listening... (speak now)")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)

        try:
            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=6
            )
        except sr.WaitTimeoutError:
            return ""

        try:
            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text.lower()

        except sr.UnknownValueError:
            return ""

        except sr.RequestError:
            print("Speech service error")
            return ""

        except Exception as e:
            print("Mic error:", e)
            return ""
def ask_gpt(prompt):

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Reply in short, max 1-2 sentences."},
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
