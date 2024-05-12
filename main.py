import tkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *
'''
Auuuuuuuu, I guess I am doing this now, for whoever is following along,
I will probably leave these comments at the end of certain chunks to state my current issues,
but don't answer, just go bruh how can you have such donut issue
'''

window = tk.Tk()
window.title("Rat Maid")
window.iconbitmap(r'C:\Users\julia\Downloads\favicon.ico')
window.geometry('500x500')
window.attributes('-alpha',0.75)
'''
Let's go, I have transparency now
'''
char1 = PhotoImage(file = r'C:\Users\julia\Downloads\idle-1-preview.png')
canv = tkinter.Canvas(window, bg='white', height=500, width=500)
creation = canv.create_image(250, 250, image=char1, )
'''
Sprite added (it started to fleeping not add because of file= >:(
, but I figured that out :D)
New problem is that I can't make object opaque without making window not opaque
'''
canv.pack()
window.mainloop()