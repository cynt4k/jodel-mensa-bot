import requests
import json

class MensaApi():

    baseurl = ""
    headers = {"Content-Type": "application/json"}

    def __init__(self, mensa):
        self.mensa = mensa


    def get_mensa_name(self):
        url = MensaApi.baseurl + "{}".format("/".join(["mensa", self.mensa]))
        try:
            response = requests.get(url, headers=MensaApi.headers)
        except ConnectionError as e:
            print("jo")

        if response.status_code == 200:
            return json.loads(response.content.decode())["data"]["name"]

    def getfoodbymensa(self):
        url = MensaApi.baseurl + "{}".format("/".join(["mensa", self.mensa, "food"]))
        try:
            response = requests.get(url, headers=MensaApi.headers)
        except ConnectionError as e:
            print("jo")

        if response.status_code == 200:
            return json.loads(response.content.decode())["data"]

    def get_food_by_mensa_today(self):
        url = MensaApi.baseurl + "{}".format("/".join(["mensa", self.mensa, "food", "mon"]))
        try:
            response = requests.get(url, headers=MensaApi.headers)
        except ConnectionError as e:
            print("jo")

        if response.status_code == 200:
            return json.loads(response.content.decode())["data"]

