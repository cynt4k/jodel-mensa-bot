import os
import configparser
from dotenv import load_dotenv
from pathlib import Path
import src.api as api
import jodel_api
import json

config = ""

def init(path):
    env = ""
    env_path = ""
    try:
        env = os.environ["PYTHON_ENV"]
    except KeyError:
        print("No environment specified")
        exit(1)

    if env == "prod":
        env_path = Path(path) / ".env-prod"
    elif env == "dev":
        env_path = Path(path) / ".env-dev"
    elif env == "test":
        env_path = Path(path) / ".env-test"
    else:
        print("This environment is invalid")
        exit(1)

    load_dotenv(dotenv_path=env_path)
    try:
        jodel_api.JodelAccount.secret = os.environ["JODEL_APIKEY"].encode('ascii')
        jodel_api.JodelAccount.version = os.environ["JODEL_VERSION"]
        api.MensaApi.baseurl = os.environ["MENSA_API_URL"] + "/"
    except KeyError as e:
        print("Environment variable " + str(e) + " not defined")


def parseconfig(file):
    with open(file, "r") as f:
        config = json.load(f)
        return config



def writeconfig(data):
    with open(config, "w") as f:
        json.dump(data, f)