import requests
import datetime
import time
from classes.sensors import Light
from classes.sensors import Button

from classes import Server

class Client(object):

    def __init__(self, config):
        self.config = config
        self.server = Server.Server(config.get('Server', 'httpAddress'))
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
        time.sleep(0.5)



    def signOn(self):
        send = {
            'client': self.config.get('Client', 'clientKey'),
            'timestamp': '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        }

        while True:
            print('Attempting sign-on')
            request = self.server.post('/signOn', send)

            if request.status_code == 200:
                print('Signed on')
                break;
            else:
                print('Failed, retrying...')
                time.sleep(2)
        print(requests)

    def heartbeat(self):
        send = {
            'client': self.config.get('Client', 'clientKey'),
            'timestamp': '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        }

        error = False

        try:
            self.lightRed.on()
            request = self.server.post('/heartbeat', send)
            self.lightRed.off()
        except:
            error = True
            self.lightRed.off()

        if error or request.status_code != 200:
            print('Heartbeat: Server responded with an error code')

    def alarmButton(self):
        if self.button.isBeingClicked():
            if self.alarmStatus:
                self.lightGreen.on()
                self.alarmStatus == True
            else:
                self.lightGreen.off()
                self.alarmStatus == False

