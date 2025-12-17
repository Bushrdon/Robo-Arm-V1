from tkinter import *
import tkinter as tk

import os
from pathlib import Path

from PIL import ImageTk, Image

# Define Button Commands



# Define Path for GUI images

SRC = Path('D:/DATA/Desktop/RoboArm/Software/main/src/main.py').resolve().parent #Esto sera un problema con el tema de la redistribucion 
GUI = SRC.parent
IMG_DIR = GUI /"img"

UP_ARROW = IMG_DIR /"up-arrow.png"
LEFT_ARROW = IMG_DIR /"left-arrow.png"
DOWN_ARROW = IMG_DIR /"down-arrow.png"
ARROW = IMG_DIR /"arrow.png"
RIGHT_ARROW = IMG_DIR /"right-arrow.png"

# GUI Composition (using pillow)
root = Tk()
root.title("Robot Arm")

up_arrow = ImageTk.PhotoImage(Image.open(UP_ARROW))
btn = tk.Button(root)
btn.grid(column=2, row=1, padx=2, pady=2)
btn['image']=up_arrow

left_arrow = ImageTk.PhotoImage(Image.open(LEFT_ARROW))
btn1= tk.Button(root)
btn1.grid(column=1, row=2, padx=2, pady=2)
btn1['image']=left_arrow

down_arrow = ImageTk.PhotoImage(Image.open(DOWN_ARROW))
btn2= tk.Button(root)
btn2.grid(column=2, row=3, padx=2, pady=2)
btn2['image']=down_arrow

arrow = ImageTk.PhotoImage(Image.open(ARROW))
btn3= tk.Button(root)
btn3.grid(column=2, row=2, padx=2, pady=2)
btn3['image']=arrow

right_arrow = ImageTk.PhotoImage(Image.open(RIGHT_ARROW))
btn4= tk.Button(root)
btn4.grid(column=3, row=2, padx=2, pady=2)
btn4['image']=right_arrow

#we would need to include some image difference explaining the movement produced by each button

root.geometry("600x400")
root.mainloop()
