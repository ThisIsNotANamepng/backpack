import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

def button_callback1(channel):
    print("Button 1 was pushed!")
def button_callback2(channel):
    print("Button 2 was pushed!")
def button_callback3(channel):
    print("Button 3 was pushed!")
def button_callback4(channel):
    print("Button 4 was pushed!")


GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(8,GPIO.RISING,callback=button_callback1) # Setup event on pin 10 rising edge

GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(10,GPIO.RISING,callback=button_callback2)

GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(12,GPIO.RISING,callback=button_callback3)

GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(16,GPIO.RISING,callback=button_callback4)



message = input("Press enter to quit\n\n") # Run until someone presses enter

GPIO.cleanup() # Clean up
