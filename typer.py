import copy
import os
import subprocess
import time
import random
import math
import keyboard as kbm
from pynput.keyboard import Key, Controller
keyboard=Controller()
#edit recursive!
def typer(text,cpm,error,replace_string,kb_use,use_caps,write_out,kb_original,disable_bp,lw):
    sofar=""
    if replace_string==' ' or replace_string==None:
        replace_string='qwertyuiop[]asdfghjkl;zxcvbnm,./=´§ů,.-'
    index=0
    space_off='CTRL   WIN   ALT   [  SPACE  ]   ALT   OPT   CTRL'
    space_on='CTRL   WIN   ALT   [_________]   ALT   OPT   CTRL'
    kb=copy.deepcopy(kb_original)
    #print(kb_original)
    def draw_ty(draw,ti):
        for x in draw:
            for y in x:
                if ti.isupper(): print(y.upper(), end='   ')
                else: print(y, end='   ')
            print()

    while index<len(text):
        
        tindex=text[index]
        if random.randint(0,100)==55 and error>0 and error<len(text)-len(sofar):
            tindex=random.choice(replace_string)
        elif error>len(text)-len(sofar): 
            tindex=random.choice(replace_string)
        for z in kb:
            if tindex.lower() in z:
                ind=z.index(tindex.lower())
                z[ind] = "█"
        
        if kb_use==1: draw_ty(kb,tindex)
        if tindex==' ' and kb_use==1 :print(space_on)
        elif kb_use==1:print(space_off)
        if write_out==1: print(sofar)
        if tindex=="¦" and disable_bp==True:
            keyboard.press(Key.backspace)
            keyboard.release(Key.backspace)
        elif tindex=="^" and disable_bp==True:
            keyboard.press(Key.space)
            keyboard.release(Key.space)
        elif tindex=="¬" and disable_bp==True:
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
        else:
            keyboard.type(tindex)
        kb=copy.deepcopy(kb_original)
        sofar+=tindex
        time.sleep(1/cpm)
        if os.name=='nt': os.system('cls')
        elif os.name=='posix': os.system('clear')
        if kbm.is_pressed('esc'):
            print("Typing stopped")
            exit()
        index+=1

    if lw==True: typer(text,cpm,error,replace_string,kb_use,use_caps,write_out,kb_original,disable_bp,lw)
