import configparser;
import requests;
from socketIO_client import SocketIO
from apscheduler.schedulers.background import BlockingScheduler

from classes import Client
from classes import Server
from classes.sensors import Button

config = configparser.ConfigParser()
config.read("config.ini")

client = Client.Client(config)
server = Server.Server(config)

scheduler = BlockingScheduler()

alarmSwitch = scheduler.add_job(client.alarmButton, 'interval', seconds=0.1)
SocketIO.on('alarm', client.serverAlarmRequest)

scheduler.start()
