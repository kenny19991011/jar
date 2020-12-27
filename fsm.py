from transitions.extensions import GraphMachine
from utils import send_text_message, send_button_message, send_image_message, send_carousel_template
import requests
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction

# global variable
base = ''
taste = ''
deep = ''

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_taste(self, event):
        text = event.message.text
        return text.lower() == "drink"

    def on_enter_taste(self, event):
        title = '口味選擇'
        text = '請選擇你想要的口味'
        btn = [
            MessageTemplateAction(
                label = '偏甜',
                text ='偏甜'
            ),
            MessageTemplateAction(
                label = '偏酸',
                text = '偏酸'
            ),
        ]
        url = 'https://i.imgur.com/MNaMCQN.jpg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_deep(self, event):
        global taste
        text = event.message.text

        if text == '偏甜':
            taste = '偏甜'
            return True
        elif text == '偏酸':
            taste = '偏酸'
            return True
        return False
        
    def on_enter_deep(self, event):
        title = '濃度選擇'
        text = '請選擇你想要的酒感'
        btn = [
            MessageTemplateAction(
                label = '酒感重',
                text = '酒感重'
            ),
            MessageTemplateAction(
                label = '酒感輕',
                text = '酒感輕'
            )
        ]
        url = 'https://i.imgur.com/MNaMCQN.jpg'
        send_button_message(event.reply_token, title, text, btn, url)
    def is_going_to_base(self, event):
        global deep
        text = event.message.text

        if text == '酒感重':
            deep = '酒感重'
            return True
        elif text == '酒感輕':
            deep = '酒感輕'
            return True
        
        return False

    def on_enter_base(self, event):
        #send_text_message(event.reply_token, '呱呱呱')
        send_carousel_template(event.reply_token)

    def is_going_to_spe(self, event):
        global base
        text = event.message.text

        if text == '琴酒':
            base = '琴酒'
            return text.lower() == "gin"
        elif text == '伏特加':
            base = '伏特加'
            return text.lower() == "volka"
        elif text == '威士忌':
            base = '威士忌'
            return text.lower() == "whiskey"
        elif text == '龍舌蘭':
            base = '龍舌蘭'
            return text.lower() == "tequlia"
        elif text == '白蘭地':
            base = '白蘭地'
            return text.lower() == "brandy"
        elif text == '蘭姆酒':
            base = '蘭姆酒'
            return text.lower() == "rum"
        return False

    def on_enter_spe(self, event):
       send_text_message(event.reply_token, '呱呱呱呱')