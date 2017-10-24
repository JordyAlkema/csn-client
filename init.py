import configparser;
import requests;
from apscheduler.schedulers.background import BlockingScheduler

from classes import Client
from classes import Server
from classes.sensors import Button

config = configparser.ConfigParser()
config.read("config.ini")

client = Client.Client(config)
button = Button.Button(23)
#client.signOn()

scheduler = BlockingScheduler()

heartbeat = scheduler.add_job(client.heartbeat, 'interval', seconds=2.5)
watchButton = scheduler.add_job(button.isBeingClicked, 'interval', seconds=0.1)

scheduler.start()
