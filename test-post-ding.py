#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import requests
import os
import json

token = "0a884d39d2b040cbb4c0e8b403f482bdc108f4154ec0094e5523d2233f03f378"
token2 = "bWVChtY7keG6Q5qXkZqdqaVdmyZ8cZOkt9JHvn0NrTw"
url = 'https://oapi.dingtalk.com/robot/send?access_token=%s' % token
url2 = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token%s' % token2

# print os.path.basename("J:/Djangostyle/my-k8s-ansible/test-post-ding.py")
# with open("J:/Djangostyle/my-k8s-ansible/dingding.json", "r") as f:
#     # print type(f)
#     load_dict = json.load(f).encode("UTF8")

# for date in date["text"]["content"]["alerts"]:
#     title = date["annotations"]["summary"]
#     text = date["annotations"]["description"].encode("UTF8") + ",点击进入Prometheus查询"
#     alterurl = date["generatorURL"]
#     old_url = alterurl.split("//")[1].split("/")[0]
#     new_url = str(alterurl).replace(old_url, "192.168.1.30:33000")
#     dicta = {"msgtype": "link", "link": {}}
#     dicta["link"]["text"] = text
#     dicta["link"]["title"] = title
#     dicta["link"]["picUrl"] = ""
#     dicta["link"]["messageUrl"] = new_url
#     req = requests.post(url, json=dicta)

f = {
   "touser" : "@all",
   "msgtype" : "text",
   "agentid" : 1000002,
   "text" : {
       "content" : "你的快递已到，请携带工卡前往邮件中心领取。\n出发前可查看<a href=\"http://work.weixin.qq.com\">邮件中心视频实况</a>，聪明避开排队。"
   },
   "safe":0
}
requests.post(url=url2, json=f)
