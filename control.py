import sys
import os.path
import typer
import time
import random
history=[]
kb_en=[['`','1','2','3','4','5','6','7','8','9','0','-','='],
    ['q','w','e','r','t','y','u','i','o','p','[',']','\ '],
    ['a','s','d','f','g','h','j','k','l',';','"','ENTER'],
    ['z','x','c','v','b','n','m',',','.','/',' SHIFT']
    ]
kb_cs=[[';','+','ě','š','č','ř','ž','ý','á','í','é','=','´'],
    ['q','w','e','r','t','z','u','i','o','p','ú',')','¨ '],
    ['a','s','d','f','g','h','j','k','l',';','"','ENTER'],
    ['z','x','c','v','b','n','m',',','.','/',' SHIFT']
    ]
kb_ru=[['§','1','2','3','4','5','6','7','8','9','0','-','='],
    ['й','ц','у','к','е','н','г','ш','щ','з','х','ъ','\ '],
    ['ф','ы','в','а','п','р','о','л','д','ж','э','ENTER'],
    ['я','ч','с','м','и','т','ь','б','ю','.',' SHIFT']
    ]
kb_su=[['ё','1','2','3','4','5','6','7','8','9','0','+','´'],
    ['q','w','e','r','t','y','u','i','o','p','å','¨','/ '],
    ['a','s','d','f','g','h','j','k','l','ö','ä','ENTER'],
    ['z','x','c','v','b','n','m',',','.','-',' SHIFT']
    ]


def tips(sw):
    tip=["use -s when typing the help command for shortened version"
        ,"when you always forget syntax of a command, just display shortened help",
        "hello. Have (imaginary) 0.05USD for using my program",
        "this command has esentially has no point rn, its for the future",
        "use v -c to show the changelog",
        "now on linux",
        "the syntax of the run command is: run [/k] [/d] [/b] [/w] <speed> <errors> <string> <error characters*>"]
    if not "a" in sw: print("The tip of today is: " + str(tip[random.randint(0,len(tip)-1)]))
    else:
        print("List of all tips:")
        print(*tip, sep="\n  -")
def help(sw,args):
    if "s" in sw:
        print('''
HELP - SHORT
============
run @r [/k] [/d] [/b] [/w] {/c} {/f} {/r} <speed> <errors> <string> |error characters|
help [/s]
version [/c]
tip [/a]
*u can use either the windows style or the linux style switch writing''')
    else:
        print('''
        ========
        = HELP =
        ========
        <major 0.4>
        Report all bugs you find via github issues and I'll love you <3
        SYNTAX:
        [] - switches, can be typed either using the Windows /x
             or the Linux -x format. They are always ONE LETTER!
        { } - language switches. Set keyboard layout (run). Syntax
              same as switches
        <> - Mandatory arguments
        | | - optional arguments
        @ - Alternative name (first letter of the command)
        COMMANDS:
        run: run @r [/k] [/d] [/b] [/w] {/c} {/f} {/r} <speed> <errors> <string> |error characters| - starts the typing
            -[/k] hides the onscreen keyboard
            -[/d] disables the use of capital letters. Legacy function, /doesnt work anymore change of library/
            -[/b] writes out the typed string after typing finishes
            -[/w] disables 3sec wait before typing starts
            -[/t] makes the program read input string from a .txt file
                  instead of the string typed into command
            -[/s] disables the use of keyboard aliases; List here:
                    - "■" or "¦".. Backspace 
            -{/c} sets the keyboard layout to Czech
            -{/f} sets the keyboard layout to Finnish
            -{/r} sets the keyboard layout to Russian
            <speed> typing speed, in characters per seconds
            <errors> probability of error appearing in the text, 0-100, 100 for no errors
            <string> the text that will be typed out
            |error characters| list of characters to be replaced by - optional
        help: help @h [/s] - displays this help
            -[/s] show shorter version of this help
        version: version @v [/c]
            -[/c] prints more detailed version of version changelog
        tip: tip @t [/a] - displays a random tip
            -[/a] prints the list of all tips existing
        ''')
def version(sw,args):
    if "c" in sw:
        print(''' 
       =========
       =VERSION=
       =========
       Version: BETA 0.4 - MAJOR RELEASE
       Codename: You'll love it!
       Release date: 28/12/22 (DD/MM/YY)
       
       CHANGELOG:
       MAJOR:
            -Ability to import .txt files (using the /t switch)
            -Ability to use multiple keyboard layouts with the /c /f /r switches
                -Added Czech layout to the keyboard visualiser
                -Added Finnish keyboard the keyboard visualizer
                -Added Russian keyboard to the keyboard visualiser
                (leave empty if you want to keep the english keyboard)
            -Error generator algorithmus updated; if you want to know how, open
             either help or source code and look
            -Added keyboard aliases; "■" or "¦" now symbolize backspace
                -Can be disabled with the /s switch
        MINOR:
            -Writing out text when typing out the text
             now works as intended
            -Added the /a switch to tip command; via help
            -Edited and improved the help
            -Unspecified bugfixes''')
    else:
        print('''Version: beta 0.4
Still under development. Use version /c for more info
or help for help''')
        tips("")
def run(sw,args):
    disable_bp=True
    kb=[['`','1','2','3','4','5','6','7','8','9','0','-','='],
    ['q','w','e','r','t','y','u','i','o','p','[',']','\ '],
    ['a','s','d','f','g','h','j','k','l',';','"','ENTER'],
    ['z','x','c','v','b','n','m',',','.','/',' SHIFT']
    ]
    wr=args[2]
    if "t" in sw:
        try:
            f=open(args[2],'r')
            wr=f.read()
            f.close()
        except:
            print("Error: error loading the file")
            exit()
    if "c" in sw:
        kb=kb_cs
    elif "f" in sw:
        kb=kb_su
    elif "r" in sw:
        kb=kb_ru
    vol=' '
    onscreen_kb=1
    use_cap=1
    write_out=0
    if "s" in sw:
        disable_bp=False
    if "k" in sw:
        onscreen_kb=0
    if "d" in sw:
        use_cap=0
    if "b" in sw:
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
    try: typer.typer(wr,int(args[0]),int(args[1]),vol,onscreen_kb,use_cap,write_out,kb,disable_bp)
    except: print("Error:run command:unknown error")
class Command:
    def __init__(self, cmd, alias, args,vol, execute, syntax):
        self.cmd=cmd
        self.alias=alias
        self.args=args
        self.execute=execute
        self.vol=vol
        self.syntax=syntax
    def update(self):
        if len(sys.argv)>1 and (self.cmd==sys.argv[1] or self.alias==sys.argv[1]):
            receiveargs=[]
            out_sw=[]
            #for x in range(2,len(sys.argv)):
            #    receiveargs.append(sys.argv[x])
            receiveargs=sys.argv[2:]
            for y in receiveargs:
                if y[0]=="/" or y[0]=="-":
                    out_sw.append(y)
                    while y in receiveargs:
                        receiveargs.remove(y)
            for u in range(len(out_sw)):
                if "/" in out_sw[u] or "-" in out_sw[u]:
                    out_sw[u]=out_sw[u][1]
            #print(str(len(receiveargs)) + str(receiveargs))
            if len(receiveargs)==self.args or len(receiveargs)>self.args:
                exec(self.execute)
                history.append(self.cmd)
                #print(history)
            else: print("Error: Wrong arguments: " + self.syntax)

if len(sys.argv)==1:
    version([],0)

#hi=Command("hi", ["/a"], 3,1,'print("hi" + str(out_sw) + str(receiveargs))')
#hi.update()
r=Command("run", "r", 3,1,'run(out_sw,receiveargs)',"run @r [/k] [/d] [/b] [/w] {/c} {/f} {/r} <speed> <errors> <string> |error characters|")
r.update()
v=Command("help", "h", 0,0,'help(out_sw,0)',"help [/s]")
v.update()
x=Command("version", "v", 0,0,'version(out_sw,0)',"version [/c]")
x.update()
z=Command("tip", "t", 0,0,'tips(out_sw)',"tip")
z.update()

