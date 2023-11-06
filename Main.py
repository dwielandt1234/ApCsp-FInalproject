import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

#define voice variables, create a microphone
Reco = spr.Recognizer()
micro = spr.Microphone()
#capture the voice 
with mc as source:
  print("Hey Please say 'Hello' in order to start the Recognizion")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
  Reco.adjust_for_ambient_noise(source, duration=0.2)
  audio = Reco.listen(source) 
  Mytext = Reco.recognize_google(audio) 

#this will ask the user if what we have is what he said
print("You said: ", Mytext)
fcheck = input("Is this correct? (y/n): ")
