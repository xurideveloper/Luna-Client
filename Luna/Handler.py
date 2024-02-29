import Interface
from Packages.Secure import Handler

# Luna @ Command Module

def Execute(Command):
     if Command.startswith('Setkey'):
         Arg = str(Command.split()[1])
         Handler.Setkey(Arg)

     if Command.startswith('Download'):
        Arg = str(Command.split()[1])
        Handler.Download(Arg)

     if Command.startswith('Encrypt'):
        Arg = str(Command.split()[1])
        Handler.Encrypt(Arg)

     if Command.startswith('Decrypt'):
        Arg = str(Command.split()[1])
        Handler.Decrypt(Arg)

def Handle():
    while True:
        Command = Interface.Input('Command - ')
        Execute(Command)