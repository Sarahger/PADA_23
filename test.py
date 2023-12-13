import math
from math import radians, cos, sin, asin, sqrt
import numpy as np
import time

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient 
os.system ("sudo pigpiod") #Launching GPIO library
time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio #importing GPIO library

ESC=13  #Connect the ESC in this GPIO pin 

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0) 

max_value = 1500 #change this if your ESC's max value is different or leave it be
min_value = 1015  #change this if your ESC's min value is different or leave it be

height = 15  #keeping constant for now will change later according to value from bmp

def distance(lat1, lat2, lon1, lon2):
	
		lon1 = radians(lon1)
		lon2 = radians(lon2)
		lat1 = radians(lat1)
		lat2 = radians(lat2)
	
		# Haversine formula 
		dlon = lon2 - lon1 
		dlat = lat2 - lat1
		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2

		c = 2 * asin(sqrt(a)) 
		
		r = 6400
		
		return(c * r)

def initialize (latitude, longitude):
        lat1 = 19.044356759382666 % 10000 #CRCE
        lon1 = 72.82036700137729 % 10000

        lat2 = latitude % 10000     # 19.04395680561915 #TAJ
        lon2 = longitude % 10000     # 72.8192707034145

        dist = distance(lat1, lat2, lon1, lon2) * 1000
        dist_f= dist * 3.28084
        print(f"Distance:\nMeters = {dist} m\nFeet = {dist_f} ft")
        print(f"Height = {height} m")
        # Hypotenuse
        hypo = sqrt(dist**2 + height**2)
        print(f"Hyoptenuse =  {hypo} m\n" )

        del_lon = (lon2-lon1)
        X = math.cos(lat2) * math.sin(del_lon)
        Y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(del_lon)

        heading_angle = math.atan2(X,Y)

        headangle= math.degrees(heading_angle)

        if headangle > -36 and headangle <= 36:
                direction = 'North'
        elif headangle > 36 and headangle <= 72:
                direction = 'North East'
        elif headangle > 72 and headangle <= 108:
                direction = "East"
        elif headangle > 108 and headangle <= 144:
                direction = "South East"
        elif headangle > 144 and headangle <= 180:
                direction = "South"
        elif headangle > -144 and headangle <= -108:
                direction = "South West"
        elif headangle > -108 and headangle <= -72:
                direction = "West"
        elif headangle > -72 and headangle <= -36:
                direction = "North West"
        elif headangle > -180 and headangle <= -144:
                direction = "South"

        angle = find_angle(height, dist)
        print(f"Angle (in Degrees) = {angle}\n")

        pitch = float(input("Enter pitch angle: "))

        if (pitch!=angle):   #assuming angle below x-axis in fourth quadrant
                if (pitch<angle and pitch>angle-10):
                        pi.set_servo_pulsewidth(ESC,1125)
                elif (pitch<angle and pitch<angle-10):
                        pi.set_servo_pulsewidth(ESC,min_value)
                elif (pitch>angle and pitch<angle+10):
                        pi.set_servo_pulsewidth(ESC,1325)
                elif (pitch>angle and pitch>angle+10):
                        pi.set_servo_pulsewidth(ESC,max_value)
                else:
                        pi.set_servo_pulsewidth(ESC,1250)

        if (height!=15) :
                if (height<15 and dist>=2):
                        pi.set_servo_pulsewidth(ESC,max_value)
                elif (height>15 and dist<=200):
                        pi.set_servo_pulsewidth(ESC,min_value)
                else:
                        pi.set_servo_pulsewidth(ESC,1250)


        # Heading
        print(f"Heading = {headangle} {direction}\n")

        return headangle

def find_angle(height, dist):
		# Calculate the angle in radians
		angle_radians = math.atan(height / dist)
		
		# Convert radians to degrees 
		angle_degrees = math.degrees(angle_radians)
		
		return angle_degrees

def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
        pi.set_servo_pulsewidth(ESC, 0)
        pi.stop()

def calibrate():   #This is the auto calibration procedure of a normal ESC
        pi.set_servo_pulsewidth(ESC, 0)
        print("Disconnect the battery and press Enter")
        inp = input()
        if inp == '':
                pi.set_servo_pulsewidth(ESC, max_value)
                print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
                inp = input()
                if inp == '':            
                        pi.set_servo_pulsewidth(ESC, min_value)
                        print ("Wierd eh! Special tone")
                        time.sleep(7)
                        print ("Wait for it ....")
                        time.sleep (5)
                        print ("Im working on it, DONT WORRY JUST WAIT.....")
                        pi.set_servo_pulsewidth(ESC, 0)
                        time.sleep(2)
                        print ("Arming ESC now...")
                        pi.set_servo_pulsewidth(ESC, min_value)
                        time.sleep(1)
                        print ("See.... uhhhhh")
                        manual_drive() # You can change this to any other function you want

def manual_drive(): #You will use this function to program your ESC if required
        print ("Manual: give a value between 0 and you max value" )   
        while True:
                inp = input()
                if inp == "stop":
                        stop()
                        break
                else:
                        pi.set_servo_pulsewidth(ESC,inp)

while True:

        # Example: Update latitude and longitude based on your aircraft's GPS data
        latitude = float(input("Enter latitude: "))  # Replace with your aircraft's latitude
        longitude = float(input("Enter longitude: "))  # Replace with your aircraft's longitude
        current_heading = initialize(latitude, longitude)
        # Calculate the desired heading
        desired_heading = 90 # using latitude and longitude of GPS once dropped

        heading_error = desired_heading-current_heading;

        print(f"\nHeading error: {heading_error} degrees\n")

        if (heading_error!=0):
                if(heading_error<0):
                        yaw = 180
                        #set servo angle = yaw
                        print("Servo 180")

                if(heading_error>0):
                        yaw = 0
                        #set servo angle = yaw
                        print("Servo 0")
        
        #if (roll!=0):
                #move rudders(?)

