import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
os.system("sudo killall pigpiod")
import pigpio #importing GPIO library

ESC=13
i=1014
pi = pigpio.pi()

def prop_speed():
    for i in range(1600):
            i+=10
            pi.set_servo_pulsewidth(ESC, i)
            time.sleep(0.04)