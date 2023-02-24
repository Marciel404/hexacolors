import requests, http
import http.client

class ClientAPI:

    def __init__(
            self,
            type: str,
            value: str,
        ) -> int:

        self.url = 'https://www.thecolorapi.com/id?{}={}'.format(type, value)
    
    def get(self):

        res = requests.get(self.url).json()
        return res['hex']['clean']