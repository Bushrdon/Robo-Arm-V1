# Getting Started

El codigo deberia de poder ser compilado como cualquier dispositivo AVR con las especificaciones del Arduino UNO. 
Selecciona el Dev Board desde el IDE de Arduino y el puerto serial, luego sube el codigo a la tarjeta. 

Para flashear el codigo en la tarjeta sin el arduino IDE puedes utilizar el Makefile dejado junto con el codigo fuente mas las herramientas de AVR. 

# Code Structure

The first section belongs to data definitions, servo definitions and stepper constructors for joint 1, 2 and 3.
The setup function begin serial comunication, execute the welcoming in serial monitor and set both kinds of motors.
The main loop has run functions for each stepper. You can't change these lines since steppers wont move at all

    joint1.run();
    joint2.run();
    joint3.run();

Main if statement executes what is inside as long as there is something on buffer 

    Serial.available()>0

Steppers movement work with character data received

    if(UserInput == 's')

Lines in each if or else if statement is basically the same

      steps1=steps1-200;
      joint1.moveTo(steps1);
      Serial.print("Moving Joint 1 -\n");
      Serial.print("Current Position: ");
      Serial.print(joint1.currentPosition());
      Serial.print("\n");

The step1 variable needs to be different for each articulation since it serves as reference for each steppers to move from a relative position. 

For servo controlling, the else if statements uses functions like:

    target_1 = 105;
      while(POS != target_1){
      if(POS < target_1){
        POS++;
      } else {
        POS--;
      }
    servo1.write(target_1);
    delay(25);
    servo1.write(90);
    }

It is basic servo controlling dealing with write() methods and POS variable incremente while servo nears target position. 

# Code Reference

You can check functions listed here:

    void open_clamp(int target_1);
  Open clamp according to a certaing angle. Change target_1 for a wider or less wide opening. Consider changing the code for 180 degress servo motors, this code involves POS variable with would make 180 servos go to 90 degrees position. 

    void close_clamp(int target_1);
  Close clamp with basically the same logic as open_clamp()
  
    void welcome_terminal();
  Welcoming in serial monitor. If you use Arduino integrated Serial Monitor you could see this messages which is very useful for testing purposes.
  
    void move_upwards(int target_2);
  Move second servo (wrist servo) upwards. Consider change this code if you have 180 degrees servo motors.
  
    void move_downwards(int target_2);
  Move second servo downwards.
  
    void abort();
  Disable outputs for all steppers. This function powers the whole body off. Consider the fact that once this function is executed the arm will "fade" 

# Libraries

Como se explica en el README de inicio, las liberias que debes tener instalados en tu IDE son:

 * [AccelStepper](https://github.com/swissbyte/AccelStepper)
 * [Serial UART](https://github.com/espressif/arduino-esp32/tree/2b15254d0b28329dc7af3fd8f9757e125e682660)

Se han barajeado algunas opciones sobre la libreria para el control de motores paso a paso, pero hasta ahora el unico que parece marcar un standar es la libreria AccelStepper. 

# Lib Docs

Deberias encontrar documentacion de las librierias usadas aqui:

 * [AccelStepper](https://www.airspayce.com/mikem/arduino/AccelStepper/)

 * [Serial (UART)](https://github.com/espressif/arduino-esp32/blob/2b15254d0b28329dc7af3fd8f9757e125e682660/docs/en/api/serial.rst)

