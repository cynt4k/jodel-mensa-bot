import jodel_api

class JodelApi(jodel_api.JodelAccount):

    def __init__(self, lat, lng, city, **kwargs):
        super().__init__(lat, lng, city, **kwargs)


    def get_last_own_posts(self, skip=0, limit=60, after=None, hashtag=None, channel=None, **kwargs):
        return self._get_posts('', skip, limit, after, True, hashtag, channel, **kwargs)


    def get_last_own_post(self, after=None, hashtag=None, channel=None, **kwargs):
        rawposts = self._get_posts('', 0, 60, after, True, hashtag, channel, **kwargs)

        posts = sorted(rawposts.items(), key=lambda kv: kv["created_at"])

        return posts[0]
