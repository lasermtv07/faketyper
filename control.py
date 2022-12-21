import sys
import os.path
import typer
import time
history=[]
def help(sw,args):
    if "s" in sw:
        print('''
        HELP - SHORT
        ============
        run [/k] [/d] [/b] [/w] <speed> <errors> <string> <error characters*>
        help [/s]
        version [/c]
        
        *if you want to use the default settings, set to ' '. ''')
    else:
        print('''
        ========
        = HELP =
        ========
        <major 0.2>
        Note: The program is still in beta and therefore is NOT meant to represent the full product.
        Please, all bugs report on GitHub. And yes, the code is awful.
            -laser :)
        SYNTAX:
        [] - switches
        <> - argument. All arguments are MANDATORY! *If you want to choose default settings, you have to use ' ',
             even though it works only with run <error characters>.
        COMMANDS:
        run: run [/k] [/d] [/b] [/w] <speed> <errors> <string> <error characters*> - starts the typing
            -/k hides the onscreen keyboard
            -/d disables the use of capital letters. Legacy function.
            -/b writes out the typed string after typing finishes
            -/w disables 3sec wait before typing starts
            <speed> typing speed, in characters per seconds
            <errors> probability of error appearing in the text, 0-100, 100 for no errors
            <string> the text that will be typed out
            <error characters>* list of charcters that error characters will be repalced with. If u want all letters, write ' '
        help: help [/s] - displays this help
            -/s show shorter version of this help
        version: version [/c] - prints the current version of the program
            -/c prints more detailed version of version changelog
        ''')
def version(sw,args):
    if "c" in sw:
        print(''' 
       =========
       =VERSION=
       =========
       Version: BETA 0.2 - MAJOR RELEASE
       Codename: less 'if' update
       Release date: 16/12/22 (DD/MM/YY)
       
       CHANGELOG:
       MAJOR:
            -CLI system updated
            -Command switches added
            -Removed support for voluntary arguments and aliases
       MINOR:
            - changed the run command
                -added switches /k /s /d /w
                -removed the alias r
            - changed the help command
                -added the /s switch
            -changed the version command
                -added the /c switch
            -removed changelog command''')
    else:
        print('''Version: beta 0.2
Still under development. Use version /c for more info
or help for help''')
def run(sw,args):
    vol=' '
    onscreen_kb=1
    use_cap=1
    write_out=0
    if "k" in sw:
        onscreen_kb=0
    if "d" in sw:
        use_cap=0
    if "b" in sw and "k" in sw:
        write_out=1
    if args[0].isnumeric()!=True:
        print("Error:run command:wrong input type (speed)")
    if args[1].isnumeric()!=True and int(args[1])<101:
        print("Error:run command:wrong input type (errors)")
    if "w" not in sw:
        print("wait 3 seconds")
        time.sleep(3)
    try: vol=args[3]
    except: vol=' '
    try: typer.typer(args[2],int(args[0]),int(args[1]),vol,onscreen_kb,use_cap,write_out)
    except: print("Error:run command:unknown error")

class Command:
    def __init__(self, cmd, alias, args,vol, execute):
        self.cmd=cmd
        self.alias=alias
        self.args=args
        self.execute=execute
        self.vol=vol
    def update(self):
        if len(sys.argv)>1 and (self.cmd==sys.argv[1] or self.alias==sys.argv[1]):
            receiveargs=[]
            out_sw=[]
            for x in range(2,len(sys.argv)):
                receiveargs.append(sys.argv[x])
            for y in receiveargs:
                if y[0]=="/" or y[0]=="-":
                    out_sw.append(y)
            for r in out_sw:
                while r in receiveargs:
                    receiveargs.remove(r)
            for u in range(len(out_sw)):
                if "/" in out_sw[u] or "-" in out_sw[u]:
                    out_sw[u]=out_sw[u][1]
            #print(str(len(receiveargs)) + str(receiveargs))
            if len(receiveargs)==self.args or len(receiveargs)>self.args:
                exec(self.execute)
            else: print("Error:Incorrect number of arguments")

if len(sys.argv)==1:
    version([],0)

#hi=Command("hi", ["/a"], 3,1,'print("hi" + str(out_sw) + str(receiveargs))')
#hi.update()
r=Command("run", "r", 3,1,'run(out_sw,receiveargs)')
r.update()
v=Command("help", "h", 0,0,'help(out_sw,0)')
v.update()
x=Command("version", "v", 0,0,'version(out_sw,0)')
x.update()

