import os
import json
import requests

from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def send():
    if request.method == 'POST':
        post_data = request.get_data()
        send_alert(bytes2json(post_data))
        return 'success'
    else:
        print (os.getenv('ROBOT_TOKEN'))
        return 'weclome to use prometheus alertmanager dingtalk webhook server!'


def bytes2json(data_bytes):
    data = data_bytes.decode('utf8').replace("'", '"')
    return json.loads(data)


def send_alert(data):
    prometheus_ip = os.getenv("prometheus_ip")
    if not prometheus_ip:
        prometheus_ip="192.168.1.29:33000"
    token = os.getenv('ROBOT_TOKEN')
    if not token:
        print('you must set ROBOT_TOKEN env')
        return
    url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % token
    try:
        for date in data["alerts"]:
            title = date["annotations"]["summary"]
            text = date["annotations"]["description"] + ",点击进入Prometheus查看"
            alterurl = date["generatorURL"]
            old_url = alterurl.split("//")[1].split("/")[0]
            new_url = str(alterurl).replace(old_url, prometheus_ip)
            dicta = {"msgtype": "link", "link": {}}
            dicta["link"]["text"] = text
            dicta["link"]["title"] = title
            dicta["link"]["picUrl"] = ""
            dicta["link"]["messageUrl"] = new_url
            req = requests.post(url, json=dicta)
            result = req.json()
            if result['errcode'] != 0:
                print('notify dingtalk error: %s' % result['errcode'])
    except:
        print ("数据格式有误")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
