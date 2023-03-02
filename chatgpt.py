import time
from revChatGPT.V1 import Chatbot
from const import ACCESS_TOKEN


class ChatGptManager():
    def __init__(self,proxy:str=None):
        cfg = {
            'access_token': ACCESS_TOKEN,
        }
        if proxy:
            cfg['proxy'] = proxy
        self.bot = Chatbot(cfg)

    def ask(self, prompt):
        response = ""
        for data in self.bot.ask(
            prompt
        ):
            response = data["message"]
        return response
    
    def get_cov_id(self):
        return self.bot.get_conversations()

if __name__ == "__main__":
    bot = ChatGptManager(proxy='http://127.0.0.1:10810')
    print(bot.get_cov_id())
    