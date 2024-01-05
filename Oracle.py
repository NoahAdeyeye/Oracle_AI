import os
import time
import pyaudio
import speech_recognition as sr
from gtts import gTTS
import openai
import pyttsx3

api_key = ""

lang = 'en'

openai.api_key = api_key

guy = ""

while True:
    def get_audio():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=1)  # Adjust the duration for ambient noise
            audio = r.listen(source, phrase_time_limit=10, timeout=5)  # Adjust phrase_time_limit and timeout
            said = ""

            try:
                said = r.recognize_google(audio)
                print(said)
                global guy
                guy = said

                if "Friday" in said:
                    words = said.split()
                    new_string = ' '.join(words[1:])
                    print(new_string)
                    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": said}])
                    text = completion.choices[0].message['content']
                    speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
                    speech.save("welcome1.mp3")

                    # Use pyttsx3 for text-to-speech
                    engine = pyttsx3.init()
                    engine.setProperty('rate', 150)  # Adjust the speech rate (words per minute)
                    engine.setProperty('volume', 1.0)  # Adjust the volume (0.0 to 1.0)
                    engine.say(text)
                    engine.runAndWait()
            except Exception:
                print("Exception")

        return said

    if "stop" in guy:
        break

    get_audio()





