import requests
import os
import Interface

import hashlib
import base64
from cryptography.fernet import Fernet

# Luna @ Secure Module

Client = 'Secure'

def Setkey(Key):
    with open('Luna/Packages/Secure/Session', 'wb') as File:
        Key = Key.encode()
        HashKey = hashlib.md5(Key).hexdigest()
        Key = base64.urlsafe_b64encode(HashKey.encode('utf-8'))

        File.write(Key)
        Interface.Send('Success', f'Key set', Client)

def GetKey():
    with open('Luna/Packages/Secure/Session', 'r') as Data:
        Key = Data.read()
        Interface.Send('Success', f'Got key,', Client)
    return Key
    
def Lock(File, Data):
    Key = Fernet(GetKey())
    Encrypted = Key.encrypt(Data)
    
    with open(f'Luna/Files/{File}', 'wb') as f:
        f.write(Encrypted)

    Interface.Send('Warn', f'Locked @{File}', Client)

def Unlock(File, Data):
    Key = Fernet(GetKey())
    Decrypted = Key.decrypt(Data)

    with open(f'Luna/Files/{File}', 'wb') as f:
        f.write(Decrypted)

    Interface.Send('Warn', f'Unlocked @{File}', Client)

def Download(Url):
    Response = requests.get(Url)

    if ("content-disposition" in Response.headers):
        content_disposition = Response.headers["content-disposition"]
        Filename = content_disposition.split("filename=")[1]
    else:
        Filename = Url.split("/")[-1]

    Interface.Send('Success', 'Starting download')
    
    with open(f'Luna/Files/{Filename}', mode="wb") as file:
        file.write(Response.content)
        Interface.Send('Success', f'Downloaded {Filename}')