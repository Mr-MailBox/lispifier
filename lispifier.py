'''
god forgives all, regardless of sin
'''
import pyperclip as pc

if input("y to copy clipboard, n to exit: ") == "y":
    art = pc.paste()
else:
    quit()

#find every r and replace it with a w
art = art.replace('r', 'w')
art = art.replace('l', 'w')
art = art.replace('R', 'W')
art = art.replace('L', 'W')
#Lay thy eyes upon salvation.
print(art)

