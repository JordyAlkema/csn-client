import RPi.GPIO as GPIO

class Buzzer(object):
    def __init__(self, GPIOPin):
        self.GPIOPin = GPIOPin
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(GPIOPin, GPIO.OUT)
        self.buzzer = GPIO.PWM(GPIOPin, 250)

    def start(self):
        self.buzzer.start(50)

    def stop(self):
        self.buzzer.stop()