import configparser;
import requests;
from apscheduler.schedulers.background import BlockingScheduler

from classes import Client
from classes import Server
from classes.sensors import Button

config = configparser.ConfigParser()
config.read("config.ini")

client = Client.Client(config)

#client.signOn()

scheduler = BlockingScheduler()

heartbeat = scheduler.add_job(client.heartbeat, 'interval', seconds=2.5)
watchButton = scheduler.add_job(client.alarmButton, 'interval', seconds=0.2)

scheduler.start()
