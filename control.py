import sys
import os.path
import typer
import time
def run(sw,args):
    onscreen_kb=1
    use_cap=1
    write_out=0
    if "/k" in sw:
        onscreen_kb=0
    if "/d" in sw:
        use_cap=0
    if "/b" in sw and "/k" in sw:
        write_out=1
    if args[0].isnumeric()!=True:
        print("Error:run command:wrong input type (speed)")
    if args[1].isnumeric()!=True and int(args[1])<101:
        print("Error:run command:wrong input type (errors)")
    if "/w" in sw:
        print("wait 3 seconds")
        time.sleep(3)
    try: typer.typer(args[2],int(args[0]),int(args[1]),args[3],onscreen_kb,use_cap,write_out)
    except: print("Error:run command:unknown error")


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
            for x in range(2,len(sys.argv)):
                receiveargs.append(sys.argv[x])
            for y in receiveargs:
                if y in self.switch and y[0]=="/" and y not in out_sw:
                    out_sw.append(y)
                elif y[0]=="/" and y not in out_sw and y[1] in self.switch:
                    print("Error:Wrong switches useds")
                    exit()
            for r in out_sw:
                while r in receiveargs:
                    receiveargs.remove(r)
            #print(str(len(receiveargs)) + str(receiveargs))
            if len(receiveargs)==self.args:
                exec(self.execute)
            else: print("Error:Incorrect number of argument")


hi=Command("hi", ["/a"], 3,'print("hi" + str(out_sw) + str(receiveargs))')
hi.update()
r=Command("run", ["/k","/d","/w","/b"], 4,'run(out_sw,receiveargs)')
r.update()

