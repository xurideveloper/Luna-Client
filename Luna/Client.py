import os
import Interface
import Handler

def Init():
    Packages = ['Packages', 'Files']
    Ready = True

    for Package in Packages:
        if os.path.exists(os.path.join('Luna/', Package)):
            Interface.Send('Success', f'Loaded [{Package}]')
        else:
            Interface.Send('Issue', f'Failed [{Package}] :(')
            Ready = False

    if Ready:
        Handler.Handle()
Init()