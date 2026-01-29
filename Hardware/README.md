# Part List

Debes tener a la mano los siguientes **componentes**:

1. **ESP32**
2. **ULN2003A (x3)**
3. **Unipolar Stepper 24BYJ48-BJ (x3)**

# Scheme

	Still working on it

# Parts Specs

Especificaciones y comentarios referentes a los componentes del proyecto.

## ESP32 [(Datasheet)](https://cdn.sparkfun.com/datasheets/IoT/esp32_datasheet_en.pdf)

<img src='img/esp32.jpg'>

*descripcion del componente*

El sistema esta pensado para ser usado en conjunto con una computadora que corra el software con la interfaz de usuario. Dado que el metodo de comunicacion entre el microcontrolador y la computadora es por medio Serial UART, se entiende que el microcontrolador ya dispondria de una fuente de alimentacion por lo que esta no sera necesario a la hora de la aplicacion.  

Mas adelante se dara a entender que es necesario hacer uso de los pines de salida de voltaje integrados en el esp32 para fines de alimentacion.

Hasta donde se tiene contemplado las conexiones de este componente solo involucran 2x3 = 6 GPIOS arbitrarios que irian a los pines de cada driver para cada motor. 

## ULN2003A [(Datasheet)](https://www.alldatasheet.com/datasheet-pdf/view/25566/STMICROELECTRONICS/ULN2003A.html)

<img src='img/uln2003a.jpg'>

*descripcion del componete*

Este es un modulo muy simple que integra un arreglo de siete transistores en configuracion darlington. Su uso no envuelve mas que conectar a una fuente con los valores nominales del motor y cada canal del integrado conectarlo a un pin de motor unipolar.

Para mas informacion consultar con el esquema en [schemes](https://github.com/Bushrdon/Robo-Arm-V1/blob/master/Hardware/schemes/scheme_1.pdf)


## Unipolar Stepper [(Datasheet)](https://d25vv4z8gtre3w.cloudfront.net/fajlcsatolas/24BYJ48_28BYJ48_30BYJ46%20l%C3%A9ptet%C5%91%20motor.pdf)

<img src='img/stepper.jpg'>

Este es un motor paso a paso unipolar cuyas conexiones se puede consultar [aqui](https://github.com/Bushrdon/Robo-Arm-V1/blob/master/Hardware/schemes/scheme_1.pdf)
