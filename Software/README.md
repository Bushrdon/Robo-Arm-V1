# Getting Started

Para correr el codigo puedes simplemente correr el codigo desde la terminal estando el directorio apropiado:

	python main.py

## Prerequisites

You need to have python 3.13
Also, install all this modules for the program to work properly:

  - Pillow
  - Pyserial

The program also utilizes Tkinter and Pathlib but they are already installed if you have python install. 

## Features:

The program is based mainly on the idea that you can control direct motor movement in both directions. In case of servos, you have a button for opening and closing the clamp.
A button for abort stepper movement disabling outputs can also be found. 
"View" submenu is currently non-functional at all. But it was intended to show serial monitor inside the application. 
The program also features a simple COM Port manager. There's no great exception hnadling system, just some Error message shown in the terminal, so it is not robust enough.
