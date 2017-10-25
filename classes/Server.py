import requests
from socketIO_client import SocketIO

class Server(object):

    def __init__(self, config):

        self.clientID = config.get('Client', 'clientID')
        self.http = config.get('Server', 'httpAddress')
        self.port = config.get('Server', 'port')

        # self.socket = SocketIO(self.http, self.port, params={
        #    'client_id': self.clientID
        # })

    def alarm(self, status):
        self.socket.emit('alarm', {

        })
