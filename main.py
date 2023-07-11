import requests
import os
from dotenv import load_dotenv

class TelegramBot():
    def __init__(self):
        load_dotenv()
        self.__telegram_token = os.getenv('TELEGRAM_TOKEN')
        self.__telegram_url = "https://api.telegram.org/bot" + self.__telegram_token
   
    def getTelegramToken(self):
        return self.__telegram_token

    def getTelegramURL(self):
        return self.__telegram_url
    
    def requestBot(self, endpoint):
        tempUrl = self.getTelegramURL() + "/" + endpoint
        response = requests.get(tempUrl)
        return response.json()

# response = requests.get(url)

# response_json = response.json()
# print(response_json)

TB = TelegramBot()
print(TB.requestBot("getMe"))