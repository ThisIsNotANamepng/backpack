def button_callback8(channel):
    print("Button 8 was pushed!")
def sayspomethinf(channel):
    print("I said something")
    print(channel)
    os.system("echo ' '")
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




GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.add_event_detect(18,GPIO.RISING,callback=button_callback5) # Setup event on pin 10 rising edge

GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(22,GPIO.RISING,callback=button_callback6)

GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(24,GPIO.RISING,callback=button_callback7)

GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(26,GPIO.RISING,callback=button_callback8)



message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.remove_event_detect(16)
GPIO.add_event_detect(16,GPIO.RISING,callback=sayspomethinf)
input("jbhklbhk")
GPIO.cleanup() # Clean up
