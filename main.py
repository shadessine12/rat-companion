import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
import random
import time
'''
Auuuuuuuu, I guess I am doing this now, for whoever is following along,
I will probably leave these comments at the end of certain chunks to state my current issues,
but don't answer, just go bruh how can you have such donut issue
'''
x = 1400
width = 73
height = 108
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
canv = tkinter.Canvas(window, bg='black', height=height, width=width)
char1 = PhotoImage(file = r'C:\Users\julia\OneDrive\Pictures\idle-1-preview.png')
char2 = PhotoImage(file = r'C:\Users\julia\OneDrive\Pictures\idle-2-preview.png')
char3 = PhotoImage(file = r'C:\Users\julia\OneDrive\Pictures\idle-3-preview.png')
char4 = PhotoImage(file = r'C:\Users\julia\OneDrive\Pictures\idle-4-preview.png')
char5 = PhotoImage(file = r'C:\Users\julia\OneDrive\Pictures\idle-5-preview.png')
char6 = PhotoImage(file = r'C:\Users\julia\OneDrive\Pictures\idle-6-preview.png')
idle = [char1, char2, char3, char4, char5, char6]
def idleAni (idle):
    for i in idle:
        time.sleep(10)
        canv.create_image(width / 2, height / 2, image=i, )
        canv.pack()
        time.sleep(10)
        canv.delete('all')
        canv.pack()
'''
Sprite added (it started to fleeping not add because of file= >:(
, but I figured that out :D)
New problem is that I can't make object opaque without making window not opaque
'''
idleAni(idle)
canv.pack()
window.mainloop()