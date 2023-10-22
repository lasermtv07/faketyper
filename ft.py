# faketyper, (C) 2022/23 lasermtv07
# this programs comes with ABSOLUTELY NO WARRANTY, including warranty implied by merchability
# released under the GNU General public licence, version 3.0 (via file attached to repository)
# this program is free as in freedom, feel free to modify and redistriute it
import sys
import os.path
import typer
import time
import random
history=[]
all_commands=["run","r","help","h","version","v","ti","t"]
def separ(string):
    return "¬".join(string.split())

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
        for r in tip:
            print("  -" + r)
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
        <major 1.1>
        Report all bugs you find via github issues and I'll love you <3
        SYNTAX:
        [] - switches, can be typed either using the Windows /x
             or the Linux -x format. They are always ONE LETTER!
        { } - language switches. Set keyboard layout (run). Syntax
              same as switches
        <> - Mandatory arguments
        | | - optional arguments
        @ - Alternative name (first letter of the command)
        COMMANDS*:
        run**: run @r [/k] [/d] [/b] [/w] [/l] [/e] {/c} {/f} {/r} <speed> <errors> <string> |error characters| - starts the typing
            -[/k] hides the onscreen keyboard
            -[/d] disables the use of capital letters. Legacy function, /doesnt work anymore - change of code structure/
            -[/b] writes out the typed string after typing finishes
            -[/w] disables 3sec wait before typing starts
            -[/t] makes the program read input string from a .txt file
                  instead of the string typed into command
            -[/s] disables the use of keyboard aliases; List here:
                    - "■" or "¦".. Backspace
                    - "^".. Space
                    - "¬"***.. Newline
            -[/l] writes the text in an endless loop
            -[/e] - Newlines with every space
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
            
        FOOTNOTES:
            -* - program can sometimes run slow, especially
                for the first time if the libraries arent loaded or if 
                you set too big speed. Disable keyboard projection, that might help
            -** - you can stop the run with the esc key
            -*** - presses space, cant have [/s] in command
        ---
        Released under the GNU General Public Licence
        ''')
def version(sw,args):
    if "c" in sw:
        print(''' 
       =========
       =VERSION=
       =========
       Version: 1.1.0 - MAJOR RELEASE
       Codename: Uhh.. full release i guess?
       Release date: 1/20/23 (DD/MM/YY)
       
       CHANGELOG:
       MAJOR:
            - keys on the visualiser now switch cases
            - you can now loop write in endless loop using the [/l] switch
            - you can now automatically newline after space is in the string using [/e]
            - you can stop the pragram with esc
            - added new aliases:
                - "^" for space
                - "¬" for newline
        MINOR:
            - if python exception is raised during the typer run, you get error message that
              contains a short description of the error (insted of just "Error: unknown error" or long description)
              ---
Released under the free GNU General Public Licence, version 3
Feel free to redistribute the program, including modification and sale,
under the condition that you'll keep it free for all other users.
For a program to be free it must follow these 4 specification, as specified by RMS:
    (0) Users have freedom to USE the program
    (1) Users have access to the SOURCE CODE
    (2) Users can REDISTRIBUTE the unmodified program
    (3) Users can REDISTRIBUTE modified program
More info on the GNU project website, www.gnu.org

Have fun :)''')
    else:
        print('''Version: full 1.1.0
Full release, please report bugs on Github. Use version /c for more info
or help for help
---
Released under the free GNU General Public Licence, version 3
Feel free to redistribute the program, including modification and sale,
under the condition that you'll keep it free for all other users.
visit www.gnu.org or type version -c for more info''')
        tips("")
def run(sw,args):
    lw=False
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
    if "l" in sw:
        lw=True
    if "e" in sw:
        wr=separ(wr)
    if args[0].isnumeric()!=True:
        print("Error:run command:wrong input type (speed)")
    if args[1].isnumeric()!=True and int(args[1])<101:
        print("Error:run command:wrong input type (errors)")
    if "w" not in sw:
        print("wait 3 seconds")
        time.sleep(3)
    try: vol=args[3]
    except: vol=' '
    try: typer.typer(wr,int(args[0]),int(args[1]),vol,onscreen_kb,use_cap,write_out,kb,disable_bp,lw)
    except Exception as e: print("Error: Python error: " + str(e) + "\nPlease report this report to me using GitHub Issues")
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
                #if "$debug" in receiveargs: print(receiveargs)
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
if len(sys.argv)>1 and sys.argv[1] not in all_commands: print("Error: Unknown command")
