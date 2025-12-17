# Getting Started

Con esta guia podras poner poner todo el orden para usar el programa de una forma mas practica. 

Para correr el codigo puedes simplemente correr el codigo desde la terminal estando el directorio apropiado:

	python main.py

## Prerequisites

Asegurate de tener una version estable y reciente de python 3
Tambien debes tener instalados los siguientes modulos:

  - Pillow
  - Pyserial
  - pathlib (modulo que viene por defecto con python)
  - Tkinter (modulo que viene por defecto con python)


## Setup and building via Meson (For Linux only)

Esta guia es para construir el codigo a partir de [Meson Build System](https://mesonbuild.com/Getting-meson.html) unicamente para dispositivos Linux. 
Asegurate de tener instalado para comenzar con el building del codigo. 


## Configuring Assets

Esta seccion es importante dado que el codigo actualmente implementa el modulo pathlib que navega entre los directorios de tu sistema para encontrar los diferentes assets que contiene la interfaz grafica.
Esto es muy inconveniente por temas de distribucion dado que naturalmente nadie tendra la misma ruta para acceder a estos archivos lo que haria que el programa crasheara.
A menos que encuentre una forma de hacer mas redistribuible esa parte del codigo se tendra que configurar manualmente para todo el que quiera probar el programa. 

Actualmente la linea donde se define el path es la linea 11 es main.py

	SRC = Path('D:/DATA/Desktop/RoboArm/Software/main/src/main.py').resolve().parent

Por favor asegurate de no cambiar de ninguna forma los directorios del programa. El path tiene que senalar donde se encuentra el codigo fuente de la apliacion **incluyendo** el archivo .py

## Gallery

<>
