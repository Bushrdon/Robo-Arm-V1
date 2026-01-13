# Log

**Cosas temrminadas y cosas por terminar:**

La barrera entre lo que esta terminado y lo que potencialmente puede enferentarse a cambios es algo delgada, pero para tener nocion de progreso esta bien basarnos en esta lista.

**Ya hecho:**

1.Firmware: 
a. Framework definido: Arduino
b. Libreria definida: AccelStepper
2.Software:
a. Lenguaje definido: Python
b. GUI en: Tkinter
c. Libreria para Serial UART: PySerial
3.Hardware:
a. Unidad de Controlador: ESP32

**Por hacer:**

Hardware:
a. Terminar de decidir por modelo y tipo de motor paso a paso

	Sugiero el modelo de un bipolar NEMA17 si se pretende hacer la estructura con impresion 3d

b. Decidirse por los drivers relativos al tipo de motor que se usara 

	Sugiero el DRV8825, en general sugiero todo lo propuesto en 'Hardware/README.md'
	
Estructura:

a. Definir si se hara usando impresion 3D o materiales mas improvisados y ligeros
b. Definir si la estructura implementara sistemas de transmision para hacer llegar movimiento a cada articulacion o sera mas simple y solo implementara lo descrito en 'Robo-Arm/Hardware'
c. Definir si se considera agregarle un elemento terminal o solo nos limitaremos a hacer un brazo articulado

# Overview

 Robot Angular con 3 GDL controlado por medio de una interfaz grafica en Python/Tkinter y un microcontrolador ESP32 mediante motores paso a paso.
 
 <img src="preview.png"/>
 
## Features

 El proyecto integra control directo de los motores paso a paso mediante una GUI simple ademas de una serie de funciones presentadas como botones extra para ejecutar patrones de movimiento especificos. 
 
 <img src="GUI_preview.png">
 
 El robot tambien posee elementos terminales intercambeables destinados a demostrar la utilidad de los patrones de movimiento integrados en la GUI. 
 Funciones como Control de Velocidad por sensores y mecanismo complejos de transmision aun estan en contemplacion. 

## Project Structure

 * **Embedded** - Codigo embedido en C/C++ usando el framework de Arduino y su IDE

 * **Tkinter Code** - Codigo de alto nivel para la interfaz grafica y representacion visual del robot que implementa la libreria Pillow para el manejo de imagenes

 * **Pyserial Code** - Codigo que define la interfaz de comunicacion serial entre la PC y el microcontrolador implementando la libreria PySerial

 * **Schematics** - Documentacion referente a las conexiones y montaje general del hardware implementado
 
 * **CAD Models** - Referencia de modelos 3D usados para el robot.


## Prerequisites 

 * **Hardware**: 
   - Placa Espressif ESP32
   - Motores Paso a Paso
   - Cable Mini-USB
   
 * **Software**:
   - Arduino IDE
   - Python 3.13>=
   - ESP32 Arduino Core
   - Accelstepper Library
   
 * **Pip Packages**:
   - Pillow 
   - PySerial
	

## Installation/Setup

	[Bajo desarrollo]
	
## Additional Notes:

 Se tendran diversos archivos README para cada seccion mayor del repositorio. El proyecto podra tener multiples ramas dedicadas a versiones nativas y a versiones de desarrollo y master. Actualmente este repositorio solo tiene la rama de master.
