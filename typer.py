import copy
import os
import time
import random
import keyboard
import math

def typer(text,cpm,correctness,replace_string):
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
        if random.randint(0,math.ceil(correctness))==0 and correctness<100:
            t=random.randint(0,len(replace_string)-1)
            tindex=replace_string[t]
        for z in kb:
            if tindex in z:
                ind=z.index(tindex)
                z[ind] = "█"
        
        draw_ty(kb)
        if tindex==' ':print(space_on)
        else:print(space_off)
        keyboard.send(tindex)
        kb=copy.deepcopy(kb_original)
        time.sleep(1/cpm)
        os.system('cls')
        index+=1
#qwertyqwertyqwertyqwertyasdxmqwertyasdxmqwertyasdxmqqqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxm
#qwertyasdxmqwertyasdxmqwertyasdxmqwertyasdxmenglish keyboard text hahahahahhahaahasdsasdassasdsasdasssttexttexttexttexttexttexttexttexttexttexttexttexttexttextte xtte xt
#te xt text2 texnnhihihihihihniaidsadacdra
#avokahocmhahnjanoj
#nhojnhojahojahojnjhafnkhafjkahfjkahfjkahfkjnhfknasnfkadfkjjfahhakjfhanfhajknhakjfnjkahfanfhjnnfhjkafhjkahfjkahfjkahfakfhfafhnafhkjdnafhnkafnajfhajfhknnhfahfafhakhfanknfhnkfanjkanhnkjfhakhlandknfhakhnadkfh
#ahojnhojahnnahojkjhafjkhnfjkahfjnnhfjkahfkjahfkjnshfnanfkjjfanhakjfhajnhajkfnakjfhjknhfajfhjknfnjkafhnnahfjkahnjkahfakfhnafhnanhkjdsanhjkafhajfhajfhkjahfahfnfhakhnajkcnhjkfahjkafhakjfhanhlasdkjfnanngadkfh
#ahojahojahojahojkjhafjkhafjkahfjkahfjkahfkjahfkjashfkadfkjjfahhakjfhajfhajkfhakjfhjkahfajfhjkafhjkafhjkahfjkahfjkahfakfhfafhkafhkjdsafhjkafhajfhajfhkjahfahfafhakhfajkcfhjkfahjkafhakjfhakhlasdkjfhakhgadkfh
#