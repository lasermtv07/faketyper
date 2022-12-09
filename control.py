import sys
import os.path
#import typer
import time

class Command:
    def __init__(self, cmd, switch, args, execute):
        self.cmd=cmd
        self.switch=switch
        self.args=args
        self.execute=execute

    def update(self):
        if len(sys.argv)>1 and self.cmd==sys.argv[1]:
            receiveargs=[]
            out_sw=[]
            out_args=[]
            for x in range(2,len(sys.argv)):
                receiveargs.append(sys.argv[x])
            for y in receiveargs:
                if y in self.switch and y[0]=="/" and y not in out_sw:
                    out_sw.append(y)
                elif y[0]=="/" and y not in out_sw and y[1] in self.switch:
                    print("Error:Wrong switches used")
                    exit()
            for r in out_sw:
                while r in receiveargs:
                    receiveargs.remove(r)
            #input naming standard:
            #i - integer
            #s - string
            #f - float
            exec(self.execute)


hi=Command("hi", ["/a"], ['s','i'],'print("hi" + str(out_sw) + str(out_args) + str(receiveargs))')
hi.update()

