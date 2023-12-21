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
    #定义要发送的数据
    data = {
        "msgtype": "markdown", # 定义数据格式为markdown，还有其他格式，具体参考钉钉开放文档
        "markdown": {
            "title": "你好308",
            "text": "好好好～～～牛魔zc洗澡!————hby"+"剩余电费"+fetch_electricity_fee(api_url)+"\n"
        },
        "at": {
            "atMobiles": [
                "18868576061", 
                "",  # 这里的手机号和上面的保持一致
            ],
            "isAtAll": True # @全体成员
        }
    }
    #发送post请求
    requests.post(webhook, data=json.dumps(data), headers=headers)