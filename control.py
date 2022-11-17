import sys
import os.path
import typer
import time
arg=len(sys.argv)
run_speed=60
errors=100
error_characters=''
string='test'
if arg==1:
    print("NOTE: THIS IS OPEN TESTING AND BACKUP VERSION ONLY AND IS NOT MEANT TO REPRESENT THE FINISHED PRODUCT!")
    print("More info within help that you can open with faketyper help")
    print("Version: beta v1.0")
    print("Program by lasermtv")
for x in range(1,arg):
    if sys.argv[x]=='v' or sys.argv[x]=='version':
        print("NOTE: THIS IS OPEN TESTING AND BACKUP VERSION ONLY AND IS NOT MEANT TO REPRESENT THE FINISHED PRODUCT!")
        print("More info within help that you can open with faketyper help")
        print("Version: beta v1.0")
        print("Program by lasermtv")
        break
    if sys.argv[x]=='r' or sys.argv[x]=='run':
        if arg<5:
            print("Error: One or more required arguments are missing: faketyper r <speed> <errors> <string> [error characters]")
            print("                                                              ^") 
        else:
            if sys.argv[x+1].isnumeric()==False:
                print("Error: Wrong argument here: faketyper r <speed> <errors> <string> [error characters]")
                print("                                         ^")
            elif int(sys.argv[x+1])>100000 or int(sys.argv[x+1])<0:
                print("Error: Number is too high or too low: faketyper r <speed> <errors> <string> [error characters]")
                print("                                                   ^")
            else:
                run_speed=int(sys.argv[x+1])
                if sys.argv[x+2].isnumeric()==False:
                    print("Error: Wrong argument here: faketyper r <speed> <errors> <string> [error characters]")
                    print("                                                ^")
                elif int(sys.argv[x+2])>100000 or int(sys.argv[x+2])<0:
                    print("Error: Number is too high or too low: faketyper r <speed> <errors> <string> [error characters]")
                    print("                                                           ^")
                else:
                    errors=int(sys.argv[x+2])
                    if sys.argv[x+3]=='':
                        print("Error: No string input: faketyper r <speed> <errors> <string> [error characters]")
                        print("                                                      ^")
                    else:string=sys.argv[x+3]
                    if arg>x+4: error_characters=sys.argv[x+4]
                    print("3 seconds delay is set up before start. Please, place your cursor where you want to type")
                    time.sleep(3)
                    typer.typer(string,run_speed,errors,error_characters)
                    print("Task Done")
    if sys.argv[x]=='h' or sys.argv[x]=='help':
        print("HELP")
        print("====")
        print("Note: This is a beta and it is NOT SUPPOSED TO REPRESENT THE FULL PRODUCT! I only wanna backup it here as Im gonna have to rewrite a big chunk of it,")
        print("      because the code is pretty bad. But if u use it anyway and find a bug, please report it here: https://forms.gle/zrfyfarPjU3WtuQB7")
        print("      Also dont look at it unless you wanna add it to your cringe compilation.\n      Your Laser =)")
        print("Syntax marks: <arg> - required argument")
        print("              [arg] - additional, not required argument")
        print("Commands:")
        print("run - r - starts the typer. Syntax: faketyper r <speed> <errors> <string> [error characters]")
        print("       <speed> - amount of characters written per second")
        print("       <errors> - number of errors in the output. 100 is no errors, 0 is all characters replaced by random generator.")
        print("       <string> - what you want the simulator to write")
        print("       [error characters] - list of all characters from which characters that replace errors will be choosen")
        print("version - v - prints current version and author. Syntax: faketyper v")
        print("help - h - prints this help")

