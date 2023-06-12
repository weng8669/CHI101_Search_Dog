import os
import json
import numpy as np
import requests

# from PIL import Image, ImageOps
from flask import Flask, request, abort
import subprocess
import shutil
from my_select import get_device_id


from linebot import (LineBotApi, WebhookHandler)
from linebot.exceptions import (InvalidSignatureError)
from linebot.models import (MessageEvent, TextMessage, TextSendMessage, ImageMessage, ImageSendMessage, TemplateSendMessage, ButtonsTemplate, URITemplateAction, CarouselTemplate, CarouselColumn, URIAction, FlexSendMessage, CameraAction, CameraRollAction, QuickReply,
    QuickReplyButton, PostbackAction, PostbackTemplateAction, PostbackEvent)
from linebot.exceptions import LineBotApiError


#我把資料都寫在env.json裡 記得進去裡面修改成自己要套用的Linebot API
with open('env.json') as f:
    env = json.load(f)
    
line_bot_api = LineBotApi(env['YOUR_CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(env['YOUR_CHANNEL_SECRET'])
#---------imgur-----------
client_id = env['YOUR_IMGUR_ID']
access_token = env['IMGUR_TOKEN']
headers = {'Authorization': f'Bearer {access_token}'}



app = Flask(__name__)


# 設定主選單的範本訊息
main_menu_template = TemplateSendMessage(
    alt_text='主選單',
    template=ButtonsTemplate(
        text='請選擇功能',
        actions=[
            PostbackTemplateAction(
                label='分享好友',
                data='share_friend'
            )
        ]
    )
)




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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    except Exception as e:
        print("Error occurred while handling webhook: ", e)
        abort(500)

    return 'OK'


#根據訊息內容  做處理
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    
    if event.message.text == '所有狗狗介紹':
        with open('all_dogs_0525.json',encoding='utf-8') as d:     ##### all_dogs_02.json###########
            test = json.load(d)
        line_bot_api.reply_message(
        event.reply_token,FlexSendMessage('有哪些狗',test)
        )        

    elif event.message.text == '關於中原動服社':
        with open('about_01.json',encoding='utf-8') as d:       ##### about_01.json##################
            test = json.load(d)
        line_bot_api.reply_message(
        event.reply_token,FlexSendMessage('中原動服社',test)
        )  
    elif event.message.text == '小黑在哪裡':
        
        dog_name = "小黑"
        a = list(get_device_id(dog_name))
        # print(a)
        
        if a[0] == 'nano':
            imglink = "https://imgur.com/l5f9HCm.jpg"
        elif a[0] == 'esp':
            imglink = "https://www.poaipets.com.tw/wp-content/uploads/2021/03/%E5%89%96%E6%9E%90%E7%8B%97%E7%8B%97%E5%B8%B8%E8%A6%8B%E7%96%BE%E7%97%85.jpg"



        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="最後出現時間：" + a[1]),
            image_message
        ]
        )
    elif event.message.text == '小熊在哪裡':
        
        dog_name = "小熊"
        a = list(get_device_id(dog_name))
        # print(a)
        
        
        if a[0] == 'nano':
            imglink = "https://imgur.com/l5f9HCm.jpg"
        elif a[0] == 'esp':
            imglink = "https://www.poaipets.com.tw/wp-content/uploads/2021/03/%E5%89%96%E6%9E%90%E7%8B%97%E7%8B%97%E5%B8%B8%E8%A6%8B%E7%96%BE%E7%97%85.jpg"
        
        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="最後出現時間：" + a[1]),
            image_message
        ]
        )
    elif event.message.text == '小斑在哪裡':
        
        dog_name = "小斑"
        a = list(get_device_id(dog_name))
        # print(a)
        
        
        if a[0] == 'nano':
            imglink = "https://imgur.com/l5f9HCm.jpg"
        elif a[0] == 'esp':
            imglink = "https://www.poaipets.com.tw/wp-content/uploads/2021/03/%E5%89%96%E6%9E%90%E7%8B%97%E7%8B%97%E5%B8%B8%E8%A6%8B%E7%96%BE%E7%97%85.jpg"
        
        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="最後出現時間：" + a[1]),
            image_message
        ]
        )
    
    elif event.message.text == 'Q比在哪裡':
        
        dog_name = "Q比"
        a = list(get_device_id(dog_name))
        # print(a)
        
        
        if a[0] == 'nano':
            imglink = "https://imgur.com/l5f9HCm.jpg"
        elif a[0] == 'esp':
            imglink = "https://www.poaipets.com.tw/wp-content/uploads/2021/03/%E5%89%96%E6%9E%90%E7%8B%97%E7%8B%97%E5%B8%B8%E8%A6%8B%E7%96%BE%E7%97%85.jpg"
        
        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="最後出現時間：" + a[1]),
            image_message
        ]
        )
    
    elif event.message.text == '莎白在哪裡':
        
        dog_name = "莎白"
        a = list(get_device_id(dog_name))
        # print(a)
        
        
        if a[0] == 'nano':
            imglink = "https://imgur.com/l5f9HCm.jpg"
        elif a[0] == 'esp':
            imglink = "https://www.poaipets.com.tw/wp-content/uploads/2021/03/%E5%89%96%E6%9E%90%E7%8B%97%E7%8B%97%E5%B8%B8%E8%A6%8B%E7%96%BE%E7%97%85.jpg"
        
        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="最後出現時間：" + a[1]),
            image_message
        ]
        )
    
    elif event.message.text == '土豆在哪裡':
        
        dog_name = "土豆"
        a = list(get_device_id(dog_name))
        # print(a)
        
        
        if a[0] == 'nano':
            imglink = "https://imgur.com/l5f9HCm.jpg"
        elif a[0] == 'esp':
            imglink = "https://www.poaipets.com.tw/wp-content/uploads/2021/03/%E5%89%96%E6%9E%90%E7%8B%97%E7%8B%97%E5%B8%B8%E8%A6%8B%E7%96%BE%E7%97%85.jpg"
        
        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="最後出現時間：" + a[1]),
            image_message
        ]
        )
    
    elif event.message.text == '樂樂在哪裡':
        
        dog_name = "樂樂"
        a = list(get_device_id(dog_name))
        # print(a)
        
        
        if a[0] == 'nano':
            imglink = "https://imgur.com/l5f9HCm.jpg"
        elif a[0] == 'esp':
            imglink = "https://www.poaipets.com.tw/wp-content/uploads/2021/03/%E5%89%96%E6%9E%90%E7%8B%97%E7%8B%97%E5%B8%B8%E8%A6%8B%E7%96%BE%E7%97%85.jpg"
        
        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            TextSendMessage(text="最後出現時間：" + a[1]),
            image_message
        ]
        )
                
    elif event.message.text == '小黑小檔案':                ## 小檔案照片link ####
        imglink = "https://imgur.com/lShVKyv.png"

        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            image_message
        ]
        )
    
    elif event.message.text == '小熊小檔案':
        imglink = "https://imgur.com/JUjt24L.png"

        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            image_message
        ]
        )

    elif event.message.text == '小斑小檔案':
        imglink = "https://imgur.com/G8XABG7.png"

        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            image_message
        ]
        )
    
    elif event.message.text == 'Q比小檔案':
        imglink = "https://imgur.com/NCxi8rZ.png"

        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)        
        line_bot_api.reply_message(
        event.reply_token,
        [
            image_message
        ]
        )


    elif event.message.text == '莎白小檔案':
        imglink = "https://imgur.com/nm2s6bk.png"

        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            image_message
        ]
        )

    elif event.message.text == '土豆小檔案':
        imglink = "https://imgur.com/3tzMLTC.png"

        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            image_message
        ]
        )

    elif event.message.text == '樂樂小檔案':
        imglink = "https://imgur.com/sNq30ep.png"

        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        line_bot_api.reply_message(
        event.reply_token,
        [
            image_message
        ]
        )

    elif event.message.text == '開發團隊':                
        imglink = "https://imgur.com/dm8S1PD.jpg"    

        image_message = ImageSendMessage(original_content_url=imglink, preview_image_url=imglink)
        
        line_bot_api.reply_message(
        event.reply_token,
        [
            image_message,
            TextSendMessage(text='E-mail：mingahsu@gmail.com')
        ]
        )


    elif event.message.text == '這隻狗叫什麼名字':    
        message=TextSendMessage(
            text="操作說明：\
                                                請從下面按鈕選擇開啟相機拍照或從相簿選取照片，傳送至系統進行辨識",
            quick_reply=QuickReply(
                items=[                    
                    QuickReplyButton(
                        action=CameraAction(label="拍照")
                        ),
                    QuickReplyButton(
                        action=CameraRollAction(label="相簿")
                        )
                        
                ]
            )
        )
        try:
            line_bot_api.reply_message(event.reply_token, message)
        except LineBotApiError as e:
            print('發生 LineBotApiError: ', e)

    # elif event.message.text == '好友分享':
    #     line_bot_id = '@186vrmwz'                              # 我的 Line Bot ID
    #     line_bot_link = f'line://nv/recommendOA/{line_bot_id}'

    #     line_bot_api.reply_message(
    #         event.reply_token,
    #         TextSendMessage(text=f'分享[中原搜狗]給好友：\n{line_bot_link}')
    #     )

    elif event.message.text == '主選單':
        line_bot_api.reply_message(event.reply_token, main_menu_template)


@handler.add(PostbackEvent)
def handle_postback(event):
    if event.postback.data == 'share_friend':
        line_bot_id = '@186vrmwz'  # 您的 LINE Bot ID
        line_bot_link = f'line://nv/recommendOA/{line_bot_id}'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'請點擊下方連結分享給好友：\n{line_bot_link}')
        )


#大概運作流程=>
#-> 當bot接收到圖片
#-> 保存圖檔temp.jpg 
#-> 將圖片帶入執行detect.py 並產出標出名稱的圖檔 和txt檔(我加在detect裡) 然後放在LineExport資料夾裡
#-> 刪除temp.jpg 並把產出有標框線的圖上傳至imgur
#-> 讀取txt檔的結果 回傳給使用者
#-> 把LineExport資料夾刪除

#-----當使用者傳圖片時-----
@handler.add(MessageEvent, message=ImageMessage)
def handle_image_message(event):
    message_content = line_bot_api.get_message_content(event.message.id)
    with open('temp.jpg', 'wb') as f:
        for chunk in message_content.iter_content():
            f.write(chunk)
            
    user_id = event.source.user_id

    line_bot_api.push_message(user_id, TextSendMessage(text='辨識進行中...請稍後'))
    if os.path.exists('LineExport'):
        shutil.rmtree('LineExport')
    # 帶入參數 執行 detect    
    result = subprocess.run(['python', 'detect.py', '--weights', 'yolov7.pt', '--conf-thres', '0.5', '--img-size', '416', '--source', 'temp.jpg', '--project', './', '--name', 'LineExport'],text=True)
    #os.remove('temp.jpg')

    print("==========================")
    print(result)#自己看爽用
    print("==========================")
    
    #狗勾標籤對應中文名稱
    Dog_CH = {
        'Black':'小黑',
        'Bear':'小熊',
        'Ben':'小斑',
        'Qbi':'Q比',
        'Sabai':'莎白',
        'Tudo':'土豆',
        'Lele':'樂樂'
    }
    

    imgur_link = upload_image_to_imgur('./LineExport/temp.jpg')
    
    #讀取標籤內容    
    with open("./LineExport/result.txt", "r") as f:
        content = f.read()
         
        if content:  # 有檢測結果
            Dogresult = (content.split(' '))[1].strip(',')
            dog_name = Dog_CH.get(Dogresult, "查無此狗")
                
            # 回傳圖片和結果給使用者
            if imgur_link:
                image_message = ImageSendMessage(original_content_url=imgur_link, preview_image_url=imgur_link)
                line_bot_api.reply_message(
                event.reply_token,
                [
                    TextSendMessage(text=f'偵測完畢　他是{dog_name}:D'),
                    image_message
                ]
            )
            else:
                line_bot_api.reply_message(event.reply_token, TextSendMessage(text='上傳圖片到 Imgur 失敗'))
                    

            
                #刪除殘留檔 可刪可不刪
                #os.remove('result.txt')
                #shutil.rmtree('LineExport')
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text='沒有偵測到狗狗，請重新上傳正確圖片'))
            
    # shutil.rmtree('LineExport')



# 傳圖片上imgur
def upload_image_to_imgur(image_path):
    url = 'https://api.imgur.com/3/upload'
    with open(image_path, 'rb') as f:
        response = requests.post(url, headers=headers, files={'image': f})
        if response.status_code == 200:
            return response.json().get('data').get('link')
        else:
            return None
#--------------------------------------------------------------------------------------

# @handler.add(MessageEvent, message=TextMessage)
# def handle_message(event):
#     if event.message.text == '好友分享':
#         line_bot_id = '@186vrmwz'  # 替換為您的 Line Bot ID
#         line_bot_link = f'line://nv/recommendOA/{line_bot_id}'
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text=f'請分享以下連結給您的好友：\n{line_bot_link}')
#         )






if __name__ == "__main__":
    app.run()
