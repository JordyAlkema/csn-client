import RPi.GPIO as GPIO

class Button(object):
    def __init__(self, GPIOPin):
        self.GPIOPin = GPIOPin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(GPIOPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def hasBeenClicked(self):
        if self.clicked == True:
            self.clicked = False
            return True
        else:
            return False

    def isBeingClicked(self):
        input_state = GPIO.input(self.GPIOPin)
        if input_state == False:
            print('Clicked')
            self.clicked = True