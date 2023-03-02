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



import time

txt = "set a timer for five minutes"

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
print("Setting timer for "+str(tim)+" seconds")
time.sleep(tim)
