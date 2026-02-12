# Overview

 Robot Angular con 4 GDL controlado por medio de una interfaz grafica en Python/Tkinter y un microcontrolador ATmega328p mediante motores paso a paso unipolares y servo motores.
 
 <img src="preview.png"/>

# Important Note

This is Robo-Arm-V1 which features high level embedded code and low potency 24BYJ48-BJ stepper motors, simple GUI interface. A Robotic-Arm-V2 will be developed soon. Or never.

## Contents 

|Folder | Contents |
|-------|----------|
|[CAD](https://github.com/Bushrdon/Robo-Arm/tree/master/CAD)|Archivos CAD de modelos 3D|
|[Firmware](https://github.com/Bushrdon/Robo-Arm/tree/master/Firmware)|Archivo .ino con su documentacion|
|[Hardware](https://github.com/Bushrdon/Robo-Arm/tree/master/Hardware)|Esquemas electronicos, documentacion y simulacion en proteus 8.15|
|[Software](https://github.com/Bushrdon/Robo-Arm/tree/master/Software)|Assests y codigo de la GUI y programacion serial|
 
## Features

 El proyecto integra control directo de los motores mediante una GUI simple, al mismo tiempo soporta manejo de puertos seriales configurables y funciones de apagado. 
 
 <img src="GUI_preview.png">
 
## Project Structure

 * **Embedded** - Codigo embedido en C/C++ usando el framework de Arduino y su IDE

 * **Tkinter Code** - Codigo de alto nivel para la interfaz grafica y representacion visual del robot que implementa la libreria Pillow para el manejo de imagenes

 * **Pyserial Code** - Codigo que define el backend para comunicacion serial entre la PC y el microcontrolador

 * **Schematics** - Documentacion referente a las conexiones y montaje general del hardware implementado
 
 * **CAD Models** - Referencia de modelos 3D usados para el robot.


## Prerequisites 

 * **Hardware**: 
   - Placa Arduino UNO (O compatible)
   - Motores Paso a Paso Unipolares 24BYJ48-BJ
   - Modulo para ULN2003A
   - Servomotores MG90S
   - Cable USB mini USB-B (ESP32 USB Cable)
   
 * **Software**:
   - Arduino IDE
   - Python 3.13
   - Accelstepper Library
   
 * **Pip Packages**:
   - Pillow 
   - PySerial
	
## How to Use

First, upload the Arduino code after following the schematics provided in Hardware/Schemes

Connect your board to the host PC and power the steppers with >24 Watts of potency. (Lesser or equal will be dangerous)

Open your terminal, search for Software/main/src/main.py and run it by entering:

	python main.py

In GUI, select the COM Port you are using. You will get error message in case of selecting a closed COM Port.

Use
	
	
