import os
import random

os.system("nmcli radio wifi off")
sub = "backup" #Either backup or data

#Zip data dir
os.system("tar -czf "+sub+".tar.gz "+sub)

#Encrypt zip
os.system("gpg --encrypt --armor -r TurtleDinasour@protonmail.com "+sub+".tar.gz")

#Overwrite and Delete data dir
notesList = os.listdir("/home/pi/"+sub)
for i in notesList:
  limit = 255
  random_string = ''
  for _ in range(50000):
    random_integer = random.randint(0, limit)
    random_string += (chr(random_integer))


  n = open("home/pi/"+sub+"/"+i, "w")
  n.write(random_string)
  n.close()

notesList = os.listdir("/home/pi/"+sub+"/notes")
for i in notesList:
  limit = 255
  random_string = ''
  for _ in range(50000):
    random_integer = random.randint(0, limit)
    random_string += (chr(random_integer))


  n = open(sub+"/notes/"+i, "w")
  n.write(random_string)
  n.close()

limit = 255
random_string = ''
for _ in range(50000):
  random_integer = random.randint(0, limit)
  random_string += (chr(random_integer))
n = open(sub+"/assistant.log", "w")
n.write(random_string)
n.close()

os.system("rm -r "+sub)

#Delete zip
limit = 255
random_string = ''
for _ in range(10000000):
  random_integer = random.randint(0, limit)
  random_string += (chr(random_integer))
n = open(sub+".tar.gz", "w")
n.write(random_string)
n.close()
os.system("rm "+sub+".tar.gz")
