import RPi.GPIO as GPIO

class Button(object):
    def __init__(self, GPIOPin):
        self.GPIOPin = GPIOPin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(GPIOPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def isBeingClicked(self):
        input_state = GPIO.input(self.GPIOPin)
        if input_state == False:
            return True