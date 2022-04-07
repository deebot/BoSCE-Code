from random import random
from tkinter import *
from mss import mss
import time

root = Tk()
root.title('Screen Shot')
w = 150 # width for the Tk root
h = 100 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = ((ws/2) - (w/2))- 700
y = ((hs/2) - (h/2)) - 500

# set the dimensions of the screen 
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.resizable(False, False)

def shot():
	with mss() as sct:
		filename =sct.shot(mon=1,output="output.png")
		my_label.config(text="screen shot taken")
my_button =Button(root, text="Take a screenshot",command=shot)
my_button.pack(pady=40)

my_label =Label(root, text="")
my_label.pack(pady=10)
root.mainloop()