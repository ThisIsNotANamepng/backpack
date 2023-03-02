print("Pocket Assistant Starting....")
#Imports
import datetime
import speech_recognition as sr
#from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play
#import RPi.GPIO as GPIO
import os
import pytz
from base64 import b64encode, b64decode
import hashlib
from AesEverywhere import aes256
import json
import pathlib
import random
from pydub import AudioSegment
import random
import string
import time
#import pyaudio
import calendar
from playsound import playsound
import pygame
import firstaid

print("Imports complete")
#r = sr.Recognizer()

#mic = sr.Microphone()

pygame.init()
pygame.mixer.music.load("backpack/pi/data/beep.mp3")
timeout = 1

#Functions
global voice
voice = "picard"
#tts = TTS(model_name="tts_models/en/ljspeech/overflow", progress_bar=False)
#print("TTS Model Ready")
def log(todo):
  #open a log file and log command, hopefully the full command and not just todo
  current_time = datetime.datetime.now(pytz.timezone('America/Chicago'))

  f = open("assistant.log", "a")
  f.write(str(current_time)+" : "+todo+"\n")
  f.close()

def getButton(type):
  print(type)
  if (type=="bool"):
    print("Listening for boolean")
    m = input("Dev. Listening for bool: ")
    if (m=="t"):
      return(True)
    else:
      return(False)

  #Accept a type - boolean, 
  #Listen for button pushes
def speak(command):
  print("saying:", command)

  global old_command
  old_command = command
  filename = command.replace(" ", "")+".wav"
  if filename in os.listdir("backpack/pi/data/sounds/On-Device"):
    os.system("mpg123 "+filename)
  else:

  #  print(command)
  #  tts.tts_to_file(text=command, file_path=filename)
  #  song = AudioSegment.from_wav("new.wav")
  #  play(song)  
    print("mimic3 --voice 'en_US/hifi-tts_low' --interactive '"+command+"' | aplay")
    os.system("mimic3 --voice 'en_US/hifi-tts_low' --interactive '"+command+"' | aplay") 
  #  print("Say:  "+command)
    log(command)

def isPhrase(phrase):
  phrases = ["I'm ready.", "What do you need?", "What's the title?", "What do you want to write?", "Accepted. Do you want to password-protect it?", "No password saved.", "What do you want your password to be?", "Answer not recognized, password not set.", "Starting file.", "Quitting. Goodbye.", "Do you want to write a body paragraph?", "Note written"] 
  if phrase in phrases:
    return True
  return False

def phrase(phrase):
  f = open("backpack/pi/data/phrases-needed.txt", "a")
  f.write(phrase)
  f.close()
  print(phrase)
  """
  phrases = ["I'm ready.", "What do you need?", "What's the title?", "What do you want to write?", "Accepted. Do you want to password-protect it?", "No password saved.", "What do you want your password to be?", "Answer not recognized, password not set.", "Starting file.", "Quitting. Goodbye.", "Do you want to write a body paragraph?", "Note written"] 
  fileNames = ["ImReady.mp3", "WhatDoYouNeed.mp3", "WhatsTheTitle.mp3", "WhatDoYouWantToWrite.mp3", "AcceptedDoYouWantToPasswordProtectIt.mp3", "NoPasswordSaved.mp3", "WhatDoYouWantYourPasswordToBe.mp3", "AnswerNotRecognizedPasswordNotSet.mp3", "StartingFile.mp3", "QuittingGoodbye.mp3"]

  index = phrases.index(phrase)
  print("Playing Sound: "+phrases[index])
  #os.system("mpg123 "+fileNames[index]) - RASP
  """

def sound(sound):
  if (sound=="interpretting"):
    print("interpretting")
  elif sound=="volume":
    print("Volume test")
def getVoice():
  """
  with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout=2)
  sound("interpretting")
  voice = r.recognize_whisper(audio, language="english")
  print(voice)
  return(voice)
  """
  return(input("Voice: "))

def encrypt(plaintext, key):
  encrypted = aes256.encrypt(plaintext, key)
  return(encrypted)
def decrypt(ciphertext, key):
  return(aes256.decrypt(ciphertext, key))

def startAssistant():
  log("starting assistant")
  phrase("What do you need?")
  request = getVoice()

def spell():
  phrase("What do you want to spell?")
  word = getVoice()
  for i in word:
    speak(i)
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current
def stopwatch():
  #phrase("3, 2, 1, go")
  while True:
    try:
        start_time=time.time()
        while True:
            #phrase(round(time.time()-start_time,0),'secs',end='\n')
            time.sleep(1)
    except KeyboardInterrupt:
            print("Timer has stopped")
            end_time=time.time()
            speak("The time elapsed is "+str(round(end_time-start_time,2))+' seconds')
            break

def takeNote():
  current_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
  phrase("What's the title?")
  title = getVoice()
  log("Took note - "+title)

  phrase("Do you want to write a body paragraph?")
  contentBool = getButton("bool")
  #Listen for button. Top button is yes, second button is no
  if (contentBool==True):
    phrase("What do you want to write?")
    content = getVoice()
    phrase("Accepted. Do you want to password-protect it?")
    passwordBool = getButton("bool")
    if passwordBool == False:
      phrase("No password saved.")
      f = open("backpack/pi/data/notes/"+title+" - "+str(current_time)+".txt", "w")
      print("saved to", "backpack/pi/data/notes/"+title+" - "+str(current_time)+".txt")
      f.write(content)
      f.close()
      phrase("Note written")
    elif passwordBool == True:
      phrase("What do you want your password to be?")
      password = getVoice()
      content = encrypt(content, password)
      f = open("backpack/pi/data/notes/"+title+" - "+str(current_time)+".txt", "w")
      f.write(str(content))
      f.close()
      phrase("Note written")
  else:
    f = open("backpack/pi/data/notes/"+title+" - "+str(current_time)+".txt", "w")
    f.close()
    phrase("Note written")
def record():
  speak("Starting twenty minute recording.")
  #sudo apt-get install sound-recorder
  os.system("sound-recorder -c 2 -b 16 -P -S 20:00 recording.wav")

def shuffleMusic():
  #phrase("Shuffling music")
  music_list = os.listdir("Music/")
  random.shuffle(music_list)
  for i in music_list:
    print(i)
    addLet = (random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+"-")
    os.system("mv "+i+" "+addLet+i)
def playMusic():
  log("Started music")
  #phrase("Playing music")
  shuffleMusic()
  os.system("rhythmbox-client")
def pauseMusic():
  speak("pause music")
def stopMusic():
  speak("stop playing music")
def skipMusic():
  speak("skip this song music")
def backwordsMusic():
  speak("go back music")
def connectBluetooth():
  log("Connected to bluetooth")
  os.system("./connect_bluetooth")
  phrase("Welcome")
def getDate():
  log("Got date")
  today = datetime.datetime.now()
  days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eithteenth", "ninteenth", "twentieth", "twenty first", "twenty second", "twenty third", "twenty fourth", "twenty fifth", "twenty sixth", "twenty seventh", "twenty eigth", "twenty ninth", "thirtieth", "thirty first", "thirty second"]
  months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  day = days[today.day-1]
  month = months[today.month-1]
  year = today.year
  weekday = (today.strftime("%A"))
  speak("It is "+weekday+", "+month+" "+day)
def getTime():
  log("Got time")
  now = datetime.datetime.now()
  speak(now.strftime("Its "+'%H:%M'))
def repeatStatement():
  speak(old_command)
def firstAid():
  log("Started first aid")
  speak("First aid assistant, asks if you know the cause, if you don't it asks for symptoms. Helps you through the treating process with Red Cross or another organization's data")
def readEbook():
  log("Started reading book")
  speak("Have a library of ebooks for reading offline")
def CPRBeat():#Need a way to use button to stop met
  while True:
    pygame.mixer.music.play()
    time.sleep(0.6)
def firstAid():
  start(False)
def volume():
  #Todo: Start with the existing volume
  phrase("Adjusting volume")
  volume = 50

  while True: #Neet button input - Button1 = volume up, Button2 = volume down, Button 3 stops volume adjusting 
    p = input("Up/Down")
    com = "amixer sset 'Master' 50%"
    Hcom = "amixer sset -M 'Master' 50%"
    if p=="up":
      volume+=5
    elif p=="down":
      volume-=5
    else: 
      sound(volume)
      break
    os.system("amixer sset -M 'Master' "+str(volume)+"%")
    os.system("amixer sset 'Master' "+str(volume)+"%")
    sound("volume")

def timer(txt): #Want to make it run in the background
  x = txt.split()
  try:
      mindex = x.index("minutes")
      minutes=x[mindex-1]
      minutes = (text2int(minutes))
  except:
      minutes=0
  try:
      sindex = x.index("seconds")
      seconds=x[sindex-1]
      if sindex==-1:
          sindex=x.index("second")
          seconds=x[sindex-1]
          if sindex==-1:
              seconds=0
      seconds = (text2int(seconds))
  except:
      seconds=0
  tim=minutes*60+seconds
  log("Setting timer for "+str(tim)+" seconds")
  time.sleep(tim)
def metronome(bpm):#Add way for button to stop it, also use buttons to increase/decrease bpm
  while True:
    pygame.mixer.music.play()
    time.sleep(60/bpm)
def diary():
  current_time = datetime.datetime.now(pytz.timezone('America/Chicago'))

  f = open("backpack/pi/data/diary.txt", "a")
  f.write(str(current_time)+" : "+getVoice()+"\n")
  f.close()

def audiobook(): #AudioBook directories (titles) have to be formated by hand to be a readable sentence
  book="bill nye and boomerang"
  books = os.listdir("back/pi/date/audiooks")
  if book in books:
    phrase("Book found.")

  chapters = os.listdir("Music/")





def quit():
  log("Quit")
  speak("Quitting")
  quit()
def button_callback1(channel):
    startAssistant()
def button_callback2(channel):
    getTime()
def button_callback3(channel):
    takeNote()
def button_callback4(channel):
    os.system("./connect_bluetooth.sh")

"""
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10>
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback1)

GPIO.cleanup() # Clean up
"""

print("Pocket Assistant Ready!!")

while True:
  todo=input("Enter Command ")

  if todo=="exit":
    exit()
  elif todo=="sa": #start assistant
    startAssistant()
  elif todo=="tn": #take note
    takeNote()
  elif todo=="d": #record
    getDate()
  elif todo=="r": #record
    record()
  elif todo=="m":
    playMusic()
  elif todo=="t":
    getTime()
  elif todo=="re":
    repeatStatement()
  elif todo=="cb": # connect bluetooth
    connectBluetooth()
  elif todo=="s":
    stopwatch()
  elif todo=="cpr":
    CPRBeat()
  elif todo=="v":
    volume()
  elif todo=="t":
    timer()
  
  


