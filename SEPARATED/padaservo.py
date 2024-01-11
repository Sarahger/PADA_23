from gpiozero import Servo
from time import sleep
import os     #importing os library so as to communicate with the system
import pigpio #importing GPIO library

servo = Servo(12)  #GPIO pin

max_value = 1800 #FULL   #change this if your ESC's max value is different or leave it be
min_value = 1300 #(30%)  #change this if your ESC's min value is different or leave it be

def servo(heading_error):
        if (heading_error!=0):
                if(heading_error<0):
                        servo.max()
                        print("Servo 180")

                elif(heading_error>0):
                        servo.min()
                        print("Servo 0")

                else :
                        servo.mid()
                        print("Servo 90")
        
        time.sleep(0.1)