import requests
from socketIO_client import SocketIO


class Server(object):
    alarmDisarmed = 0
    alarmArmed = 1
    alarmTriggered = 2
    alarmGoingOff = 3

    def __init__(self, config):
        self.clientID = config.get('Client', 'clientID')
        self.http = config.get('Server', 'httpAddress')
        self.port = config.get('Server', 'port')

        print('opening connection tot the server')
        self.socket = SocketIO(self.http, self.port, params={
            'client_id': self.clientID
        })

        print('server connection opened')

    # 0 = off, 1 = armed, 2 = triggered, 3 = going off
    def alarm(self, status):
        self.socket.emit('alarm', {
            'status': status
        })

    def alarmIsArmed(self):
        return self.alarm(self.alarmArmed)

    def alarmIsDisarmed(self):
        return self.alarm(self.alarmDisarmed)

    def alarmIsTriggered(self):
        return self.alarm(self.alarmTriggered)

    def alarmIsGoingOff(self):
        return self.alarm(self.alarmGoingOff)
