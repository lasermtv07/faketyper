import copy
import os
import subprocess
import time
import random
import math
from pynput.keyboard import Key, Controller
keyboard=Controller()
def typer(text,cpm,error,replace_string,kb_use,use_caps,write_out,kb_original,disable_bp):
    sofar=""
    if replace_string==' ' or replace_string==None:
        replace_string='qwertyuiop[]asdfghjkl;zxcvbnm,./=´§ů,.-'
    index=0
    space_off='CTRL   WIN   ALT   [  SPACE  ]   ALT   OPT   CTRL'
    space_on='CTRL   WIN   ALT   [_________]   ALT   OPT   CTRL'
    kb=copy.deepcopy(kb_original)
    #print(kb_original)
    def draw_ty(draw):
        for x in draw:
            for y in x:
                print(y, end='   ')
            print()



    while index<len(text):
        tindex=text[index]
        if random.randint(0,100)==55 and error>0 and error<len(text)-len(sofar):
            tindex=random.choice(replace_string)
        elif error>len(text)-len(sofar): 
            tindex=random.choice(replace_string)
        for z in kb:
            if tindex in z:
                ind=z.index(tindex)
                z[ind] = "█"
        
        if kb_use==1: draw_ty(kb)
        if tindex==' ' and kb_use==1 :print(space_on)
        elif kb_use==1:print(space_off)
        if write_out==1: print(sofar)
        if tindex=="¦" and disable_bp==True:
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        else:
            keyboard.type(tindex)
        kb=copy.deepcopy(kb_original)
        sofar+=tindex
        time.sleep(1/cpm)
        if os.name=='nt': os.system('cls')
        elif os.name=='posix': os.system('clear')
        index+=1
