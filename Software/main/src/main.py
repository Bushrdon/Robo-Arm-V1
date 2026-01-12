from tkinter import *
import tkinter as tk

import os
from pathlib import Path

from PIL import ImageTk, Image


# Define Button Commands

#def MOVE_UP_1:
#    ser.write(b'q')

#def MOVE_DOWN_1:
#    ser.write(b'w')

#def MOVE_UP_2:
#    ser.write(b'e')

#def MOVE_DOWN_2:
#    ser.write(b'r')

#def ROTATE_RIGHT:
#    ser.write(b's')

#def ROTATE_LEFT:
#    ser.write(b't')

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

up_arrow_1 = ImageTk.PhotoImage(Image.open(UP_ARROW))
btn = tk.Button(root)
btn.grid(column=2, row=1, padx=2, pady=2)
btn['image']=up_arrow_1

down_arrow_1 = ImageTk.PhotoImage(Image.open(DOWN_ARROW))
btn2= tk.Button(root)
btn2.grid(column=2, row=3, padx=2, pady=2)
btn2['image']=down_arrow_1

joint1 = ImageTk.PhotoImage(Image.open(JOINT_1))
label1= tk.Label(root)
label1.grid(column=2, row=2, padx=2, pady=2)
label1['image'] = joint1

up_arrow_2 = ImageTk.PhotoImage(Image.open(UP_ARROW))
btn3 = tk.Button(root)
btn3.grid(column=4, row=1, padx=2, pady=2)
btn3['image']=up_arrow_2

down_arrow_2 = ImageTk.PhotoImage(Image.open(DOWN_ARROW))
btn4= tk.Button(root)
btn4.grid(column=4, row=3, padx=2, pady=2)
btn4['image']=down_arrow_2

joint2 = ImageTk.PhotoImage(Image.open(JOINT_2))
label2 = tk.Label(root, text = "joint_2")
label2.grid(column=4, row=2, padx=2, pady=2)
label2['image'] = joint2

right_arrow = ImageTk.PhotoImage(Image.open(RIGHT_ARROW))
btn5= tk.Button(root)
btn5.grid(column=7, row=2, padx=2, pady=2)
btn5['image']=right_arrow

left_arrow = ImageTk.PhotoImage(Image.open(LEFT_ARROW))
btn6= tk.Button(root)
btn6.grid(column=5, row=2, padx=2, pady=2)
btn6['image']=left_arrow

joint3 = ImageTk.PhotoImage(Image.open(JOINT_3))
label3= tk.Label(root, text = "joint_3")
label3.grid(column=6, row=2, padx=2, pady=2)
label3['image'] = joint3

root.geometry("600x400")
root.mainloop()
