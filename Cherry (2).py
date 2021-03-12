import speech_recognition as s
from gtts import gTTS
import os

sr = s.Recognizer()
print('hey i m listening to you')
with s.Microphone() as m:
    audio = sr.listen(m)
try:
    query = sr.recognize_google(audio,language='eng-in')
    print(query)
except:
    print('sorry couldnt recognise your voice')