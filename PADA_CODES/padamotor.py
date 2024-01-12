import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
os.system("sudo killall pigpiod")
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library
from padaheading import angle,dist

ESC=13  #Connect the ESC in this GPIO pin 

max_value = 1800 #FULL   #change this if your ESC's max value is different or leave it be
min_value = 1015 #(30%)  #change this if your ESC's min value is different or leave it be

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
        pi.set_servo_pulsewidth(ESC, 0)
        pi.stop()

def motor(pitch,height):
        
        if (pitch!=angle):   #assuming angle below x-axis in fourth quadrant
                if (pitch<angle and pitch>angle-10):
                        pi.set_servo_pulsewidth(ESC,1500)
                elif (pitch<angle and pitch<angle-10):
                        pi.set_servo_pulsewidth(ESC,min_value)
                elif (pitch>angle and pitch<angle+10):
                        pi.set_servo_pulsewidth(ESC,1700)
                elif (pitch>angle and pitch>angle+10):
                        pi.set_servo_pulsewidth(ESC,max_value)
                else:
                        pi.set_servo_pulsewidth(ESC,1600)

        if (height!=15) :
                if (height<15 and dist>=2):
                        pi.set_servo_pulsewidth(ESC,1700)
                elif (height>15 and dist<=200):
                        pi.set_servo_pulsewidth(ESC,1500)
                else:
                        pi.set_servo_pulsewidth(ESC,1600)

        # if pitch < angle - 10:
        #         pi.set_servo_pulsewidth(ESC, min_value)
        # elif pitch > angle + 10:
        #         pi.set_servo_pulsewidth(ESC, max_value)
        # else:
        #         pi.set_servo_pulsewidth(ESC, 1600)

        # # Additional height-based servo control
        # if height < 15 and dist >= 2:
        #         pi.set_servo_pulsewidth(ESC, 1700)
        # elif height > 15 and dist <= 200:
        #         pi.set_servo_pulsewidth(ESC, 1500)
        # else:
        #         pi.set_servo_pulsewidth(ESC, 1600)
