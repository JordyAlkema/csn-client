import time
from classes.sensors import Light
from classes.sensors import Button
from classes.sensors import Buzzer
from classes import Alarm

from classes import Server

class Client(object):

    def __init__(self, config, server):
        self.config = config
        self.server = server
        self.alarmStatus = False

        self.lightRed = Light.Light(20)
        self.lightOrange = Light.Light(21)
        self.lightGreen = Light.Light(16)
        self.lightBlue = Light.Light(12)

        self.button = Button.Button(23)
        self.buttonBlack = Button.Button(26)
        self.buttonBlue = Button.Button(19)

        self.buzzer = Buzzer.Buzzer(18)

        self.alarm = Alarm.Alarm(self.server, self.lightGreen, self.lightOrange, self.lightRed, self.buzzer)

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
                self.alarm.arm()
                self.lightGreen.on()
                self.alarmStatus = True
                print('Armed')
            else:
                self.alarm.disarm()
                self.lightGreen.off()
                self.alarmStatus = False
                print('Disarmed')

    def serverAlarmRequest(self, data):
        print(data)
        if data['status'] == 0:
            self.alarm.disarm()
        elif data['status'] == 1:
            self.alarm.arm()
        elif data['status'] == 2:
            self.alarm.trigger()
        elif data['status'] == 3:
            self.alarm.soundAlarm()

    def connectionLost(self):
        self.alarm.trigger()

    def connected(self):
        print('connected')
        self.alarm.disarm()
