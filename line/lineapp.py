from fastapi import FastAPI, Form, File, UploadFile
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextSendMessage, StickerMessage,ImageSendMessage
import shutil

app = FastAPI()

line_bot_api = LineBotApi('tCwVqKI9TPeWF1tTqidRir0xc5xTg4O63koiPELmNYfPQ2oO67XmuHOGRB6I8DnrNSTrEr3QPHgE36GgvLl89LzZoVDTOyFCR/yQMPfaHiQIVPohVzsmJvk0QcDfomMg8mDnMtvfYV/15EeSy1IIBQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('91d0c932fd7e9290e010301dbea5bc7c')

@app.post("/send_message")
async def send_message(message: str=Form(...)):
    line_bot_api.broadcast(TextSendMessage(text=message))
    return {"message": "Message sent successfully"}

@app.post("/send_sticker")
async def send_sticker(package_id: str=Form(...), sticker_id: str=Form(...)):
    line_bot_api.broadcast(StickerMessage(package_id=package_id, sticker_id=sticker_id))
    return {"message": "sticker sent succesfully"}

@app.post("/send_image")
async def send_image(image: UploadFile = File(...)):
    line_bot_api.broadcast(message=[message])
    return {"message" : "image sent succesfully"}