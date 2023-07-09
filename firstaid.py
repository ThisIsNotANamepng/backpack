
def none(t="t"):
    print("Button pressed")
    pass

def markyes(t="t"):
    print("Marked yes")
    global yes_no
    yes_no=True

def markno(t="t"):
    speak("Marked no")
    global yes_no
    yes_no=False

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
    speak("Heart attack first aid.")
    noo()
    speak("chew and swallow aspririn, if possible.")
    speak("If the victim becomes unconcious or doesn't have a pulse, begin see pee are.")
def stroke():
    speak("Stroke first aid.")
    noo()
def cut():
    speak("Severe bleeding first aid")
    speak("If the wound is deep or you're not sure how serious it is, call nine one one")
    speak("If there is a foreign object left deep in the wound, do not remove it, place bandages around it.")
    speak("Remove clothing or debris from the wound, Look for the source of the bleeding. There might be more than one wound. Do not try to clean the wound")
    speak("Cover the wound with sterile gauze or a clean cloth. Apply pressure. Do not apply pressure on a head wound if you suspect a skull fracture")
    speak("Wrap the wound in a thick bandage and tape. Lift the wound above the heart if possible.")
    speak("Have the victim lie down. If possibnle, cover the victim with a rug or blanket to prevent loss of body heat.")
    shock()
    speak("If the blood seeps through the applied bandages, apply more clean bandages and continue pressing on the injured area")
    speak("Keep the person still, and continue to try to get emergency help from an emergency room or nine one one")
    speak("After the victim is helped, wash your hands, even if it seems no blood got on you")
def majorBurn():
    speak("Major burn first aid.")
    speak("Protect the victim from further harm. Remove them from the source of the burn.")
    speak("Make sure that the victim is breathing.")
    speak("Remove jewelry, belts, and other tight items.")
    speak("Cover the burn loosely with a cloth or gauze.")
    speak("Raise the burned area if possible")
    shock()
def minorBurn():
    speak("Minor burn first aid")
    speak("Run the burn under cold water for ten minutes.")
    speak("Remove jewelry or other tight items from burn area.")
    speak("Don't break blisters, as they help defend aginst infection. If one pops, gently clean out the area with water and apply antibiotic ointment")
    speak("Apply lotion. This helps prevent drying and provides relief.")
    speak("Bandage the burn loosely with a clean bandage.")
def whichBurn():
    speak("Is it a major burn or minor burn")
    m=getVoice()
    return m

def burn():
    speak("Burn first aid.")
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
            speak("Did not understand, say major or minor burn, or say explain to know the difference")

def choking():
    speak("Choking first aid.")
    speak("For an adult, stand to the side and just behind the victim. Place your arm accross the victim's chest to support their body.")
    speak("Bend the victim at the waist to face the ground.")
    speak("Strike five seperate times bectween the victim's shoulderblades with the heel of your hand.")
    speak("If the back blows don't work, give five abdominal thrusts, also known as the heimlich manuver.")
    speak("Alternate between the blows and the thrusts until the blockage is removed")
def dislocated():
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
def fainted():
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
def heatStroke():
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
    noo()
    speak("Remove the victim from the cold. Go inside if possible.")
    speak("Gently remove wet clothing. Replace wet clothing with warm, dry clothing or blankets.")
    speak("If further warming is necessary, do so gradually. For example, apply dry compresses to the cneter of the body, chest, neck, and groin.")
    speak("Use an electric blanket if available.")
    speak("If you use a warm water bottle, wrap it in a towel first.") 
    speak("Offer the victim warm, sweet, non alcoholic drinks.")
    speak("Begin see pee are if necessary.")
    speak("Do not warn the victim too quickly, such as with a heating lamp or a warm bath.")
    speak("Don't attempt to warm the arms or legs. Massaging or heating the limbs can stress the heart and lungs.")
def sting():
    speak("Animal bite or sting first aid")
    speak("Call nine one one if the victim has trouble breathing, swelling in the face or throat, dizziness, fainting, unconciousness, a weak or rapid pulse, hives, nasuea, vomiting, diarrhea, the wound is deep or you don't know how serious it is, the skin is badly torn, crushed, or bleeding significantly, you notice swelling, redness, or oozing, you were in contact with a bat, or if you think the animal might have had rabies.")
    speak("While waiting for emergency help, ask the victim if they have an epinephrine injectory and whether you should inject it, loosen tight clothing and jewelry, don't offer anything to drink, and if needed, position the victim to prevent choking on vomit.")
    speak("For mild reactions, move to a safe area, remove any stingers, gently wash the area with soap and water, and apply cold water or ice for ten to twenty minutes.")
def spiderBite():
    speak("Spider bite first aid.")
    speak("Call nine one one if the victim was bitten by a dangerous spider, you are unsure if the spider was dangerous, the victim has severe pain, the victim has cramping, the victim has a growing wound at the bite site, the victim has problems breathing or swallowing, or if the area has spreading redness or red streaks.")
def snakeBite():
    speak("Snake bite first aid.")
    speak("If the snake bite was from a venomous snake, or if the bite area changes color, begins to dwell, or is painful, call nine one one.")
    speak("While waiting for emergency assistance, move beyond the snake's striking distance, keep the victim calm to slow the spread of venom, remove tight clothing or jewerly, position the victim so the bite is below the heart, clean the wound with soap and water, and cover it with a dry dressing.")
    speak("Do not use a tourniquet or apply ice.")
    speak("Do not cut the wound or attempt to remove the venom.")
    speak("Do not drink caffeine or alchohol.")
    speak("Do not try to capture the snake. Try to remember the snake's color and shape, and if possible, take a picture of it.")
def tick():
    speak("Tick first aid.")
    speak("Get tweezers. Grasp the tick as close to the skin as possible, and gently pull it out with a slow and steady upward motion. When it's out, take a picture of it to show a doctor.")
    speak("Do not twist or squeeze the tick with the tweezers. Do not use your bare hands. Do not use petroleum jelly, nail polish, or matches.")
    speak("Secure the tick by sticking it to a piece of tape and take a picture of it, if you haven't done so already.")
    speak("Wash your hands and the area with soap and water.")
    speak("Call nine one one if you develop a severe headache, have difficulty breathing, have paralysis, or heart palpitations.")
    speak("Contact your doctor if you aren't able to compeletely remove the tick, the rash at the site gets bigger after removal, you develop flu like symptoms, you think the bite is infected, or if you think you were bitten by a deer tick.")
def poison():
    speak("Poison first aid")
    speak("If the victim is not experiencing symptoms, or is being transported to medical help, visit poison dot org to get instructions.")
    speak("If the victim is eperiencing symptoms, or overdosed, call nine one one")
    speak("Visit poison dot org or call the poison hot line at eight hundered, two two two, one two two two for assistance.")
    speak("While waiting for emergency help to arrive, remove the victim from the poison.")
    speak("If the poison was swallowed, remove any remaining poison from the victim's mouth. If the poison was from a cleaning solution, read the bottle's label for instructions on accidental poisoning.")
    speak("If the poison is on the skin, remove any contaminated clothing and rinse the affected areas under water for fifteen to twenty minutes.")
    speak("If the posion is in the eye, remove any contact lenses and rinse the affected eye with lukewarm water for twenty minutes.")
    speak("If the poison was inhaled, get the person into fresh air.")
    speak("If the victim vomites, turn their head to the side to avoid choking.")
    speak("Have someone gather pill bottles, cleaning containers, or labels about the poison to give the medical assistance. ")
def sprain():
    speak("Sprain first aid.")
    speak("Follow the instructions for rice.")
    speak("Rest the injured limb. Try not to put weight on it.")
    speak("Ice the areas soon as possible. Continue to ice it for fifteen to twenty minutes, four to eight times a day for two days.")
    speak("Compress the area with an elastic wrap or bandage.")
    speak("Elevate the area above the heart to prevent swelling.")
    speak("Get medical help if you're unable to put weight on the joint, the joint feels numb, you can't move the joint, you develop redness or red streaks which start at the injured area, you have pain directly over the bones of an injured joint, you have injured an area which has been injured many times in the past, or you have severe pain.")
def headTrauma():
    speak("Head trauma first aid.")
    speak("Call nine one one if the following conditions are met.")
    speak("Severe head or facial bleeding, blood or leakage from nose or ears, vomiting, severe headache, change in conciousness for more than a few seconds, black and blue discoloration below the eyes or behind the ears, confusion, agitation, loss of balance, weakness or inability to use an arm or a leg, unequal pupil size, slurred speech, or seizures.")
    speak("While waiting for nine one one, keep the victim still. Lie the victim down with their head and shoulders slightly elevated. Don't move them unless absolutely necessary, if the victim is wearing a helmet, don't remove it.")
    speak("Stop any bleeding with gently applied pressure with clean washclothes or gauze.")
    speak("Watch for changes in breathing and alertness.")
def spinalInjury():
    speak("Spinal injury first aid.")
    noo()
    speak("Don't move the victim. Place rolled up heavy towels or blankets on either side of the victim's head to keep the victim's head and neck still.")
    speak("If see pee are is necessary, do chest compressions and pull the jaw forward to give mouth to mouth.")
    speak("If you need to roll the victim over to prevent choking, do so with one person rolling the head while another rolls the side to keep the neck and back aligned.")
def frostBite():
    speak("Frostbite first aid.")
    speak("Protect the skin from further damage.")
    speak("Check for signs of hypothermia.")
    speak("Get the victim out of the cold.")
    speak("Gently warm the affected areas by soaking the area in very warm, not hot, water for twenty to thirty minutes.")
    speak("If you cannot soak the area in water, apply warm, wet washcloths.")
    speak("Do not warm frotbitten with direct heat, such as a stove, lamp, fireplace, or heating pad, as this can cause burns.")
    speak("Drink non alcoholic, warm liquids.")
    speak("As the skin warms, the victim should feel tingling. Do not break any blisters that form.")
    speak("for anything more than mild frostbite, seek medical help.")
def overdose():
    speak("Drug overdose first aid.")
    noo()
    speak("Wear gloves when helping the victim. Don't touch any pills, bottles, or powder you see.")
    speak("Do not enter any area that appears unsafe.")
    speak("Administer Naloxone if available.")
    speak("Roll the victim on their side and keep the airway open to prevent choking.")
    speak("Monitor the victim and give see pee are if necessary.")


def diagnose():
    speak("Diagnose")

def causeKnown():
    speak("What is the cause?")

    input("Looking for cause, which is known")

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
        frostBite()
    elif "snake" in cause:
        snakeBite()
    elif "spider" in cause:
        spiderBite()
    elif "tick" in cause:
        tick()
    elif "bite" in cause or "sting" in cause or "stung" in cause or "bit" in cause:
        sting()
    elif "poison" in cause or "toxic" in cause or "chemical" in cause or "chemicals" in cause:
        poison()
    elif "sprain" in cause or "sprained" in cause or "twisted" in cause or "twist" in cause:
        sprain()
    elif "head" in cause:
        headTrauma()
    elif "overdose" in cause or "overdosed" in cause or "over" and "dose" in cause:
        overdose()


def startFirstAid(again):

    # The buttons do yes/no and scroll through conditions if the conditions is known
    GPIO.remove_event_detect(10)
    GPIO.remove_event_detect(11)
    GPIO.remove_event_detect(12)
    GPIO.remove_event_detect(13)
    GPIO.remove_event_detect(15)
    GPIO.remove_event_detect(16)
    GPIO.remove_event_detect(18)
    GPIO.remove_event_detect(19)

    GPIO.add_event_detect(10,GPIO.RISING,callback=markyes, bouncetime=500)
    GPIO.add_event_detect(11,GPIO.RISING,callback=markno, bouncetime=500)
    GPIO.add_event_detect(12,GPIO.RISING,callback=none, bouncetime=500)
    GPIO.add_event_detect(13,GPIO.RISING,callback=none, bouncetime=500)
    GPIO.add_event_detect(15,GPIO.RISING,callback=volumeUp, bouncetime=500)
    GPIO.add_event_detect(16,GPIO.RISING,callback=volumeDown, bouncetime=500)
    GPIO.add_event_detect(18,GPIO.RISING,callback=none, bouncetime=500)
    GPIO.add_event_detect(19,GPIO.RISING,callback=none, bouncetime=500)



    speak("Do you know what the problem is?")

    i=0
    while i<600:
        if yes_no!="":
            if yes_no==True:
                causeKnown()
                break

            elif yes_no==False:
                diagnose()
                break
        i+=1
        time.sleep(0.1)
    if i==599:
        #Never responded, go back to main menu
        print("Done")
    else:
        print("Got an answer")
        print("yes_no:", yes_no)
    yes_no=""


