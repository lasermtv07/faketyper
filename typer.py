import copy
import os
import subprocess
import time
import random
import math
from pynput.keyboard import Controller

keyboard=Controller()
def typer(text,cpm,error,replace_string,kb_use,use_caps,write_out,kb_original):
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
        if random.randint(0,error)==error and error!=100:
            tindex=random.choice(replace_string)
        for z in kb:
            if tindex in z:
                ind=z.index(tindex)
                z[ind] = "█"
        
        if kb_use==1: draw_ty(kb)
        if tindex==' ' and kb_use==1 :print(space_on)
        elif kb_use==1:print(space_off)
        keyboard.type(tindex)
        if write_out==1: print(tindex, end=' ')
        kb=copy.deepcopy(kb_original)
        time.sleep(1/cpm)
        if write_out==0:
            if os.name=='nt': os.system('cls')
            elif os.name=='posix': os.system('clear')
        index+=1
