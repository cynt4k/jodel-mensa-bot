from src.bot import Bot
import src.api as api
import schedule
from src.jodel import *

def run():
    print("NOP")

def init(config):
    
    jodelaccount = config["jodel"]["account"]
    location = config["location"]

    account = JodelApi(lat=location["lat"], lng=location["lng"], city=location["city"], config=config,
                       access_token=jodelaccount["access_token"], device_uid=jodelaccount["device_uid"],
                       expiration_date=jodelaccount["expiration_date"], distinct_id=jodelaccount["distinct_id"],
                       refresh_token=jodelaccount["refresh_token"], is_legacy=jodelaccount["is_legacy"])

    Bot(account, config["mensas"][0], api.MensaApi(config["mensas"][0]["id"])).start()

    '''for mensa in config["mensas"]:
        Bot(None, mensa, api.MensaApi(mensa.id)).start()'''