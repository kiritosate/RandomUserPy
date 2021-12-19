import requests
import json

class Client:

    def __init__(self):

        self._URL = "https://randomuser.me/api"
        self.results = json.loads(requests.get(self._URL).content)['results'][0]
    
    def getData(self):

        self._USERDATA = {
            'name': f"{self.results['name']['first']} {self.results['name']['last']}",
            'email': self.results['email'],
            'gender': self.results['gender'],
            'username': self.results['login']['username'],
            'password': self.results['login']['password'],
            'image_large': self.results['picture']['large'],
            'image_medium': self.results['picture']['medium'],
            'image_thumbnail': self.results['picture']['thumbnail'],
        }
         
        return self._USERDATA

        
