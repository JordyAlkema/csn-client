import requests

class Server(object):

    def __init__(self, httpAddress):
        self.http = httpAddress

    def get(self, url):
        return requests.get(self.http + url)

    def post(self, url, parameters):
        return requests.post(self.http + url, parameters)