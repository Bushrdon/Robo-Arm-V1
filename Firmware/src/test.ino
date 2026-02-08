#include <AccelStepper.h>
#include <Arduino.h>
#include <Servo.h>

// Arduino Test Code

//Steppers 

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

//Servos

#define PINZA_1 A4
#define JOINT4 A5

Servo servo1; // Clamp
Servo joint4; //4th Joint

//Variables

int steps1 = 200;
int steps2 = 200;
int steps3 = 200;

int POS = 90;
//Functions

void open_clamp(int target_1);
void close_clamp(int target_1);

void setup()
{     
   Serial.begin(9600);

   monitor_welcome();

   joint1.setMaxSpeed(800);
   joint1.setAcceleration(300);
   
   joint2.setMaxSpeed(800);
   joint2.setAcceleration(300);
   
   joint3.setMaxSpeed(800);
   joint3.setAcceleration(300);

   servo1.write(POS);
   joint4.write(POS);
   servo1.attach(PINZA_1);          
   joint4.attach(JOINT4);
}

void loop() {   
  
  joint2.run();
  joint1.run();
  joint3.run();
  
  if(Serial.available()>0){
    int target_1 = POS;
    int target_2 = POS;
    char UserInput = Serial.read();

    if(UserInput == 's'){
      if (steps1>800){
        steps1=800;
      } else
        steps1+=200;
      joint1.moveTo(steps1);
      Serial.print("Moving Joint 1 +\n");
      Serial.print("Current Position: ");
      Serial.print(joint1.currentPosition());
      Serial.print("\n");

    } else if (UserInput == 't'){
      if (steps1>800){
        steps1=800;
      } else
        steps1+=200;
      joint1.moveTo(-steps1);
      Serial.print("Moving Joint 1 -\n");
      Serial.print("Current Position: ");
      Serial.print(joint1.currentPosition());
      Serial.print("\n");

    } else if (UserInput == 'e'){
      if (steps2>800){
        steps2=800;
      } else
        steps2+=200;
      joint2.moveTo(steps2);
      Serial.print("Moving Joint 2 +\n");
      Serial.print("Current Position: ");
      Serial.print(joint2.currentPosition());
      Serial.print("\n");

    } else if (UserInput == 'r'){
      if (steps2>800){
        steps2=800;
      } else
        steps2+=200;
      joint2.moveTo(-steps2);
      Serial.print("Moving Joint 2 +\n");
      Serial.print("Current Position: ");
      Serial.print(joint2.currentPosition());
      Serial.print("\n");

    } else if (UserInput == 'q'){
      if (steps3>800){
        steps3=800;
      } else
        steps3+=200;
      joint3.moveTo(steps3);
      Serial.print("Moving Joint 3 +\n");
      Serial.print("Current Position: ");
      Serial.print(joint3.currentPosition());
      Serial.print("\n");

    } else if (UserInput == 'w'){
      if (steps3>800){
        steps3=800;
      } else
        steps3+=200;
      joint3.moveTo(-steps3);
      Serial.print("Moving Joint 3 +\n");
      Serial.print("Current Position: ");
      Serial.print(joint3.currentPosition());
      Serial.print("\n");

    } else if(UserInput == 'a'){
      Serial.print("Opening Clamp \n");
      open_clamp(target_1);
    } else if(UserInput == 'm'){
      Serial.print("Closing Clamp \n");
      close_clamp( target_1);
    } else if(UserInput == 'o'){
      Serial.print("Elevating Clamp\n");
      move_upwards (target_2);
    } else if (UserInput == 'p'){
      Serial.print("Descending Clamp\n");
      move_downwards(target_2);
    } else if (UserInput == 'l') {
      abort();
      Serial.print("Proceso Abortado\n");
    }
   }
}

void open_clamp(int target_1){
      target_1 = 110;
      while(POS != target_1){
      if(POS < target_1){
        POS++;
      } else {
        POS--;
      }
    servo1.write(target_1);
    delay(20);
    servo1.write(90);
    }
}

void close_clamp(int target_1){
      target_1 = 70;
      while(POS != target_1){
      if(POS < target_1){
        POS++;
      } else {
        POS--;
      }
    servo1.write(target_1);
    delay(20);
    servo1.write(90);
    }
}

void move_upwards(int target_2){
  target_2 = 110;
  while(POS != target_2){
    if(POS < target_2){
      POS++;
    } else {
      POS--;
    }
  joint4.write(target_2);
  delay(20);
  joint4.write(90);
  }
}

void move_downwards(int target_2){
  target_2 = 70;
  while(POS != target_2){
    if(POS < target_2){
      POS++;
    } else {
      POS--;
    }
  joint4.write(target_2);
  delay(20);
  joint4.write(90);
  }
}

void abort(){
  joint1.stop();
  joint2.stop();
  joint3.stop();
}

void monitor_welcome(){
  Serial.print("/***************************************/\n");
  Serial.print("This is a Serial Monitor 4-DOF Robotic Arm\n");
  Serial.print("/***************************************/\n");
  Serial.print("\n");
  Serial.print("Joint 1 Current Position: \n");
  Serial.print(joint1.currentPosition());
  Serial.print("\n");
  Serial.print("Joint 2 Current Position: \n");
  Serial.print(joint2.currentPosition());
  Serial.print("\n");
  Serial.print("Joint 3 Current Position: \n");
  Serial.print(joint3.currentPosition());
  Serial.print("\n");
  Serial.print("/***************************************/\n");
}