import configparser;
from apscheduler.schedulers.background import BackgroundScheduler

from classes import Client
from classes import Server

config = configparser.ConfigParser()
config.read("config.ini")

server = Server.Server(config)
client = Client.Client(config, server)

scheduler = BackgroundScheduler()

# for detecting button input
alarmSwitch = scheduler.add_job(client.alarmButton, 'interval', seconds=0.1)

# for watching for socket events
server.socket.on('alarm', client.serverAlarmRequest)
server.socket.on('disconnect', client.connectionLost)
server.socket.on('reconnect', client.reconnect)
server.socket.on('connect', client.connected)

scheduler.start()

server.socket.wait()
