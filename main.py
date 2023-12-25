#导入依赖库
import json
import sys
import requests
import time
import hashlib
import base64
import urllib
import hmac
import os
import datetime
from bs4 import BeautifulSoup

def encrypt(secret):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))
    return timestamp,sign

def fetch_electricity_fee(api_url):
    # 发送请求获取HTML内容
    response = requests.get(api_url)
    if response.status_code == 200:
        # 使用BeautifulSoup解析HTML
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 找到包含电费信息的元素
        price_element = soup.find('span', class_='price')
        if price_element:
            price_text = price_element.text.strip()
            price_text = price_text.replace("元", "")
            # 提取电费信息并返回
            return price_text
        else:
            return "null"
    else:
        return "error"

if __name__=='__main__':
    #定义数据类型
    headers={
            "Content-Type": "application/json",
            "Charset": "UTF-8"
    }
    secret = os.getenv('SECRET')
    access_token = os.getenv('TOKEN')
    timestamp,sign=encrypt(secret)
    #定义webhook，从钉钉群机器人设置页面复制获得
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token='+access_token+'&timestamp='+timestamp+'&sign='+sign
    # API URL
    api_url = os.getenv('URL')
    text="好好好～～～牛魔*zc*洗澡!————hby\n"+"**剩余电费**"+fetch_electricity_fee(api_url)+"\n"
    data = {
        "msgtype": "markdown", 
        "markdown": {
            "title": "牛魔们好哇",
            "text": text
        },
        "at": {
            "isAtAll": True # @全体成员
        }
    }
    requests.post(webhook, data=json.dumps(data), headers=headers)
    current_date = datetime.date.today()
    if current_date.weekday()==6:
        text2="牛魔hby提醒大家***记单词***啦～\n"+"牛魔zc提醒大家少撸管，多休息\n"
        data2 = {
            "msgtype": "markdown", 
            "markdown": {
                "title": "牛魔们好哇",
                "text": text2
            },
            "at": {
                "isAtAll": True # @全体成员
            }
        }
        requests.post(webhook, data2=json.dumps(data2), headers=headers)