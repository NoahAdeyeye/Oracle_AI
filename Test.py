import pyaudio
import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Say something...")
    audio = r.listen(source, timeout=5)

try:
    recognized_text = r.recognize_google(audio)
    print("You said: " + recognized_text)
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError as e:
    print("Error making the request; {0}".format(e))

