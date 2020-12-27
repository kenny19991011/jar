import os

from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage, TextSendMessage, ImageSendMessage, TemplateSendMessage, TemplateAction, Template, PostbackTemplateAction, ImageCarouselColumn, ImageCarouselTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, BaseSize, URIImagemapAction, ImagemapArea, MessageImagemapAction, ImageSendMessage, ImagemapSendMessage, CarouselTemplate, CarouselColumn, PostbackEvent


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)


def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"

def send_image_message(reply_token, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = ImageSendMessage(
        type='image',
        original_content_url=url,
        preview_image_url=url
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"
    
def send_button_message(reply_token, title, text, btn, url):
    line_bot_api = LineBotApi(channel_access_token)
    message = TemplateSendMessage(
        alt_text='button template',
        template = ButtonsTemplate(
            title = title,
            text = text,
            thumbnail_image_url = url,
            actions = btn
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"
def send_carousel_template(reply_token):
    line_bot_api = LineBotApi(channel_access_token)
    url = 'https://i2.kknews.cc/SIG=1nh5bt4/ctp-vzntr/1531818136622rnrq3q71rn.jpg'
    Carousel_template = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://i2.kknews.cc/SIG=1nh5bt4/ctp-vzntr/1531818136622rnrq3q71rn.jpg',                   
                    title='選擇基酒',
                    text='想喝什麼基酒？',
                    actions=[            
                        MessageTemplateAction(
                            label = "琴酒",
                            text = "琴酒"
                        ),  
                        MessageTemplateAction(
                            label = "伏特加",
                            text = "伏特加"
                        ),  
                        MessageTemplateAction(
                            label = "威士忌",
                            text = "威士忌"
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://i2.kknews.cc/SIG=1nh5bt4/ctp-vzntr/1531818136622rnrq3q71rn.jpg', 
                    title='選擇基酒',
                    text='想喝什麼基酒？',
                    actions=[
                        MessageTemplateAction(
                            label = "龍舌蘭",
                            text = "龍舌蘭"
                        ),  
                        MessageTemplateAction(
                            label = "白蘭地",
                            text = "白蘭地"
                        ),  
                        MessageTemplateAction(
                            label = "蘭姆酒",
                            text = "蘭姆酒"
                        ) 
                    ]
                )         
            ]
        )
    )
    line_bot_api.reply_message(reply_token,Carousel_template)
    return "OK"


