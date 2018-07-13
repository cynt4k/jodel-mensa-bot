import jodel_api
import time
import schedule
from threading import Thread
from src.misc import settings

class JodelApi(jodel_api.JodelAccount):

    def __init__(self, lat, lng, city, config, **kwargs):
        super().__init__(lat, lng, city, **kwargs)
        self.config = config
        Thread(target=self.refresh_schedule).start()



    def get_last_own_posts(self, skip=0, limit=60, after=None, hashtag=None, channel=None, **kwargs):
        return self._get_posts('', skip, limit, after, True, hashtag, channel, **kwargs)


    def get_last_own_post(self, after=None, hashtag=None, channel=None, **kwargs):
        rawposts = self._get_posts('', 0, 60, after, True, hashtag, channel, **kwargs)

        posts = sorted(rawposts.items(), key=lambda kv: kv["created_at"])

        return posts[0]

    def need_refresh(self):
        epoch_time = int(time.time()) - 300
        if epoch_time > self.expiration_date:
            return True

        return False

    def refresh_task(self):
        if self.need_refresh():
            data = self.refresh_access_token()
            if (data[0] != 200):
                return Exception("Failed to refresh token")
            self.access_token = data["access_token"]
            self.expiration_date = data["expiration_date"]
            print("New Jodel token: " + self.access_token + " and expiration date: " + str(self.expiration_date))
            settings.writeconfig(self.config)




    def refresh_schedule(self):
        schedule.every(5).seconds.do(self.refresh_task)

        while(True):
            schedule.run_pending()
            time.sleep(1)
