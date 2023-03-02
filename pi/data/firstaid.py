def speak(text):
    print(text)
def getVoice():
    input("Input voice: ")

def heartAttack():
    say("Heart attack")
def stroke():
    say("Stroke")
def cut():
    say("Bleeding")
def burn():
    say("Burn")
def allergicReaction():
    say ("Allergic reaction")
def choking():
    say("Choking")
def dislocate():
    say("Dislocate")
def shock():
    say("Shock")
def faint():
    say("Faint")
def brokenBone():
    say("Broekn bone")
def heat():
    say("Heatstroke")
def hypothermia():
    say("Hypothermia")
def bite():
    say("Animal bite or sting")
def poison():
    say("poison")
def sprain():
    say("sprain or twisted ankle or wrist")


def diagnose():
    speak("Diagnose")

def causeKnown():
    speak("What is the cause?")
    cause = getVoice()

    if "heart attack" in cause:
        heartAttack()
    elif "stroke" in cause and "heat" not in cause:
        stroke()
    elif "cut" in cause or "stab" in cause or "scrape" in cause:
        cut()
    elif "burns" in cause or "burn" in cause:
        burn()
    elif "allergic" in cause or "reaction" in cuase:
        allergicReaction()
    elif "choking" in cause:
        choking()
    elif "dislocate" in cause or "dislocation" in cause or "dislocated" in cause:
        dislocated()
    elif "shock" in cause or "electric" in cause or "electrocution" in cause or "electrocuted" in cause or "shocked" in cause:
        electrocuted()
    elif "faint" in cause or "fainted" in cause:
        fainted()
    elif "broken" in cause or "broke" in cause:
        brokenBone()
    elif "heat" in cause or "heatstroke" in cause:
        heatStroke()
    elif "hypothermia" in cause:
        hypothermia()
    elif "bite" in cause or "sting" in cause or "stung" in cause or "bit" in cause:
        sting()
    elif "poison" in cause or "toxic" in cause or "chemical" in cause or "chemicals" in cause:
        poison()
    elif "sprain" in cause or "sprained" in cause or "twisted" in cause or "twist" in cause:
        sprain()

def start(again):
    if again==True:
        speak("I didn't understand, what did you say?")
    elif again==False:
        speak("Ensure the scene is safe and call nine one one")
    speak("Do you know what the problem is?")
    boo = getVoice()

    if "yes" in boo:
        causeKnown()
    elif "no" in boo:
        diagnose()
    else:
        start(True)



#start(False)















"""
Add option for button to say yes or no
"""