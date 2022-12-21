import copy
import os
import subprocess
import time
import random
import keyboard
import math

def typer(text,cpm,error,replace_string,kb_use,use_caps,write_out):
    if replace_string==' ' or replace_string==None:
        replace_string='qwertyuiop[]asdfghjkl;zxcvbnm,./'
    index=0
    space_off='CTRL   WIN   ALT   [  SPACE  ]   ALT   OPT   CTRL'
    space_on='CTRL   WIN   ALT   [_________]   ALT   OPT   CTRL'
    kb_original=[['`','1','2','3','4','5','6','7','8','9','0','-','='],
    ['q','w','e','r','t','y','u','i','o','p','[',']','\ '],
    ['a','s','d','f','g','h','j','k','l',';','"','ENTER'],
    ['z','x','c','v','b','n','m',',','.','/',' SHIFT']
    ]
    kb=copy.deepcopy(kb_original)
    #print(kb_original)
    def draw_ty(draw):
        for x in draw:
            for y in x:
                print(y, end='   ')
            print()

    while index<len(text):
        tindex=text[index]
        if random.randint(0,error)==error and error!=0:
            tindex=random.choice(replace_string)
        for z in kb:
            if tindex in z:
                ind=z.index(tindex)
                z[ind] = "█"
        
        if kb_use==1: draw_ty(kb)
        if tindex==' ' and kb_use==1 :print(space_on)
        elif kb_use==1:print(space_off)
        if use_caps==1: keyboard.write(tindex)
        else: keyboard.send(tindex)
        if write_out==1: print(tindex, end=' ')
        kb=copy.deepcopy(kb_original)
        time.sleep(1/cpm)
        if write_out==0:
            if os.system('cls')!=0:
                os.system('clear')
        index+=1
