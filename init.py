import configparser;
import requests;
from apscheduler.schedulers.background import BlockingScheduler

from classes import Client
from classes import Server
from classes.sensors import Light

config = configparser.ConfigParser()
config.read("config.ini")

client = Client.Client(config)
#client.signOn()

orange = Light.Light(20)
orange.on()

scheduler = BlockingScheduler()

heartbeat = scheduler.add_job(client.heartbeat, 'interval', seconds=2.5)

scheduler.start()