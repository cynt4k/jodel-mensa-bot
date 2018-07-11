from threading import Thread
import schedule
from src.jodel import *
import time


class Bot(Thread):

    def __init__(self, account, mensa, api):
        Thread.__init__(self)
        self.account = account
        self.mensa = mensa
        self.api = api

    def post(self):
        # TODO: Implement this shit
        food = self.api.getfoodbymensa()

        posts = self.account.get_last_own_posts()

        print(food)

    def run(self):
        date = self.mensa["date"]["time"]
        if self.mensa["date"]["repeat"] == "daily":
            schedule.every(2).seconds.do(self.post)
            # schedule.every().day.at(date).do(self.post)
        elif self.mensa["date"]["repeat"] == "weekly":
            schedule.every().monday.at(date).do(self.post)


        while True:
            schedule.run_pending()
            time.sleep(1)
