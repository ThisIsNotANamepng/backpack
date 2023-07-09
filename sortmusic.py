import os
import random
import string 

musicDirectory = os.listdir("/home/pi/Music")
music_dir="/home/pi/Music"


for i in musicDirectory:
  addLet = (random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+random.choice(string.ascii_letters)+"-")
  os.system("mv '"+music_dir+"/"+i+"' '"+music_dir+"/"+addLet+i+"'")
