print("xml-parser")
import os


os.system("touch new.xml")

s = open("enwiki-20230420-abstract.xml", "r")
a = open("new.xml", "a")

print("Starting First Loop")
for i in s.readlines():
    if "<url>" not in i and "<sublink" not in i and "<links" not in i and "</links>" not in i and "<doc>" not in i and "</doc>" not in i and "<title>" in i:
        a.write(i[18:-9])
    if "<url>" not in i and "<sublink" not in i and "<links" not in i and "</links>" not in i and "<doc>" not in i and "</doc>" not in i and "<abstract" in i:
        a.write(i)
print("First Loop Finished")

os.system("touch wikipedia.xml")

a.close()
s.close()

s = open("new.xml", "r")
a = open("wikipedia.xml", "a")

print("Starting Second Loop")

for i in s.readlines():
    if "|" not in i and "#" not in i and "may refer to:" not in i:
        toWrite=""
        for k in i:
            if k!= "}" and k!= "{":
                toWrite+=k
        a.write(toWrite)
print("Second Loop Finished")


a.close()
s.close()

os.system("rm new.xml")
print("Finished")