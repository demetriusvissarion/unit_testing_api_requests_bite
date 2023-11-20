import time

class TimeError:
    def __init__(self, requester) -> None:
        self.requester = requester

    # Returns difference in seconds between the time on an external server
    # and the time on this computer
    def error(self):
        return self._get_server_time() - time.time()

    # The underscore denotes this is a private method not to be called from the
    # outside. You also shouldn't stub it in your tests. So if your tests contain
    # the words `get_server_time`, you're on the wrong track.
    def _get_server_time(self):
        response = self.requester.get("https://worldtimeapi.org/api/ip")
        json = response.json()
        return json["unixtime"]


# Usage
# =====
import requests
time_error = TimeError(requests)
time_error.error() # => "Why not: Learn how to use a french press"
# time_error.error() # => "Why not: Hold a video game tournament with some friends"