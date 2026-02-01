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

## Things to Do:

Poner botones para controlar el elemento terminal. Habria que ponerle un asset para la pinza.

Me gustaria que hubiera una parte donde se puedan leer las acciones que se realizan, es decir: que lo que se pueda leer en la terminal cuando se corra el codigo que tambien se pueda visualizar en la GUI, cosas como "Enviado 'q' Moviendo Joint 3" o algo por el estilo. Podriamos hacer algo analogo a esto. Pero estaria genial adaptarle un "Serial monitor" como en el arduino IDE.

Me gustataria que se pudiera regular la cantidad de pasos que se de. Con una barra de volumen se podria implementar. Esto se logra con el widget de [Scale](https://tkdocs.com/tutorial/morewidgets.html#scale), en el tutorial se explica mejor la idea, tengo que hacer mas flexible el codigo del archivo .ino para que la variable de "steps" se modifique en cada articulacion y que el Scale se aplica para toda articulacion.

Podriamos tambien implementar una opcion para configurar el puerto serial. Una ventana que te dejara configurar los puertos que quieras utilizar, seria una lista de "COM" del 1 hasta el 15 solo para mantenerlo simple y no poner algo asi como una funcion que chequee los puertos disponibles y luego los muestre, aunque no crea que sea dificil de implementar. Esto se logra con el widget [Listbox](https://tkdocs.com/tutorial/morewidgets.html#listbox) segun parece. Ahi se ve el tutorial, tendria que preparar el backend con Pyserial para eso.


## Gallery

Still working on it!
