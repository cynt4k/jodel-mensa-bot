import requests
import json

class MensaApi():

    baseurl = ""
    headers = {"Content-Type": "application/json"}

    def __init__(self, mensa):
        self.mensa = mensa

    def getfoodbymensa(self):
        url = MensaApi.baseurl + "{}".format("/".join(["mensa", self.mensa, "food"]))
        response = requests.get(url, headers=MensaApi.headers)

        if response.status_code == 200:
            return json.loads(response.content.decode())

