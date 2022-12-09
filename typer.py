import copy
import os
import time
import random
import keyboard
import math

def typer(text,cpm,correctness,replace_string,kb_use):
    if replace_string=='':
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
        for z in kb:
            if tindex in z:
                ind=z.index(tindex)
                z[ind] = "█"
        
        if kb_use==1: draw_ty(kb)
        if tindex==' ' and kb_use==1 :print(space_on)
        elif kb_use==1:print(space_off)
        keyboard.write(tindex)
        print(tindex)
        kb=copy.deepcopy(kb_original)
        time.sleep(1/cpm)
        #os.system('cls')
        index+=1

typer("YoU aRe A fUcKiNg BiTcH", 5, 100,'',0)
#qwertyqwertyqwertyqwertyasdxmqwertyasdxmqwertyasdxmqqqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxm
#qwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmenglish keyboard text hahahahahhahaahasdsasdassasdsasdasssttexttexttexttexttexttexttexttexttexttexttexttexttexttextte xtte xt
#te xt text2 texnnhihihihihihniaidsadacdra
#avokahocmhahnjanoj
#nhojnhojahojahojnjhafnkhafjkahfjkahfjkahfkjnhfknasnfkadfkjjfahhakjfhanfhajknhakjfnjkahfanfhjnnfhjkafhjkahfjkahfjkahfakfhfafhnafhkjdnafhnkafnajfhajfhknnhfahfafhakhfanknfhnkfanjkanhnkjfhakhlandknfhakhnadkfh
#ahojnhojahnnahojkjhafjkhnfjkahfjnnhfjkahfkjahfkjnshfnanfkjjfanhakjfhajnhajkfnakjfhjknhfajfhjknfnjkafhnnahfjkahnjkahfakfhnafhnanhkjdsanhjkafhajfhajfhkjahfahfnfhakhnajkcnhjkfahjkafhakjfhanhlasdkjfnanngadkfh
#ahojahojahojahojkjhafjkhafjkahfjkahfjkahfkjahfkjashfkadfkjjfahhakjfhajfhajkfhakjfhjkahfajfhjkafhjkafhjkahfjkahfjkahfakfhfafhkafhkjdsafhjkafhajfhajfhkjahfahfafhakhfajkcfhjkfahjkafhakjfhakhlasdkjfhakhgadkfh
#hello you fuckinjg bitch
#hello you fuckinjg bitch
#you are a ukin itchyou are a ukin itch
#you are a ukin itchyou are a ukin itch
#you are a fucking bitch
#you are a fucking bitchYoU aRe A fUcKiNg BiTcH