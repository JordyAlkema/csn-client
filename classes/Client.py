import time
from classes.sensors import Light
from classes.sensors import Button
from classes import Alarm

from classes import Server

class Client(object):

    def __init__(self, config):
        self.config = config
        self.server = Server.Server(config)
        self.alarmStatus = False
        self.alarm = Alarm.Alarm()

        self.lightRed = Light.Light(20)
        self.lightOrange = Light.Light(21)
        self.lightGreen = Light.Light(16)
        self.lightBlue = Light.Light(12)

        self.button = Button.Button(23)
        self.buttonBlack = Button.Button(26)
        self.buttonBlue = Button.Button(19)

        self.initLights()

    def initLights(self):

        self.lightRed.on()
        self.lightOrange.on()
        self.lightGreen.on()
        self.lightBlue.on()
        time.sleep(2)
        self.lightRed.off()
        self.lightOrange.off()
        self.lightGreen.off()
        self.lightBlue.off()


    def alarmButton(self):

        if self.buttonBlack.isBeingClicked():
            if self.alarmStatus == True:
                print('Alarm is triggered')
                self.alarm.trigger()

        if self.buttonBlue.isBeingClicked():
            if self.alarmStatus == False:
                print('Armed')
                self.lightGreen.on()
                self.alarmStatus = True
            else:
                print('Disarmed')
                self.lightGreen.off()
                self.alarmStatus = False

