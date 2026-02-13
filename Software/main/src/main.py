
from tkinter import *
import tkinter as tk

import os
from pathlib import Path

from PIL import ImageTk, Image

import serial

ser = None

# Initiate COM and Configure

def  set_port(port):
    global ser
    try:
        if ser and ser.is_open:
            ser.close()

        ser = serial.Serial(port, 9600, timeout=0.1)

    except Exception as e:
        print("Error opening serial port. Not Connected")

        
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

def ELEVATE():
    ser.write(b'o')

def DESCEND():
    ser.write(b'p')
    
#Terminal
    
def OPEN():
    ser.write(b'a')

def CLOSE():
    ser.write(b'm')

#Abort Command

def ABORT():
    ser.write(b'l')
    
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

m = Menu(root)
m_config=Menu(m, tearoff=0)
m.add_cascade(menu=m_config, label="Configuracion")
m_ports=Menu(m_config, tearoff=0)
m_config.add_cascade(menu=m_ports, label="Seleccionar Puerto Serial()")
m_ports.add_command(label="Serial Ports")
m_ports.add_command(label="COM1", command=lambda: set_port("COM1"))
m_ports.add_command(label="COM2", command=lambda: set_port("COM2"))
m_ports.add_command(label="COM3", command=lambda: set_port("COM3"))
m_ports.add_command(label="COM4", command=lambda: set_port("COM4"))
m_ports.add_command(label="COM5", command=lambda: set_port("COM5"))
m_monitor=Menu(m, tearoff=0)
m.add_cascade(menu=m_monitor, label="Vista")
m_monitor.add_command(label="Abrir Monitor Serial")
root['menu'] = m

button = tk.Button(root, command=OPEN, text='Abrir Pinza')
button.grid(column=1, row=1, padx=2, pady=2)

button = tk.Button(root, command=CLOSE, text='Cerrar Pinza')
button.grid(column=1, row=2, padx=2, pady=2)

button = tk.Button(root, command=ELEVATE, text='Ascender Pinza')
button.grid(column=2, row=1, padx=2, pady=2)

button = tk.Button(root, command=DESCEND, text='Descender Pinza')
button.grid(column=2, row=2, padx=2, pady=2)

up_arrow_1 = ImageTk.PhotoImage(Image.open(UP_ARROW))
btn = tk.Button(root, command = MOVE_UP_1)
btn.grid(column=3, row=1, padx=2, pady=2)
btn['image']=up_arrow_1

down_arrow_1 = ImageTk.PhotoImage(Image.open(DOWN_ARROW))
btn2= tk.Button(root, command = MOVE_DOWN_1)
btn2.grid(column=3, row=3, padx=2, pady=2)
btn2['image']=down_arrow_1

joint1 = ImageTk.PhotoImage(Image.open(JOINT_1))
label1= tk.Label(root)
label1.grid(column=3, row=2, padx=2, pady=2)
label1['image'] = joint1

up_arrow_2 = ImageTk.PhotoImage(Image.open(UP_ARROW))
btn3 = tk.Button(root, command = MOVE_UP_2)
btn3.grid(column=5, row=1, padx=2, pady=2)
btn3['image']=up_arrow_2

down_arrow_2 = ImageTk.PhotoImage(Image.open(DOWN_ARROW))
btn4= tk.Button(root, command = MOVE_DOWN_2)
btn4.grid(column=5, row=3, padx=2, pady=2)
btn4['image']=down_arrow_2

joint2 = ImageTk.PhotoImage(Image.open(JOINT_2))
label2 = tk.Label(root, text = "joint_2")
label2.grid(column=5, row=2, padx=2, pady=2)
label2['image'] = joint2

right_arrow = ImageTk.PhotoImage(Image.open(RIGHT_ARROW))
btn5= tk.Button(root, command=ROTATE_RIGHT)
btn5.grid(column=8, row=2, padx=2, pady=2)
btn5['image']=right_arrow

left_arrow = ImageTk.PhotoImage(Image.open(LEFT_ARROW))
btn6= tk.Button(root, command=ROTATE_LEFT)
btn6.grid(column=6, row=2, padx=2, pady=2)
btn6['image']=left_arrow

joint3 = ImageTk.PhotoImage(Image.open(JOINT_3))
label3= tk.Label(root, text = "joint_3")
label3.grid(column=7, row=2, padx=2, pady=2)
label3['image'] = joint3

abort= tk.Button(root, text="Apagar", command=ABORT)
abort.grid(column=1, row=5, padx=2, pady=2)

root.geometry("600x400")
root.mainloop()
