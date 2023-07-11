from telethon import TelegramClient, events, sync
import os
from dotenv import load_dotenv

# Use your own values from my.telegram.org
# api_id = 27245740
# api_hash = '6b7deb2f0a8fb4fa4aaf58492299763a'
load_dotenv()
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

channels = ["xetdaspromocoes", "LinksBrazil"]
palavrasBusca = ["Suporte", "Articulado", "Fire", "Stick", "Monitor"]
tempFile = "tmp/tempFile.txt"
receivers = ["gabrielrbernardi"]
# receivers = ["gabrielrbernardi", "gabrielrbernardi"]
# receivers = ["gabrielrbernardi", "yasminmv"]

class TelegramBot:
    def __init__(self):
        self.messagesToBeSent = ""

    def readChannelsMessages(self):
        client = TelegramClient('MyUser', api_id, api_hash)
        client.start()
        self.tempMessages = []
        for channel in channels:
            # self.messagesToBeSent += "\n\n" + channel + "\n\n"
            for message in client.get_messages(channel, limit=100):
                for x in palavrasBusca:
                    if message.message.find(x) != -1:
                        if message.message.find("shope") == -1 and message.message.find("aliexp") == -1:
                            if message.message in self.tempFileContent:
                                continue
                            self.messagesToBeSent += "\n" + message.message + "\n"
                            self.tempMessages.append(message.message)
        
        if self.tempMessages != []:
            f = open(tempFile, "w", encoding="UTF-8")
            for x in self.tempMessages:
                f.write(x + "\n")
            f.close()

    def sendMessages(self):
        self.messagesToBeSent = self.messagesToBeSent.replace("""

-""", "\n-")
        self.messagesToBeSent = self.messagesToBeSent.replace("""

h""", "\nh")
        if self.messagesToBeSent == "":
            return
        client = TelegramClient('MyBot', api_id, api_hash)
        client.start()
        for receiver in receivers:
            client.send_message(receiver, self.messagesToBeSent)

    def checkTempFile(self):
        f = open(tempFile, "r", encoding="UTF-8")
        self.tempFileContent = f.read()
        f.close()

# print(client.get_me().stringify())

# client.download_profile_photo('me')
# messages = client.get_messages('xetdaspromocoes')
# messages[0].download_media()

TB = TelegramBot()
TB.checkTempFile()
TB.readChannelsMessages()
TB.sendMessages()
