#include <AccelStepper.h>

// Used by testing Arduino Code in ESP32 WROOM Model in Proteus
// It can technically be run by a Arduino UNO if you follow the pin definitions below. 

#define JOINT1_1 9
#define JOINT1_2 8
#define JOINT1_3 7
#define JOINT1_4 6

#define JOINT2_1 5
#define JOINT2_2 4
#define JOINT2_3 3
#define JOINT2_4 2

#define JOINT3_1 1
#define JOINT3_2 0
#define JOINT3_3 14
#define JOINT3_4 15


AccelStepper joint1(8, JOINT1_1, JOINT1_3, JOINT1_2, JOINT1_4);
AccelStepper joint2(8, JOINT2_1, JOINT2_3, JOINT2_2, JOINT2_4);
AccelStepper joint3(8, JOINT2_1, JOINT2_3, JOINT2_2, JOINT2_4);

void setup()
{     
   joint1.setMaxSpeed(100);
   joint1.setSpeed(10);
   
   joint2.setMaxSpeed(100);
   joint2.setSpeed(10);
   
   joint3.setMaxSpeed(100);
   joint3.setSpeed(10);          
}

void loop() {  
  joint1.runSpeed();
  joint2.runSpeed();
  joint3.runSpeed();
}