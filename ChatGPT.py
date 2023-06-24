import poe
import logging
import sys
import json
import time
import websocket
#send a message and immediat
ws=websocket.create_connection("wss://websocket.lumina.chat:11451/")
ws.send(json.dumps({"cmd":"join","channel":"main","nick":"LuminaBot"}))
token = ''
client = poe.Client(token)

def chatwith(botname,message):
    for i in range(5):
        try:
            for chunk in client.send_message(botname, message):
                pass
            return chunk["text"]
        except:
            print(f"Retrying {i+1}/5")
            return "请求失败"
def gethistory(botname,length=10):
    histories=client.get_message_history(botname,length)
    real=[]
    for i in histories:
        real.append((i["node"]["author"],i["node"]["text"]))
    return 
def clearhistory(botname):
    client.purge_conversation(botname)
while 1:
    data=json.loads(ws.recv())
    if data['cmd']=='chat':
        if data['text'].startswith('@LuninaBot '):
            text=data['text'][11:]
            time.sleep(5)
            ws.send(json.dumps({
                    "cmd":"chat",
                    "text":chatwith('LuminaChat',text)
                }))
            
# print(chatwith('LuminaChat','a'))