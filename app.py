# encoding: utf-8
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('jYLAolTkkFliBdPR+YIrMD+SZTVxbep1mQ3xPzY1M59Cw8A7CG5vWnxNoiKXgZlABN17USaOsKNfZEYj7f8ET/UjI+UkgmCybec+wgVl9phY8SysQZO+7OnDq2Q63cq5AUuLD/pR66fqRGC6nEdhkQdB04t89/1O/w1cDnyilFU=') #Your Channel Access Token
handler = WebhookHandler('8fa92eb727d454dc1b2af572dc6ae2f1') #Your Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text #message from user

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=text)) #reply the same message from user
    

import os
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=os.environ['PORT'])
