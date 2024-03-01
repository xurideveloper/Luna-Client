import Interface
from Packages.Secure import Handler

# Luna @ Command Module

def Execute(Command):
    if Command.startswith('Setkey'):
        Arg = str(Command.split()[1])
        Handler.Setkey(Arg)

    if Command.startswith('Lock'):
        Arg = str(Command.split()[1])

        with open(f'Luna/Files/{Arg}', 'rb') as f:
            Data = f.read()
            Handler.Lock(Arg, Data)
            
    if Command.startswith('Unlock'):
        Arg = str(Command.split()[1])

        with open(f'Luna/Files/{Arg}', 'rb') as f:
            Data = f.read()
            Handler.Unlock(Arg, Data)

    if Command.startswith('Download'):
        Arg = str(Command.split()[1])
        Handler.Download(Arg)

def Handle():
    while True:
        Command = Interface.Input('Command - ')
        Execute(Command)