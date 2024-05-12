import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
'''
Auuuuuuuu, I guess I am doing this now, for whoever is following along,
I will probably leave these comments at the end of certain chunks to state my current issues,
but don't answer, just go bruh how can you have such donut issue
'''
x = 1400
width = 73
height = 108
idle = [1, 2, 3, 4, 5, 6]
event_number = random.randrange(1, 6)
window = tk.Tk()
window.title("Rat Maid")
window.iconbitmap(r'C:\Users\julia\Downloads\favicon.ico')
window.geometry('73x108+'+str(x)+'+711')
window.attributes('-alpha',1.0)

window.config(highlightbackground='black')
window.overrideredirect(True)
window.wm_attributes('-transparentcolor', 'black')

'''
Let's go, I have transparency now
'''
char1 = PhotoImage(file = r'C:\Users\julia\OneDrive\Pictures\idle-1-preview.png')
canv = tkinter.Canvas(window, bg='black', height=height, width=width)
creation = canv.create_image(width/2, height/2, image=char1, )
'''
Sprite added (it started to fleeping not add because of file= >:(
, but I figured that out :D)
New problem is that I can't make object opaque without making window not opaque
'''
canv.pack()
window.mainloop()