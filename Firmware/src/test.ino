#include <AccelStepper.h>
#include <Arduino.h>

// Used by testing Arduino Code in Arduino UNO R3 in Proteus
// It can technically be run by a Arduino UNO if you follow the pin definitions below. 


#define JOINT1_1 9
#define JOINT1_2 8
#define JOINT1_3 7
#define JOINT1_4 6

#define JOINT2_1 5
#define JOINT2_2 4
#define JOINT2_3 3
#define JOINT2_4 2

#define JOINT3_1 A0
#define JOINT3_2 A1
#define JOINT3_3 A2
#define JOINT3_4 A3


AccelStepper joint1(8, JOINT1_1, JOINT1_3, JOINT1_2, JOINT1_4); //Shoulder
AccelStepper joint2(8, JOINT2_1, JOINT2_3, JOINT2_2, JOINT2_4); //Elbow
AccelStepper joint3(8, JOINT3_1, JOINT3_3, JOINT3_2, JOINT3_4); //Wrist

void setup()
{     
   Serial.begin(9600);
   joint1.setMaxSpeed(100);
   joint1.setSpeed(10);
   
   joint2.setMaxSpeed(100);
   joint2.setSpeed(10);
   
   joint3.setMaxSpeed(100);
   joint3.setSpeed(10);          
}

void loop() {  

  if(Serial.available()>0){

    char UserInput = Serial.read();
    
    if(UserInput == 't'){
      joint1.moveTo(50);
      Serial.print("Received 1... Moving Joint 1 (50 steps)\n");
      joint1.run();
    } else if (UserInput == 's'){
      joint1.moveTo(-50);
      Serial.print("Received 2... Moving Joint 1 (-50 steps)\n");
      joint1.run();
    } else if (UserInput == 'e'){
      joint2.moveTo(50);
      Serial.print("Received 2... Moving Joint 2 (50 steps)\n");
      joint2.run();
    } else if (UserInput == 'r'){
      joint2.moveTo(-50);
      Serial.print("Received 2... Moving Joint 2 (-50 steps)\n");
      joint2.run();
    } else if (UserInput == 'q'){
      joint3.moveTo(50);
      Serial.print("Received 3... Moving Joint 3 (50 steps)\n");
      joint3.run();
    } else if (UserInput == 'w'){
      joint3.moveTo(-50);
      Serial.print("Received 2... Moving Joint 3 (-50 steps)\n");
      joint2.run();
    }
   } 
}