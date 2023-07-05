print("Pocket Assistant Starting....")
#Imports
import datetime
import speech_recognition as sr
#from TTS.api import TTS
from pydub import AudioSegment
from pydub.playback import play
import RPi.GPIO as GPIO
from gpiozero import Button
import os
import pytz
from base64 import b64encode, b64decode
import hashlib
from AesEverywhere import aes256
import json
import pathlib
import random
#from pydub import AudioSegment
import random
import string
import time
#import pyaudio
import calendar
from playsound import playsound
import pygame
import firstaid
import textdistance
import sqlite3
import hashlib
from nltk.corpus import wordnet
import nltk
import time


global selected
selected = 0

global picked
picked = 0

print("Imports complete")

DB_PATH = "todos.db"
conn = sqlite3.connect(DB_PATH)

global todoCursor
global notesCursor
todoCursor, notesCursor=0, 0
#r = sr.Recognizer()

#mic = sr.Microphone()

pygame.init()


def hashString(string):
    return (hashlib.sha256(string.encode()).hexdigest())

def speak(command):
  command=command.lower()
  print("saying:", command)
  global old_command
  old_command = command
  
  
  filename = command.replace(" ", "")+".wav"


  if filename in os.listdir("BackpackPhrases/"):
    os.system("aplay BackpackPhrases/"+filename)
  else:
    os.system("aplay beep.wav")
    print("mimic3 --voice 'en_US/hifi-tts_low' '"+command+"' > BackpackPhrases/"+filename) 
    os.system("mimic3 --voice 'en_US/hifi-tts_low' '"+command+"' > BackpackPhrases/"+filename) 
    os.system("aplay BackpackPhrases/"+filename)
    print("Say:  "+command)
  
  

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

def getVoice(starter):
  """
  with mic as source:
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source, timeout=2)
  sound("interpretting")
  voice = r.recognize_whisper(audio, language="english")
  print(voice)
  return(voice)
  """
  print(starter)
  return(input("Voice: "))

def error():
  print("There's been an error in the program. This is probably a programming issue, not anything you can fix while in use.")
  speak("There's been an error in the program. This is probably a programming issue, not anything you can fix while in use.")

def encrypt(plaintext, key):
  return(aes256.encrypt(plaintext, key))
def decrypt(ciphertext, key):
  return(aes256.decrypt(ciphertext, key))

def startAssistant(t="t"):
  speak("What do you need?")
  request = getVoice()

def spell(t="t"):
  speak("What do you want to spell?")
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

def stopwatch(t="t"):
  speak("Starting stopwatch")
  sound("321beeps")
  while True:
    try:
        start_time=time.time()
        while True:
            #speak(round(time.time()-start_time,0),'secs',end='\n')
            time.sleep(1)
    except KeyboardInterrupt:
            print("Timer has stopped")
            end_time=time.time()
            speak("The time elapsed is "+str(round(end_time-start_time,2))+' seconds')
            break

def takeNote(t="t"):
  current_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
  speak("What's the title?")
  title = getVoice()

  speak("Do you want to write a body paragraph?")
  contentBool = getButton("bool")
  #Listen for button. Top button is yes, second button is no
  if (contentBool==True):
    speak("What do you want to write?")
    content = getVoice()
    speak("Accepted. Do you want to password-protect it?")
    passwordBool = getButton("bool")
    if passwordBool == False:
      speak("No password saved.")
      f = open("backpack/pi/data/notes/"+title+" - "+str(current_time)+".txt", "w")
      print("saved to", "backpack/pi/data/notes/"+title+" - "+str(current_time)+".txt")
      f.write(content)
      f.close()
      speak("Note written")
    elif passwordBool == True:
      speak("What do you want your password to be?")
      password = getVoice()
      content = encrypt(content, password)
      f = open("backpack/pi/data/notes/"+title+" - "+str(current_time)+".txt", "w")
      f.write(str(content))
      f.close()
      speak("Note written")
  else:
    f = open("backpack/pi/data/notes/"+title+" - "+str(current_time)+".txt", "w")
    f.close()
    speak("Note written")

def record(t="t"):
  speak("Starting twenty minute recording.")
  #sudo apt-get install sound-recorder
  os.system("sound-recorder -c 2 -b 16 -P -S 20:00 recording.wav")

def shuffleMusic(t="t"):
  #phrase("Shuffling music")
  music_dir="/home/jack/Music/test/"
  music_list = os.listdir(music_dir)
  for i in music_list:
    os.system("mv "+music_dir+i+" "+music_dir+i[-(len(i)-4):])
  music_list = os.listdir(music_dir)
  for i in music_list:
    addLet = (random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+"-")
    os.system("mv "+music_dir+i+" "+music_dir+addLet+i)

def playMusic(t="t"):
  speak("Playing music")
  shuffleMusic()

  music_dir="/home/jack/Music/test/"
  music_list = os.listdir(music_dir)

  i=0

  while i<len(music_list):#Set buttons to do functons
    pygame.mixer.music.load(music_dir+music_list[i])
    pygame.mixer.music.play()
    #pygame.mixer.music.pause()
    i+=1

def pauseMusic(t="t"):
  speak("pause music")

def stopMusic(t="t"):
  speak("stop playing music")

def skipMusic(t="t"):
  speak("skip this song music")

def backwordsMusic(t="t"):
  speak("go back music")

def connectBluetooth(t="t"):
  os.system("./connect_bluetooth")
  f=open("bluetoothConnectionSuccess.txt", "r")
  if "success" in f.read():
    speak("Connected successfully. Welcome")
  else:
    print("Failed to connect")
    speak("Failed to connect")
  f.close()

def getDate(t="t"):
  today = datetime.datetime.now()
  days = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth", "ninth", "tenth", "eleventh", "twelfth", "thirteenth", "fourteenth", "fifteenth", "sixteenth", "seventeenth", "eithteenth", "ninteenth", "twentieth", "twenty first", "twenty second", "twenty third", "twenty fourth", "twenty fifth", "twenty sixth", "twenty seventh", "twenty eigth", "twenty ninth", "thirtieth", "thirty first", "thirty second"]
  months = ["January", "Febuary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
  day = days[today.day-1]
  month = months[today.month-1]
  year = today.year
  weekday = (today.strftime("%A"))
  speak("It is "+weekday+", "+month+" "+day)

def getTime(t="t"):
  now = datetime.datetime.now()
  speak(now.strftime("Its "+'%H:%M'))

def repeatStatement():
  speak(old_command)

def readEbook(t="t"):
  log("Started reading book")
  speak("Have a library of ebooks for reading offline")

def CPRBeat():#Need a way to use button to stop met
  while True:
    pygame.mixer.music.play()
    time.sleep(0.6)

def firstAid(t="t"):
  firstaid.start(False)
  
def volumeUp(t="t"):
  os.system("amixer -D pulse sset Master 5%+")
  os.system("aplay volume.wav")

def volumeDown(t="t"):
  os.system("amixer -D pulse sset Master 5%-")
  os.system("aplay volume.wav")

def volume(t="t"):
  #Todo: Start with the existing volume
  speak("Adjusting volume")
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
  pygame.mixer.music.load("beep.mp3")

  while True:#Need buttonInterrupt, stop the loop and start is again
    pygame.mixer.music.play()
    time.sleep(60/bpm)
    
def say(thing):
  speak(thing)

def audiobook(): #AudioBook directories (titles) have to be formated by hand to be a readable sentence
  book="bill nye and boomerang" #Need a button interupt
  f=open("audiobok.txt", "r")
  database = f.readlines()
  f.close()
  for i in database:
    if i==book:
      chapter = database[i+1]
      break
  chapters = os.listdir("audiooks/"+book)
  while chapter<len(chapters-1):
    os.system("mpg123 "+chapters[chapter])


  #This is if button interrupt above
  speak("What chapter?")
  chap = int(getVoice())
  books = os.listdir("back/pi/date/audiooks")
  if book in books:
    speak("Book found.")

def quit(t="t"):
  speak("Quitting")
  quit()

def define():
  say("What word do you want to define?")
  word=getVoice()

  syns = wordnet.synsets(word)
  try:
    print(syns[0].definition())
  except IndexError:
    say("There is no definition for that word")
  except:
    error()

def searchWikipedia(toSearch, t="t"):
  toReturn="No article found"
  distance=0

  speak("Searching Wikipedia")
  toSearch=toSearch.lower()

  firstFour=toSearch[0:4]

  f=open("wikipedia2/"+firstFour+".txt", "r")
  lines=f.readlines()
  print(len(lines))
  for i in lines:
    if i!="\n":
      topic = i[0:i.index("<")]
      if(textdistance.levenshtein.normalized_similarity(topic, toSearch))>distance:
        distance=textdistance.levenshtein.normalized_similarity(topic, toSearch)
        toReturn=i
  print(toReturn)


  f.close()

def navigate(t="t"):
  say("Navigate using osmmaps and the gps")

def empty(t="t"):
  pass

def stopStopwatch(t="t"):
  say("Stop the stopwatch")

def startStopwatch(t="t"):
  say("Start stopwatch")

def getStopwatchTime(t="t"):
  say("Get the stopwatch time")

def pauseResumeStopwatch(t="t"):
  say("Toggle puase of stopwatch")

def remoteUp(t="t"):
  say("Up on remote")

def remoteRight(t="t"):
  say("Right on remote")

def remoteDown(t="t"):
  say("Down on remote")

def remoteLeft(t="t"):
  say("Left on remote")

def remoteClick(t="t"):
  say("Press circle on the remote")

def remotePausePlay(t="t"):
  say("Toggle puase or play on the remote")

def remoteBack(t="t"):
  say("Back button on the remote")


def generate_todo_id(title, t="t"):
  hash_str = str(time.time()) + title
  hash_obj = hashlib.sha256(hash_str.encode())
  return hash_obj.hexdigest()[:10]

def create_todo(title, description=None, t="t"):
  todo_id = generate_todo_id(title)
  cursor = conn.cursor()
  cursor.execute("INSERT INTO todos (todo_id, title, description) VALUES (?, ?, ?)", (todo_id, title, description))
  conn.commit()
  return("Success")

def delete_todo(t="t"):
  global selected
  print(selected)
  if selected==None: selected=0
  try:
    delete_id=read_todos()[selected][0]
  except IndexError:
    speak("Todo list is already empty")
    return
  cursor = conn.cursor()
  cursor.execute("DELETE FROM todos WHERE todo_id=?", (delete_id,))
  conn.commit()
  if selected!=0: selected-=1
  return("Success")

def read_todos(t="t"):
  cursor = conn.cursor()
  cursor.execute("SELECT * FROM todos;")
  rows = cursor.fetchall()
  return rows

def increase_selected(t="t"):
  global selected
  print("Length of todo lsit", len(read_todos()))
  if selected==len(read_todos())-1:
    speak("Cursor already at max")
    return
  if selected==None:
    selected=0
    return
  print("Increasing selected", selected)
  selected+=1
  speak(read_selected_todo())

def decrease_selected(t="t"):
  global selected
  if selected==0:
    speak("Cursor already at minimum")
    return
  if selected==None:
    selected=0
  selected-=1
  speak(read_selected_todo())

def get_selected_todo(t="t"):
    global selected
    if selected is None:
      selected=0
      return read_todos()[0]#Return the first item in the table
    else:
      return read_todos()[selected]#Return the nth item in the table
    
def get_selected_todo_id(t="t"):
  global selected
  if selected is None:
    selected=0
    return read_todos()[0][0]#Return the first item in the table
  else:
    return read_todos()[selected][0]#Return the nth item in the table

def read_selected_todo(t="t"):
  speak(get_selected_todo()[1])

def create_todo_face(t="t"):
  title=getVoice("What's the title?")
  yn = getVoice("Do you want a description?")
  if "yes" in yn:
    body=getVoice("What's the description?")
    create_todo(title, body)
  else:
    create_todo(title)
  
def read_all_todos(t="t"):
  for i in read_todos:
    speak(i[1])

def edit_selected(t="t"):
  speak("Replacing selected todo description")
  new = getVoice("What do you want the new description to be?")
  cursor = conn.cursor()
  cursor.execute("UPDATE todos SET description = ? WHERE todo_id = ?;", (new, get_selected_todo_id()))
  conn.commit()
  return("Success")


def generate_note_id(title, t="t"):
    hash_str = str(time.time()) + title
    hash_obj = hashlib.sha256(hash_str.encode())
    return hash_obj.hexdigest()[:10]

def create_note(title, description=None, t="t"):
    note_id = generate_note_id(title)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO notes (note_id, title, description) VALUES (?, ?, ?)", (note_id, title, description))
    conn.commit()
    return("Success")

def delete_note(t="t"):
    global picked
    if picked==None: picked=0
    try:
      delete_id=read_notes()[picked][0]
    except IndexError:
      speak("Notes list is already empty")
      return
    cursor = conn.cursor()
    cursor.execute("DELETE FROM notes WHERE note_id=?", (delete_id,))
    conn.commit()
    if picked!=0: picked-=1
    return("Success")

def read_notes(t="t"):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notes;")
    rows = cursor.fetchall()
    return rows

def increase_picked(t="t"):
    global picked
    if picked==len(read_notes())-1:
      speak("Cursor already at max")
      return
    if picked==None:
      picked=0
      return
    picked+=1
    speak(read_picked_note())

def decrease_picked(t="t"):
    global picked
    if picked==0:
      speak("Cursor already at minimum")
      return
    if picked==None:
      picked=0
    picked-=1
    speak(read_picked_note())

def get_picked_note(t="t"):
    global picked
    if picked is None:
        picked=0
        return read_notes()[0]#Return the first item in the table
    else:
        return read_notes()[picked]#Return the nth item in the table
    
def get_picked_note_id(t="t"):
  global picked
  if picked is None:
    picked=0
    return read_notes()[0][0]#Return the first item in the table
  else:
    return read_notes()[picked][0]#Return the nth item in the table

def read_picked_note(t="t"):
  speak(get_picked_note()[1])

def create_note_face(t="t"):
  title=getVoice("What's the title?")
  yn = getVoice("Do you want a description?")
  if "yes" in yn:
    body=getVoice("What's the description?")
    create_note(title, body)
  else:
    create_note(title)
  
def read_all_notes(t="t"):
  for i in read_notes:
    speak(i[1])

def edit_picked(t="t"):
  speak("Replacing picked note description")
  new = getVoice("What do you want the new description to be?")
  cursor = conn.cursor()
  cursor.execute("UPDATE notes SET description = ? WHERE note_id = ?;", (new, get_picked_note_id()))
  conn.commit()
  return("Success")


def startMainMenu(t="t"):
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(13)
  GPIO.remove_event_detect(15)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(19)



  GPIO.add_event_detect(10,GPIO.RISING,callback=shuffleMusic, bouncetime=200)
  GPIO.add_event_detect(11,GPIO.RISING,callback=read_all_todos, bouncetime=200)
  GPIO.add_event_detect(12,GPIO.RISING,callback=firstAid, bouncetime=200)
  GPIO.add_event_detect(13,GPIO.RISING,callback=getTime, bouncetime=200)
  GPIO.add_event_detect(15,GPIO.RISING,callback=volumeUp, bouncetime=200)
  GPIO.add_event_detect(16,GPIO.RISING,callback=volumeDown, bouncetime=200)
  GPIO.add_event_detect(18,GPIO.RISING,callback=startAssistant, bouncetime=200)
  GPIO.add_event_detect(19,GPIO.RISING,callback=connectBluetooth, bouncetime=200)

def startNotesMenu(t="t"):

  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(22)
  GPIO.remove_event_detect(24)
  GPIO.remove_event_detect(26)

  GPIO.add_event_detect(11,GPIO.RISING,callback=increase_picked, bouncetime=200)
  GPIO.add_event_detect(10,GPIO.RISING,callback=decrease_picked, bouncetime=200)
  GPIO.add_event_detect(12,GPIO.RISING,callback=startTodoMenu, bouncetime=200)
  GPIO.add_event_detect(16,GPIO.RISING,callback=startMainMenu, bouncetime=200)
  GPIO.add_event_detect(18,GPIO.RISING,callback=read_all_notes, bouncetime=200)
  GPIO.add_event_detect(22,GPIO.RISING,callback=delete_note, bouncetime=200)
  GPIO.add_event_detect(24,GPIO.RISING,callback=edit_picked, bouncetime=200)
  GPIO.add_event_detect(26,GPIO.RISING,callback=create_note_face, bouncetime=200)

def startTodoMenu(t="t"):
  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(22)
  GPIO.remove_event_detect(24)
  GPIO.remove_event_detect(26)

  GPIO.add_event_detect(11,GPIO.RISING,callback=increase_selected, bouncetime=200)
  GPIO.add_event_detect(10,GPIO.RISING,callback=decrease_selected, bouncetime=200)
  GPIO.add_event_detect(12,GPIO.RISING,callback=startNotesMenu, bouncetime=200)
  GPIO.add_event_detect(16,GPIO.RISING,callback=startMainMenu, bouncetime=200)
  GPIO.add_event_detect(18,GPIO.RISING,callback=read_all_todos, bouncetime=200)
  GPIO.add_event_detect(22,GPIO.RISING,callback=delete_todo, bouncetime=200)
  GPIO.add_event_detect(24,GPIO.RISING,callback=edit_selected, bouncetime=200)
  GPIO.add_event_detect(26,GPIO.RISING,callback=create_todo_face, bouncetime=200)

def startMusicMenu(t="t"):
  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(22)
  GPIO.remove_event_detect(24)
  GPIO.remove_event_detect(26)



  GPIO.add_event_detect(11,GPIO.RISING,callback=shuffleMusic, bouncetime=200)
  GPIO.add_event_detect(10,GPIO.RISING,callback=firstAid, bouncetime=200)
  GPIO.add_event_detect(12,GPIO.RISING,callback=playMusic, bouncetime=200)
  GPIO.add_event_detect(16,GPIO.RISING,callback=test)
  GPIO.add_event_detect(18,GPIO.RISING,callback=test)
  GPIO.add_event_detect(22,GPIO.RISING,callback=test)
  GPIO.add_event_detect(24,GPIO.RISING,callback=test)
  GPIO.add_event_detect(26,GPIO.RISING,callback=test)

def startAssistantMenu(t="t"):
  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(22)
  GPIO.remove_event_detect(24)
  GPIO.remove_event_detect(26)

  GPIO.add_event_detect(11,GPIO.RISING,callback=volumeUp, bouncetime=200)
  GPIO.add_event_detect(10,GPIO.RISING,callback=volumeDown, bouncetime=200)
  GPIO.add_event_detect(12,GPIO.RISING,callback=navigate, bouncetime=200)
  GPIO.add_event_detect(16,GPIO.RISING,callback=startMainMenu, bouncetime=200)
  GPIO.add_event_detect(18,GPIO.RISING,callback=startAssistant, bouncetime=200)
  GPIO.add_event_detect(22,GPIO.RISING,callback=stopwatch, bouncetime=200)
  GPIO.add_event_detect(24,GPIO.RISING,callback=metronome, bouncetime=200)
  GPIO.add_event_detect(26,GPIO.RISING,callback=audiobook, bouncetime=200)

def startStopwatchMenu(t="t"):
  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(22)
  GPIO.remove_event_detect(24)
  GPIO.remove_event_detect(26)

  GPIO.add_event_detect(11,GPIO.RISING,callback=stopStopwatch, bouncetime=200)
  GPIO.add_event_detect(10,GPIO.RISING,callback=startStopwatch, bouncetime=200)
  GPIO.add_event_detect(12,GPIO.RISING,callback=getStopwatchTime, bouncetime=200)
  GPIO.add_event_detect(16,GPIO.RISING,callback=pauseResumeStopwatch, bouncetime=200)
  GPIO.add_event_detect(18,GPIO.RISING,callback=volumeUp, bouncetime=200)
  GPIO.add_event_detect(22,GPIO.RISING,callback=volumeDown, bouncetime=200)
  GPIO.add_event_detect(24,GPIO.RISING,callback=test, bouncetime=200)
  GPIO.add_event_detect(26,GPIO.RISING,callback=startMainMenu, bouncetime=200)

def startMetronomeMenu(t="t"):
  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(22)
  GPIO.remove_event_detect(24)
  GPIO.remove_event_detect(26)

  GPIO.add_event_detect(11,GPIO.RISING,callback=shuffleMusic, bouncetime=200)
  GPIO.add_event_detect(10,GPIO.RISING,callback=firstAid, bouncetime=200)
  GPIO.add_event_detect(12,GPIO.RISING,callback=playMusic, bouncetime=200)
  GPIO.add_event_detect(16,GPIO.RISING,callback=test, bouncetime=200)
  GPIO.add_event_detect(18,GPIO.RISING,callback=test, bouncetime=200)
  GPIO.add_event_detect(22,GPIO.RISING,callback=test, bouncetime=200)
  GPIO.add_event_detect(24,GPIO.RISING,callback=test, bouncetime=200)
  GPIO.add_event_detect(26,GPIO.RISING,callback=test, bouncetime=200)

def startAudiobookMenu(t="t"):
  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(22)
  GPIO.remove_event_detect(24)
  GPIO.remove_event_detect(26)



  GPIO.add_event_detect(11,GPIO.RISING,callback=shuffleMusic)
  GPIO.add_event_detect(10,GPIO.RISING,callback=firstAid)
  GPIO.add_event_detect(12,GPIO.RISING,callback=playMusic)
  GPIO.add_event_detect(16,GPIO.RISING,callback=stop)
  GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback5)
  GPIO.add_event_detect(22,GPIO.RISING,callback=button_callback6)
  GPIO.add_event_detect(24,GPIO.RISING,callback=button_callback7)
  GPIO.add_event_detect(26,GPIO.RISING,callback=button_callback8)

def startMapMenu(t="t"):
  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(22)
  GPIO.remove_event_detect(24)
  GPIO.remove_event_detect(26)



  GPIO.add_event_detect(11,GPIO.RISING,callback=shuffleMusic)
  GPIO.add_event_detect(10,GPIO.RISING,callback=firstAid)
  GPIO.add_event_detect(12,GPIO.RISING,callback=playMusic)
  GPIO.add_event_detect(16,GPIO.RISING,callback=stop)
  GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback5)
  GPIO.add_event_detect(22,GPIO.RISING,callback=button_callback6)
  GPIO.add_event_detect(24,GPIO.RISING,callback=button_callback7)
  GPIO.add_event_detect(26,GPIO.RISING,callback=button_callback8)

def startRemoteMenu(t="t"):
  GPIO.remove_event_detect(11)
  GPIO.remove_event_detect(10)
  GPIO.remove_event_detect(12)
  GPIO.remove_event_detect(16)
  GPIO.remove_event_detect(18)
  GPIO.remove_event_detect(22)
  GPIO.remove_event_detect(24)
  GPIO.remove_event_detect(26)



  GPIO.add_event_detect(11,GPIO.RISING,callback=remoteUp)
  GPIO.add_event_detect(10,GPIO.RISING,callback=remoteRight)
  GPIO.add_event_detect(12,GPIO.RISING,callback=remoteDown)
  GPIO.add_event_detect(16,GPIO.RISING,callback=remoteLeft)
  GPIO.add_event_detect(18,GPIO.RISING,callback=remoteClick)
  GPIO.add_event_detect(22,GPIO.RISING,callback=remotePausePlay)
  GPIO.add_event_detect(24,GPIO.RISING,callback=remoteBack)
  GPIO.add_event_detect(26,GPIO.RISING,callback=startMainMenu)


"""
t=0
f=0
while True:

  searchWikipedia(input("Search term:   "))
  tf=input("Correct?  ")
  if(tf=="y"):
    t+=1
  else:
    f+=1
  print(t, "correct, ", f, "not correct")
"""

def test(t):
  print("Thing done")

def translate(inLan, toLan, sentence):
  print("translate")


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(10,GPIO.RISING,callback=test, bouncetime=200) # Setup event on pin 10 rising edge

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(11,GPIO.RISING,callback=test, bouncetime=200)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(12,GPIO.RISING,callback=test, bouncetime=200)

GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(13,GPIO.RISING,callback=test, bouncetime=200)

GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
GPIO.add_event_detect(15,GPIO.RISING,callback=test, bouncetime=200) 

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(16,GPIO.RISING,callback=test, bouncetime=200)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(18,GPIO.RISING,callback=test, bouncetime=200)

GPIO.setup(19, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(19,GPIO.RISING,callback=test, bouncetime=200)



speak("Welcome. System ready.")
startMainMenu()
while(True): 
  command=input(">  ").split()
  if command!="":
    if command[0]=="log":
      print("Log")
    elif command[0]=="stop":
      print("Stop ASB")
    elif command[0]=="shutdown":
      print("Shutdown computer")
    elif command[0]=="sound":
      speak("Sound test")


#Each button calls its own function. When a new menu is called, a global function or class variable changes what happens in the button's function