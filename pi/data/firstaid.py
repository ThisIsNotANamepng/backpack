def speak(text):
    print(text)
def phrase(test):
    print(text)
def getVoice():
    input("Input voice: ")

def noo():
    speak("Call nine one one.")
def shock():
    speak("If you notice signs of shock,")
    speak("Lay the victim down and elevate the legs slightly.")
    speak("Keep the victim still and don't move them.")
    speak("Begin see pee are if necessary.")
    speak("loosen tight clothing and jewelry, and cover with a blanket to prevent chilling.")
    speak("Don't let the victim eat or drink.")
    speak("If the victim is vomitting or bleeding out of the mouth, and no spinal injury is suspected, turn the victim on their side to prevent choking.")
    speak("Treat for injuries.")
    speak("Calmly reassure the victim.")
def heartAttack():
    phrase("Heart attack first aid.")
    noo()
    phrase("chew and swallow aspririn, if possible.")
    phrase("If the victim becomes unconcious or doesn't have a pulse, begin see pee are.")
def stroke():
    phrase("Stroke first aid.")
    noo()
def cut():
    phrase("Severe bleeding first aid")
    phrase("If the wound is deep or you're not sure how serious it is, call nine one one")
    phrase("If there is a foreign object left deep in the wound, do not remove it, place bandages around it.")
    phrase("Remove clothing or debris from the wound, Look for the source of the bleeding. There might be more than one wound. Do not try to clean the wound")
    phrase("Cover the wound with sterile gauze or a clean cloth. Apply pressure. Do not apply pressure on a head wound if you suspect a skull fracture")
    phrase("Wrap the wound in a thick bandage and tape. Lift the wound above the heart if possible.")
    phrase("Have the victim lie down. If possibnle, cover the victim with a rug or blanket to prevent loss of body heat.")
    shock()
    phrase("If the blood seeps through the applied bandages, apply more clean bandages and continue pressing on the injured area")
    phrase("Keep the person still, and continue to try to get emergency help from an emergency room or nine one one")
    phrase("After the victim is helped, wash your hands, even if it seems no blood got on you")
def majorBurn():
    phrase("Major burn first aid.")
    phrase("Protect the victim from further harm. Remove them from the source of the burn.")
    phrase("Make sure that the victim is breathing.")
    phrase("Remove jewelry, belts, and other tight items.")
    phrase("Cover the burn loosely with a cloth or gauze.")
    phrase("Raise the burned area if possible")
    shock()
def minorBurn():
    phrase("Minor burn first aid")
    phrase("Run the burn under cold water for ten minutes.")
    phrase("Remove jewelry or other tight items from burn area.")
    phrase("Don't break blisters, as they help defend aginst infection. If one pops, gently clean out the area with water and apply antibiotic ointment")
    phrase("Apply lotion. This helps prevent drying and provides relief.")
    phrase("Bandage the burn loosely with a clean bandage.")
def whichBurn():
    phrase("Is it a major burn or minor burn")
    m=getVoice()
    return m

def burn():
    phrase("Burn first aid.")
    while True:
        m=whichBurn()
        if "major" in m:
            majorBurn()
            break
        elif "minor" in m:
            minorBurn()
            break
        elif "explain" in m:
            print("Diagnose burn?")
        else:
            phrase("Did not understand, say major or minor burn, or say explain to know the difference")

def choking():
    speak("Choking first aid.")
    speak("For an adult, stand to the side and just behind the victim. Place your arm accross the victim's chest to support their body.")
    speak("Bend the victim at the waist to face the ground.")
    speak("Strike five seperate times bectween the victim's shoulderblades with the heel of your hand.")
    speak("If the back blows don't work, give five abdominal thrusts, also known as the heimlich manuver.")
    speak("Alternate between the blows and the thrusts until the blockage is removed")
def dislocate():
    speak("Dislocation first aid.")
    noo()
    speak("Don't move the joint. Splint the affected area nd keep it still. Don't try to force it back into place.")
    speak("Put ice on the injured joint. This can help reduce swelling.")
def electrocuted():
    speak("Electrocution first aid")
    speak("Don't touch the victim if they are still in contact with the electricity source.")
    speak("Don't move a victim with an electrical injury unless there is immediate danger.")
    speak("Call nine one one if there are any exposed wiring or power lines")
    speak("Call nine one one if the following condiions are met.")
    speak("The victim has confusion, severe burns, difficulty breathing, heart rythm problems, cardiac arrest, muscle pain or contractions, seizures, or loss of conciousness")
    speak("Turn off the source of electricity, if possible. If not, use a nonconductive object made of cardboard, plastic, or wood to move the victim from the source of electricity.")
    speak("Begin see pee are if the victim shows no sign of breathing, coughing, or movement.")
    shock()
    speak("Apply a bandage or clean cloth loosely to the wound, Don't use a blanket or towel, as fibers can stick to the burns.")
def faint():
    speak("Fainting first aid.")
    speak("Position the victim on their back.")
    speak("If the victim is not breathing, begin see pee are and call nine one one. Continue until the victim regains conciuosness or help arrives.")
    speak("If the victim is breathing and the victim doesn't have any injuries, raise the legs above heart level about a foot if possible. Loosen belts, collars, or other constrictive clothing.")
    speak("If the victim does not regain conciousness within one minute, call nine one one.")
def brokenBone():
    speak("Broken bone first aid.")
    speak("Call nine one one if the following conditions are met.")
    speak("The broken bone was the result of a major trauma, if the victim isn't breathing or responsive, there is heavy bleeding, the limb or joint appears deformed, the bone has pierced the skin, the extremity of the limb is numb or blue at the end, or if you think a bone is broken in the neck, head, or back.")
    speak("Next, stop any bleeding")
    speak("immobilize the injured area, don't realign the bone.")
    speak("Apply ice pack to limit swelling and reduce pain")
    shock()
def heat():
    speak("Heatstroke first aid")
    noo()
    speak("Do whatever you can to cool the victim. You could")
    speak("Put the victim in a tub of cool water")
    speak("Spray the victim with a garden hose.")
    speak("Sponge the victim with cool water")
    speak("Fan the victim while misting with cool water.")
    speak("Place ice packs or cool, wet towels on th neck, armpits, and groin.")
    speak("Cover the victim with cool, damp sheets.")
    speak("If the victim is concious, offer chilled water, a sports drink containing electrolytes, or a non alcoholic beverage containing caffeine.")
    speak("Begin see pee are if necessary.")


def hypothermia():
    speak("Hypothermia first aid")
    
def bite():
    say("Animal bite or sting first aid")
def poison():
    say("Poison first aid")
def sprain():
    say("sprain or twisted ankle or wrist first aid")
def headTrauma():
    speak("Head trauma first aid")
def frostBite():
    speak("Frostbite first aid.")


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
    elif "frostbite" in cause:
        frostbite()
    elif "bite" in cause or "sting" in cause or "stung" in cause or "bit" in cause:
        sting()
    elif "poison" in cause or "toxic" in cause or "chemical" in cause or "chemicals" in cause:
        poison()
    elif "sprain" in cause or "sprained" in cause or "twisted" in cause or "twist" in cause:
        sprain()
    elif "head" in cause:
        headTrauma()

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