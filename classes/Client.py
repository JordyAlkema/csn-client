import time
from classes.sensors import Light
from classes.sensors import Button

from classes import Server

class Client(object):

    def __init__(self, config):
        self.config = config
        self.server = Server.Server(config)
        self.alarmStatus = False

        self.lightRed = Light.Light(20)
        self.lightOrange = Light.Light(21)
        self.lightGreen = Light.Light(16)

        self.button = Button.Button(23)

        self.initLights()

    def initLights(self):

        self.lightRed.on()
        self.lightOrange.on()
        self.lightGreen.on()
        time.sleep(2)
        self.lightRed.off()
        self.lightOrange.off()
        self.lightGreen.off()


    def alarmButton(self):
        if self.button.isBeingClicked():
            if self.alarmStatus == False:
                print('Armed')
                self.lightGreen.on()
                self.lightOrange.off()
                self.alarmStatus = True
            else:
                print('Disarmed')
                self.lightGreen.off()
                self.lightOrange.on()
                self.alarmStatus = False

