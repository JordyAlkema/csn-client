import requests
import datetime
import time
from classes import Server

class Client(object):

    def __init__(self, config):
        self.config = config
        self.server = Server.Server(config.get('Server', 'httpAddress'))

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
            request = self.server.post('/heartbeat', send)
        except:
            error = True

        if error or request.status_code != 200:
            print('Heartbeat: Server responded with an error code')
