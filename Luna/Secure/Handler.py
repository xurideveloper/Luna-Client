import json
import Interface

# Luna @ Secure Module

Client = 'Secure'

def Setkey(Key):
    with open('Secure/data.json') as f:
        Data = json.load(f)
        Data['Key'] = Key
        #Data.update(Key)

    Interface.Send('Success', f'Set key', Client)