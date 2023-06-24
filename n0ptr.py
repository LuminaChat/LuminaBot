import poe
import logging
import sys
import json
import websocket
import time
#send a message and immediately delete it
ws=websocket.create_connection("wss://websocket.lumina.chat:11451/")
ws.send(json.dumps({"cmd":"join","channel":"main","nick":"n0ptr"}))
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
    return real
while 1:
    data=json.loads(ws.recv())
    if data['cmd']=='chat':
        if data['nick']!='n0ptr':
            text=chatwith('BotO15AYGQD64',data['nick']+': '+data['text'])
            if '我不想回复。' in text:
                continue
            _text=text.split(';')
            for i in _text:
                time.sleep(len(i)*0.5)
                ws.send(json.dumps({"cmd":"chat","text":i.replace('n0pTr: ','')}))