
from tkinter import *
import tkinter as tk

import os
from pathlib import Path

from PIL import ImageTk, Image

import serial

# Initiate COM and Configure

ser = serial.Serial('COM3', 9600, timeout=1)

if not ser.is_open:
    ser.open()

# Define Button Commands

def MOVE_UP_1():
    ser.write(b'q')

def MOVE_DOWN_1():
    ser.write(b'w')

def MOVE_UP_2():
    ser.write(b'e')

def MOVE_DOWN_2():
    ser.write(b'r')

def ROTATE_RIGHT():
    ser.write(b's')

def ROTATE_LEFT():
    ser.write(b't')

#Terminal
    
def OPEN():
    ser.write(b'a')

def CLOSE():
    ser.write(b'm')

# Miniterm. Go easy with this call 'cause it does not neccesarly work

def Open_term():
    os.system('python -m serial.tools.miniterm COM1')

# Define Path for GUI images

SRC = Path(__file__).resolve().parent  
GUI = SRC.parent
IMG_DIR = GUI /"img"

UP_ARROW = IMG_DIR /"up-arrow.png"
LEFT_ARROW = IMG_DIR /"left-arrow.png"
DOWN_ARROW = IMG_DIR /"down-arrow.png"
RIGHT_ARROW = IMG_DIR /"right-arrow.png"
JOINT_1 = IMG_DIR /"joint_1.png"
JOINT_2 = IMG_DIR /"joint_2.png"
JOINT_3 = IMG_DIR /"joint_3.png"

# GUI Composition (using pillow)

root = Tk()
root.title("Robot Arm")

button = tk.Button(root, command=OPEN, text='Abrir Pinza')
button.grid(column=1, row=1, padx=2, pady=2)

button = tk.Button(root, command=CLOSE, text='Cerrar Pinza')
button.grid(column=1, row=2, padx=2, pady=2)

up_arrow_1 = ImageTk.PhotoImage(Image.open(UP_ARROW))
btn = tk.Button(root, command = MOVE_UP_1)
btn.grid(column=2, row=1, padx=2, pady=2)
btn['image']=up_arrow_1

down_arrow_1 = ImageTk.PhotoImage(Image.open(DOWN_ARROW))
btn2= tk.Button(root, command = MOVE_DOWN_1)
btn2.grid(column=2, row=3, padx=2, pady=2)
btn2['image']=down_arrow_1

joint1 = ImageTk.PhotoImage(Image.open(JOINT_1))
label1= tk.Label(root)
label1.grid(column=2, row=2, padx=2, pady=2)
label1['image'] = joint1

up_arrow_2 = ImageTk.PhotoImage(Image.open(UP_ARROW))
btn3 = tk.Button(root, command = MOVE_UP_2)
btn3.grid(column=4, row=1, padx=2, pady=2)
btn3['image']=up_arrow_2

down_arrow_2 = ImageTk.PhotoImage(Image.open(DOWN_ARROW))
btn4= tk.Button(root, command = MOVE_DOWN_2)
btn4.grid(column=4, row=3, padx=2, pady=2)
btn4['image']=down_arrow_2

joint2 = ImageTk.PhotoImage(Image.open(JOINT_2))
label2 = tk.Label(root, text = "joint_2")
label2.grid(column=4, row=2, padx=2, pady=2)
label2['image'] = joint2

right_arrow = ImageTk.PhotoImage(Image.open(RIGHT_ARROW))
btn5= tk.Button(root, command = ROTATE_RIGHT)
btn5.grid(column=7, row=2, padx=2, pady=2)
btn5['image']=right_arrow

left_arrow = ImageTk.PhotoImage(Image.open(LEFT_ARROW))
btn6= tk.Button(root, command = ROTATE_LEFT)
btn6.grid(column=5, row=2, padx=2, pady=2)
btn6['image']=left_arrow

joint3 = ImageTk.PhotoImage(Image.open(JOINT_3))
label3= tk.Label(root, text = "joint_3")
label3.grid(column=6, row=2, padx=2, pady=2)
label3['image'] = joint3

# Key Bindings. Very intuitive way of GUI controlling I suppose. Need a fix bacause functions callings takes 0 positional arguments. Do not use.

root.bind("w", MOVE_UP_1)
root.bind("s", MOVE_DOWN_1)
root.bind("a", ROTATE_LEFT)
root.bind("d", ROTATE_RIGHT)
root.bind("q", OPEN)
root.bind("e", CLOSE)

# Implementing console terminal. Not Working currently

term = tk.Button(root, command=Open_term, text='Monitor Serial')
term.grid(column=1, row=4, padx=2, pady=2)


root.geometry("600x400")
root.mainloop()
