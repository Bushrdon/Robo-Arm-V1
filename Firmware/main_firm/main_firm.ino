#include<Arduino.h>
#include<AccelStepper.h>

//****************************************************************

//NOTAS DE DESARROLLO

//****************************************************************

// Nota preliminar: la mayor parte de esta informacion migrara
// en algun punto al README.md del directorio de firmware
// por ahora vivira aqui como comentario del codigo.

//***************************************************************

//Este es el codigo que va a ejecutar el microcontrolador.
//La referencia de la libreria permite utilizar posiciones realiva
//de los motores lo que puede ayudar cuando se quiera implementar
//patrones de movimientos programados.

//****************************************************************
//****************************************************************

//Informacion dada en Class Reference para AccelStepper:

//AccelStepper() Constructor Documentation
//Constructor. You can have multiple simultaneous steppers, all
//moving at different speeds and accelerations, provided you call
//their run() functions at frequent enough intervals. Current
//position is set to 0, target position is set to 0. MaxSpeed and
//Acceleration default to 1.0. The motor pins will be initialised
//to OUTPUT mode during the constructor by a call to enableOutputs(). 

//Dice que se pueden tener multiples motores paso a paso en
//simultaneo ademas de poder hacerlos independientes en su
//movimientos.

//Muchas de las funciones de esta libreria tratan a las unidades
//espaciales como "steps" habria que comprobar empiricamente
//como de largo es un step a menos que encuentre algo que me de
//nocion de que tanto es un step

//****************************************************************
//****************************************************************

//     ---- Set Functions y Loop Functions ----

// Naturalemte las siguientes funciones se clasifican como:

// Para ejecutar una vez:

//     setMaxSpeed() => Establece la velocidad de movimiento maxima
//     permitida, esto dependera del procesador. El valor por de
//     fecto es 1 step por segundo

//     setAcceleration() => Establece la proporcion de aceleracion
//     (Es decir, la velocidad aumenta tantas veces cada tantos
//     segundos) Parametro: float > 0.0 obligatoriamente

//     moveTo() => Esta en presente en ejemplos basicos pero no
//     pillo la idea. Segun la referencia lo que hace es establecer
//     un posicion "target" (blanco, fijo). La funcion run tratara
//     siempre de mover el motor desde una poisicion inicial a
//     la posicion "target"

// Para ejecutar en bucle:

//    run() => Por lo que entiendo acciona el motor y devuelve "true"
//    hasta que el motor llega a la "target position", en la refe
//    rencia se recomienda llamar a esta funcion tan a menudo como
//    sea posible preferiblemente en el loop. Cada llamada de run()
//    hara al menos un "step"

//    distanceToGo() => En la referencia: "Returns: the distance..."
//    "from the current position to the target position in steps..."
//    "Positive is clockwise from the current position." Devuelve
//    la distancia que hay desde la poisicion actual hasta la posicion
//    "target" en steps. Tambien aclara que el valor es positivo a
//    partir del valor de la posicion actual.

//    currentPosition() => En la referencia: "Returns: the current..."
//    "motor position in steps. Positive is clockwise from the 0 position."
//    Devuelve la posicion actual del motor en steps. Aclara que se
//    cuenta positivo a partir de la posicion 0.

//****************************************************************
//****************************************************************

//                        --- Programa ---    

//****************************************************************
//****************************************************************

//Algunas definiciones


//Character definitions
//Consult main.py

constexpr char MOVE_JOINT1_UP = 'q'
constexpr char MOVE_JOINT1_DOWN = 'w'
constexpr char MOVE_JOINT2_UP = 'e'
constexpr char MOVE_JOINT2_DOWN = 'r'
constexpr char MOVE_JOINT3_RIGHT = 's'
constexpr char MOVE_JOINT3_LEFT = 't'


//Input del usuario

  char userInput;

//Los Steppers seran llamados como articulaciones (joints) y seran enumerados como lo dice el esquematico en Hardware/ 

  AccelStepper joint1(AccelStepper::FULL2WIRE, 33, 31); // Hay que terminar de confirmar el nombre de los pines en ESP32 Arduino-Core
  AccelStepper joint2(AccelStepper::FULL2WIRE, 30, 29);
  AccelStepper joint3(AccelStepper::FULL2WIRE, 28, 27);

  void setup() {
      Serial.begin(9600);

}

void loop() {
  
  if(Serial.available() > 0){ //Habilita la lectura de userInput solo cuando hay bits disponibles en el buffer de Rx
                              
          userInput = Serial.read();
          
          //En funcion del caracter recibido ejecutar la accion correspondiente (una cadena de if else me parece mas apropiado que switch case)

          if (userInput == MOVE_JOINT1_UP){

	    while(userInput == MOVE_JOINT1_UP);
              joint1.foo(); //Especifica la accion que se quiera hacer.
                            //Lo que se quiere: Que un motor rote siempre que el boton
                            //en la GUI este pulsado pero solo hasta cierto limite.
                                
          } else if(userInput == MOVE_JOINT1_DOWN){

	    while(userInput == MOVE_JOINT1_DOWN)              
              joint1.run(); // Statement para movimiento hacia abajo del joint1
              
          } else if(userInput == MOVE_JOINT2_UP){

	    while(userInput == MOVE_JOINT2_UP);
              
              // Statement para movimiento hacia arriba del joint2
              
          } else if(userInput == MOVE_JOINT2_DOWN){

	    while(userInput == MOVE_JOINT2_DOWN);
	    
              // Statement para movimiento hacia abajo del joint2
              
          } else if(userInput == MOVE_JOINT3_RIGHT){

	    while(userInput == MOVE_JOINT3_RIGHT);
	    
              // Statement para movimiento hacia la derecha del joint3
              
          } else if(userInpur == MOVE_JOINT3_LEFT){

	    while(userInput == MOVE_JOINT3_LEFT);
	    
              // Statement para movimiento hacia la izquierda del joint3
              
          }
  }
}


