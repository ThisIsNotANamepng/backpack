import os
import unidecode
import string
alphabet = list(string.ascii_lowercase)
for a in alphabet:
    for b in alphabet:
        for c in alphabet:
            for d in alphabet:
                file=a+b+c+d
                open("wikipedia2/"+file+".txt", "w")
                print("Opened", file+".txt")

print("Beginning search")
f=open("wikipedia/wikipedia.xml", "r")

lines=f.readlines()
print(len(lines))
f.close()

for i in lines:
    topic = unidecode.unidecode(i[0:i.index("<")])
    os.system('echo "'+i+'" >> wikipedia2/'+topic[0:4].lower()+'.txt')
print("Finished")