import requests 

class BotHandler:
    
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)
        
    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json
    
    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp
    
    def get_last_update(self):
        get_result = self.get_updates()
        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]
        return last_update

dv_bot = BotHandler("443743656:AAH-NUwl0gDj-0W8hYMaUQUc5IcEuh-wOOU")

triggers = ["deja vu",
            "higher on the street",
            "calling you",
            "standing on my feet!"]

responses = ["I've just been in this place before!",
             "And I know it's my time to come home!",
             "And the subject's a mystery!",
             "It's so hard when I try to believe! Whooooaaa!"]
def main():
    
    new_offset = None
    
    while True:
        
        dv_bot.get_updates(new_offset)
        last_update = dv_bot.get_last_update()
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text'].lower()
        last_chat_id = last_update['message']['chat']['id']

        for i in range(len(triggers)):
            if triggers[i] in last_chat_text:
                dv_bot.send_message(last_chat_id,responses[i])

        new_offset = last_update_id + 1
    
    return
        
if __name__ == '__main__':  
    try:
        main()
    except KeyboardInterrupt:
        exit()
