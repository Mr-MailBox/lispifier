'''
god forgives all, regardless of sin
'''
import pyperclip as pc
import tkinter as tk

if input("y to copy clipboard, n to exit: ") == "y":
    art = pc.paste()
else:
    quit()
x = 0
foo = input("press r to remove characters, l to lispify ")
if foo == 'r':
    loops = int(input("how many different characters? "))
    characters = []
    for x in range(loops):
        d = input("character? ")
        characters.append(d)
        print(characters)
        
    times = len(characters)
    while x < times:
        art = art.replace(characters[x],'')
        x += 1
        
    print(times)
    print(art)
    
elif foo == 'l':
    #find every r and replace it with a w
    art = art.replace('r', 'w')
    art = art.replace('l', 'w')
    art = art.replace('R', 'W')
    art = art.replace('L', 'W')
    #Lay thy eyes upon salvation.
    print(art)

else:
    print('now u have to restart it you dumb idiot')
    



