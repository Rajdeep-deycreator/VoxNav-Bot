## Voice-Controlled Autonomous Obstacle Detection Robot

## Project overview 

This Robot is a simple voice controlled robot basic surveillance robot that can be instructed through voice command and can navigate itself with integrated sensors.

It can be used for basic surveillance through its integrated sensors,cammeras,Hardware Control unit(Arduino UNO R3), Software control Unit (Raspberry pi 5) and motors for locomotion 

## Why I built this 

This Robot was originally built for a school exhibition project, later i decided to upgrade the infrastructure and functionalities by integrating more effective electronic components, Firmware and an upgraded software

## Robot prototype 

Below is the Prototype (exhibition version) of the robot

![Robot_Prototype](/images/Robot_Prototype.jpg)

## 3D Cad

the screenshots of 3D model of the Robot is attached below.

![cad_screenshot_1](/images/CADing_screenshot_1.jpg)

![cad_screenshot_2](/images/CADing_screenshot_2.jpg)

The complete ".step" is present in the "/CAD" directory in the root of the repo

## Wiring diagram 

The following attached image shows the wiring diagram of the system where the Hardware Control Unit(HCU) is integrated with the Software Control Unit (SCU) along with other electrical components 

![wiring_diagram](/images/schematic_circuit_diagram.jpg)

## System Architecture 

This Robot has an integrated architecture of the Hardware Control Unit (HCU) and Software Control Unit (SCU) along with other components. The architecture is explained below:

→ Software Control Unit (SCU): The Software Control Unit (SCU) is the Raspberry pi 5 board used to operate the Voice-Controled software  which has an integrated Chat bot system that allows users to take information from the robot based on the Data it is trained with. It is also used to form a secure connection with a digital device such as a Laptop or a mobile over a secure network for data transfer during servilance or Remote access. Main feature : fast processing of software and integration with an digital device for controling the robot

→ Hardware Control Unit (HCU): The Hardware Control Unit (HCU) is the Arduino UNO R3 that is used for maintaining the firmware,controlling the sensors and motors for locomotion,it is integrated with the Software Control Unit (SCU) Through USB over 'serial-comuication" so that the robot's hardware could be controlled by the software whether by Voice-Command system or Remote access

→L298N Motor Driver: The L298N Motor Driver is integrated With the Robots Firmware through the Hardware Control Unit (HCU). This controls the direction and speed of the motors of the Robot that is essential for its locomotion 

→ Servo Motors: Servo motors are used to control the movement of Arms,Elbows and head that makes it functionable like an actual Robot.It is integrated with the Robots firmware through the Hardware Control Unit (HCU)

→ Network : A wifi router is being used here to establish a secure connection with the Robot's Software Control Unit (SCU) and a monitoring device such as a laptop , Mobile phone,etc for data transfer during surveillance mode and Remote access of the Robot.

→ Sensors: Sensors Like Ultrasound sensor and Ir proximity sensor are used here for obstecal detection. These are controlled by the Hardware Control Unit (HCU)

→ Cammera : A day & Night vison cammera is used here for advanced obstecal detection and for capturing videos and pictures during Surveillance mode . This cammera is Integrated with the Software Control Unit (SCU)

## BOM (bill of material)


| Component | Why it's used | Unit Cost (USD) | Qty | Total Cost (USD) |
|-----------|---------------|-----------------|-----|------------------|
| Raspberry Pi 5 | The main computer that runs the robot software and processes voice commands. | 172.44 | 1 | 172.44 |
| Arduino UNO R3 | Handles hardware level control like reading sensors and driving motors. | 21.00 | 1 | 21.00 |
| Gear Motors | Provide movement by driving the robot wheels. | 2.06 | 4 | 8.24 |
| Servo Motors | Used to move mechanical parts like the cammera mount and other joints. | 2.17 | 5 | 10.85 |
| L298N Motor Driver | Allows the controller to control motor speed and direction safely. | 2.17 | 1 | 2.17 |
| Ultrasonic Sensor | Measures distance so the robot can detect obstacles in front. | 2.17 | 1 | 2.17 |
| IR Proximity Sensor | Helps detect nearby objects using infrared light. | 1.08 | 1 | 1.08 |
| Raspberry Pi Night Vision Cammera | Captures images and video so the robot can monitor surroundings even in low light. | 19.64 | 1 | 19.64 |
| Lithium Ion Cells | Provide battery power for the robot electronics. | 1.74 | 5 | 8.70 |
| Power Bank | Supplies portable power to the Raspberry Pi. | 18.50 | 1 | 18.50 |
| 512GB SD Card | Stores the operating system, robot software and recorded data. | 64.00 | 1 | 64.00 |
| Wireless WiFi Router | Enables the robot to connect to a wireless network for monitoring and control. | 12.00 | 1 | 12.00 |
| HDMI Cable | Used during setup to connect the Raspberry Pi to a monitor for configuration. | 15.24 | 1 | 15.24 |
| **Total Estimated Cost** |  |  |  | **356.03 USD** |

the total break down of the BOM is also available in the "bom.csv" file at the root of this repo

## Prototype Improvements

Since the original version of this robot was built for a school exhibition, the current version includes several improvements:

→ Improved voice command system  
→ Enhanced chatbot with updated training data  
→ Better software management and structure  
→ Improved power management and efficiency