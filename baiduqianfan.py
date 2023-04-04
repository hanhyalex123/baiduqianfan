from apikey import *
import requests as req
import json
#API url
APIDOMAIN="https://api-eccloud.saicmotortest.com"
APIURL='/chat/completions'

#API header
Headers={'saicid':SAICID,'apikey':APIKEY}

#API测试,消息体使用json格式,data=json.
# res=req.post(APIDOMAIN+APIURL,headers=Headers,data=json.dumps({ "messages": [{ "role": "user", "content": "你好，请问你是？" }] }))
# print(res.text)

class BaiduQianFan:
    def __init__(self):
        self.message=[]

    def chat(self,input_message):
        self.message.append({"role": "user", "content": input_message})
        completion=req.post(APIDOMAIN+APIURL,headers=Headers,data=json.dumps({ "messages": self.message }))
        completion=json.loads(completion.content)
        self.message.append({"role": "assistant","content": completion["result"]})
        
        return "AI: " + str(completion["result"])

#将对话请求做成循环，使用BaiduQianFan类进行对话，补全代码
baiduQianFan=BaiduQianFan()
while True:
    input_message = input("用户: ")
    if input_message == "exit":
        print("聊天记录"+str(baiduQianFan.message))
        break
    print(baiduQianFan.chat(input_message))

#git remote add origin git@github.com:hanhyalex123/baiduqianfan.git 然后 git push -u origin master 报错Please make sure you have the correct access rights and the repository exists.应该怎么解决

#say hello




