import RPi.GPIO AS GPIO

class Light(object):

    def __init__(self, GPIOPin):
        self.GPIOPin = GPIOPin
        self.state = False
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(GPIOPin, GPIO.OUT)


    def on(self):
        GPIO.output(self.GPIOPin, GPIO.HIGH)
        self.state = True

    def off(self):
        GPIO.output(self.GPIOPin, GPIO.LOW)
        self.state = False

    def toggle(self):
        if self.state:
            self.off()
        else:
            self.on()
