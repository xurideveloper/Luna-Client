import requests
import os
from cryptography.fernet import Fernet
import Interface

# Luna @ Secure Module

Client = 'Secure'
Path = 'Luna/Files/'

def Setkey(Key):
    with open('Luna/Packages/Secure/Session', 'w') as Data:
        Data.write(Key)
        Interface.Send('Success', f'Key set', Client)

def Download(Url):
    Response = requests.get(Url)

    if ("content-disposition" in Response.headers):
        content_disposition = Response.headers["content-disposition"]
        Filename = content_disposition.split("filename=")[1]
    else:
        Filename = Url.split("/")[-1]

    Interface.Send('Success', 'Starting download')
    
    with open(f'{Path}{Filename}', mode="wb") as file:
        file.write(Response.content)
        Interface.Send('Success', f'Downloaded {Filename}')