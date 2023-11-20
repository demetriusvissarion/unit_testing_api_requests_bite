import time

class TimeError:
    def __init__(self, requester, time) -> None:
        self.requester = requester
        self.time = time

    # Returns difference in seconds between the time on an external server
    # and the time on this computer
    def error(self):
        return self._get_server_time() - self.time

    # The underscore denotes this is a private method not to be called from the
    # outside. You also shouldn't stub it in your tests. So if your tests contain
    # the words `get_server_time`, you're on the wrong track.
    def _get_server_time(self):
        response = self.requester.get("https://worldtimeapi.org/api/ip")
        json = response.json()
        print(f'my_time: {self.time}')
        print(f'JSON Response: {json}')
        return json["unixtime"]


# Usage
# =====
# import requests
# my_time = time.time()
# time_error = TimeError(requests, my_time)
# print(time_error.error())