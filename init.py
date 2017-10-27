import configparser;
import requests;
from socketIO_client import SocketIO
from apscheduler.schedulers.background import BlockingScheduler

from classes import Client
from classes import Server
from classes.sensors import Button

config = configparser.ConfigParser()
config.read("config.ini")

server = Server.Server(config)
client = Client.Client(config, server)

scheduler = BlockingScheduler()

alarmSwitch = scheduler.add_job(client.alarmButton, 'interval', seconds=0.1)
SocketIO.on('alarm', client.serverAlarmRequest)

scheduler.start()
