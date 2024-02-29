import Interface
from Secure import Handler
# Luna @ Command Module

def Execute(Command):
     if Command.startswith('setkey'):
         Arg = str(Command.split()[1])
         Handler.Setkey(Arg)

def Handle():
    while True:
        Command = Interface.Input('Command - ')
        Execute(Command)