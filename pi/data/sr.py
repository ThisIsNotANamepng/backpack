import speech_recognition as sr
import pyaudio
import os

r = sr.Recognizer()


with sr.Microphone() as source:
    print("Say something!")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout=2)

print("Done recording----------------------")

os.system('mpg123 computer-ready.mp3')
print("All done")


print("Whisper thinks you said " + r.recognize_whisper(audio, language="english"))
