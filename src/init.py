from src.bot import Bot
import src.api as api
import schedule

def run():
    print("NOP")

def init(config):

    Bot(None, config["mensas"][0], api.MensaApi(config["mensas"][0]["id"])).start()

    '''for mensa in config["mensas"]:
        Bot(None, mensa, api.MensaApi(mensa.id)).start()'''