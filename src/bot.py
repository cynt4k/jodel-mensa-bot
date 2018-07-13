from threading import Thread
import schedule
from src.jodel import *
import time


class Bot(Thread):

    def __init__(self, account, mensa, api, templates):
        Thread.__init__(self)
        self.account = account
        self.mensa = mensa
        self.api = api
        self.templates = templates

    def post(self):
        # TODO: Implement this shit
        food = self.api.get_food_by_mensa_today()

        mensa, messages = self.parse_food(food)
        post_id = ""
        try:
            res = self.account.create_post(mensa)

            if res[0] != 200:
                return Exception("Error at posting: " + str(res[1]))

            post_id = res[1]["post_id"]
            time.sleep(5)
            #print(mensa)
        except Exception as e:
            print(e)

        for message in messages.items():
            res = self.account.create_post(message[1]["message"], ancestor=post_id)
            time.sleep(15)
            while res[0] != 200 or len(res[1]) == 0:
                res = self.account.create_post(message[1]["message"], ancestor=post_id)
                time.sleep(5)
            #print(message[1]["message"])
            for meal in message[1]["meals"]:
                res = self.account.create_post(meal, ancestor=post_id)
                time.sleep(15)
                while res[0] != 200 or len(res[1]) == 0:
                    res = self.account.create_post(meal, ancestor=post_id)
                    time.sleep(5)
                #print(meal)


        print("jo")

    def parse_food(self, food):
        parsedfood = dict()
        mensa_name = self.api.get_mensa_name()
        mensa = self.templates["message"].replace("<MENSA_NAME>", mensa_name)

        for category in food:
            name = ""
            if category["name"] == "Hauptgerichte":
                name = "mainmeal"
            elif category["name"] == "Suppen":
                name = "soup"
            elif category["name"] == "Beilagen":
                name = "sidedishfood"
            elif category["name"] == "Nachspeisen":
                name = "dessert"
            else:
                continue
            parsedfood[name] = {"message": self.templates[name], "meals": []}

            for meal in category["meal"]:
                message = self.templates["food"].replace("<NAME>", meal["name"]).replace("<PRICE>", meal["price"])
                parsedfood[name]["meals"].append(message)

        return mensa, parsedfood


    def run(self):
        date = self.mensa["date"]["time"]
        if self.mensa["date"]["repeat"] == "daily":
            # schedule.every(30).seconds.do(self.post)
            self.post()
            # schedule.every().day.at(date).do(self.post)
        elif self.mensa["date"]["repeat"] == "weekly":
            schedule.every().monday.at(date).do(self.post)


        while True:
            schedule.run_pending()
            time.sleep(1)
