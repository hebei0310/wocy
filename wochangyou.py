import requests
import json
import time

interval = 20 * 60 # 20分钟，单位为秒

def send_post():
    url = 'https://game.wostore.cn/api/app/user/v2/qos/start'
    headers = {
        'Authorization': 'eyJhbGciOiJIUzUxMiJ9.eyJ1c2VyX2lkIjo4Mjc2MDk2NjM3MTM4MDAxOTIsInVzZXJfa2V5IjoiZmFhZGUxMmEtZTc3NC00N2UyLWI5ZTQtYWYyNGE4ZDQ5ZDU4IiwidXNlcm5hbWUiOiJ4KuaelyJ9.bzyNrAUh3oCe4T3kjK-tArkjAEWwasLxsTJNC8ISOAWWCo_rwC45c15mNlj40EMEObPIGiPRHaZQQcoU05RNhQ',
        'Content-Type': 'application/json'
    }
    data = {
        'channelId': '90002',
        'privateIp': '10.1.10.1'
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 发送成功，响应：{response.json()}")
    except Exception as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 发送失败，错误信息：{e}")

print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 脚本已启动，将每隔20分钟发送一次POST请求")

while True:
    send_post()
    time.sleep(interval)
