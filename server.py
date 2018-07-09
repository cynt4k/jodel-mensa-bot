from src.misc import settings
import src as app
import os


if __name__ == "__main__":
    settings.init(os.path.dirname(os.path.abspath(__file__)))
    config = settings.parseconfig("config.json")
    app.init(config)
