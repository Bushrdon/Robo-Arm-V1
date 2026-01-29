#include <AccelStepper.h>

// Embedded Code used in phyisical ESP32 board
// Need to be sure on pin definitions for ESP32 GPIOS yet.

#define JOINT1_1 13
#define JOINT1_2 14
#define JOINT1_3 27
#define JOINT1_4 26

#define JOINT2_1 25
#define JOINT2_2 33
#define JOINT2_3 32
#define JOINT2_4 18

#define JOINT3_1 19
#define JOINT3_2 21
#define JOINT3_3 22
#define JOINT3_4 23


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