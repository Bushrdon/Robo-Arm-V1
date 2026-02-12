# Mechanical Structure

CAD models were taken from the project made by [Giulio Virtual World] (https://www.giulio-virtual-world.com/projects/projects/robotic-arm/), I strongly suggest you follow the exact same structure with the same hardware involving the arm. At the same time be aware PLA tends to melt under a long period of use so I suggest some strategy for dissipating heat in steppers since they can dilate the joint adaptations. You can consider utilizing another printing material like PETG for important parts since I noticed it gave better results. 

Also, if you are using a non-standard stepper of servo model, you will need to implement some adapatations since articulations will not be possible for a different size of steppers and servos. 

The amount of steppers needs a potency major than 24 Watts. Power supplies using 2A at 12v are not enough for the 5 steppers and I will inmediatly power off the power supply in that case. So I suggest using more current.
