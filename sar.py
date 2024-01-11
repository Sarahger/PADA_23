
# import math
# from math import radians, cos, sin, asin, sqrt
# import numpy as np
# import time
# import serial
# import pynmea2
# from gpiozero import Servo
# from time import sleep
# import os     #importing os library so as to communicate with the system
# import pigpio #importing GPIO library
# import board
# import adafruit_bmp3xx
# import sys
# import smbus
# from imusensor.MPU9250 import MPU9250

# address = 0x68
# bus = smbus.SMBus(1)
# imu = MPU9250.MPU9250(bus, address)
# imu.begin()

# os.system("sudo killall pigpiod")
# os.system ("sudo pigpiod") #Launching GPIO library

# time.sleep(1) # As i said it is too impatient and so if this delay is removed you will get an error

# ESC=13  #Connect the ESC in this GPIO pin 

# pi = pigpio.pi();
# pi.set_servo_pulsewidth(ESC, 0) 

# # I2C setup
# i2c = board.I2C()  # uses board.SCL and board.SDA
# # i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
# bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c,0x76)

# SPI setup
# from digitalio import DigitalInOut, Direction
# spi = board.SPI()
# cs = DigitalInOut(board.D5)
# bmp = adafruit_bmp3xx.BMP3XX_SPI(spi, cs)

# port = ("/dev/ttyAMA0")
# baud = 9600

# serialPort = serial.Serial(port,baudrate=baud,timeout=0.5)

# bmp.pressure_oversampling = 8
# bmp.temperature_oversampling = 2
# bmp.sea_level_pressure = 1013.25

# servo = Servo(12)  #GPIO pin

# max_value = 1800 #FULL   #change this if your ESC's max value is different or leave it be
# min_value = 1300 #(30%)  #change this if your ESC's min value is different or leave it be

# def distance(lat1, lat2, lon1, lon2):
#     lon2 = radians(lon2)
#     lon1 = radians(lon1)
#     lat1 = radians(lat1)
#     lat2 = radians(lat2)
    
#     # Haversine formula 
#     dlon = lon2 - lon1 
#     dlat = lat2 - lat1
#     a = sin(dlat / 2)*2 + cos(lat1) * cos(lat2) * sin(dlon / 2)*2
#     c = 2 * asin(sqrt(a)) 
#     r = 6400
#     return(c * r)

# def initialize (latitude, longitude, height, pitch):
#         lat1 = 19.044356759382666 % 10000 #CRCE
#         lon1 = 72.82036700137729 % 10000

#         lat2 = latitude % 10000     # 19.04395680561915 #TAJ
#         lon2 = longitude % 10000     # 72.8192707034145

#         dist = distance(lat1, lat2, lon1, lon2) * 1000
#         dist_f= dist * 3.28084
#         print(f"Distance:\nMeters = {dist} m\nFeet = {dist_f} ft")
#         print(f"Height = {height} m")
#         # Hypotenuse
#         hypo = sqrt(dist*2 + height*2)
#         print(f"Hyoptenuse =  {hypo} m\n" )

#         del_lon = (lon2-lon1)
#         X = math.cos(lat2) * math.sin(del_lon)
#         Y = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(del_lon)

#         heading_angle = math.atan2(X,Y)

#         headangle= math.degrees(heading_angle)

#         if headangle > -36 and headangle <= 36:
#                 direction = 'North'
#         elif headangle > 36 and headangle <= 72:
#                 direction = 'North East'
#         elif headangle > 72 and headangle <= 108:
#                 direction = "East"
#         elif headangle > 108 and headangle <= 144:
#                 direction = "South East"
#         elif headangle > 144 and headangle <= 180:
#                 direction = "South"
#         elif headangle > -144 and headangle <= -108:
#                 direction = "South West"
#         elif headangle > -108 and headangle <= -72:
#                 direction = "West"
#         elif headangle > -72 and headangle <= -36:
#                 direction = "North West"
#         elif headangle > -180 and headangle <= -144:
#                 direction = "South"

#         angle = find_angle(height, dist)
#         print(f"Angle (in Degrees) = {angle}\n")            
#         # Heading
#         print(f"Heading = {headangle} {direction}\n")

        # if (pitch!=angle):   #assuming angle below x-axis in fourth quadrant
        #         if (pitch<angle and pitch>angle-10):
        #                 pi.set_servo_pulsewidth(ESC,1500)
        #         elif (pitch<angle and pitch<angle-10):
        #                 pi.set_servo_pulsewidth(ESC,min_value)
        #         elif (pitch>angle and pitch<angle+10):
        #                 pi.set_servo_pulsewidth(ESC,1700)
        #         elif (pitch>angle and pitch>angle+10):
        #                 pi.set_servo_pulsewidth(ESC,max_value)
        #         else:
        #                 pi.set_servo_pulsewidth(ESC,1600)

        # if (height!=15) :
        #         if (height<15 and dist>=2):
        #                 pi.set_servo_pulsewidth(ESC,1700)
        #         elif (height>15 and dist<=200):
        #                 pi.set_servo_pulsewidth(ESC,1500)
        #         else:
        #                 pi.set_servo_pulsewidth(ESC,1600)

#         return headangle

# def find_angle(height, dist):
#         # Calculate the angle in radians
#         angle_radians = math.atan(height / dist)
        
#         # Convert radians to degrees 
#         angle_degrees = math.degrees(angle_radians)
          
#         return angle_degrees

#https://medium.com/@niru5/hands-on-with-rpi-and-mpu9250-part-3-232378fa6dbc
#https://learn.adafruit.com/adafruit-bmp388-bmp390-bmp3xx/python-circuitpython


# def stop(): #This will stop every action your Pi is performing for ESC ofcourse.
#         pi.set_servo_pulsewidth(ESC, 0)
#         pi.stop()

# def calibrate():   #This is the auto calibration procedure of a normal ESC
#         pi.set_servo_pulsewidth(ESC, 0)
#         print("Disconnect the battery and press Enter")
#         inp = input()
#         if inp == '':
#                 pi.set_servo_pulsewidth(ESC, max_value)
#                 print("Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
#                 inp = input()
#                 if inp == '':            
#                         pi.set_servo_pulsewidth(ESC, min_value)
#                         print ("Wierd eh! Special tone")
#                         time.sleep(7)
#                         print ("Wait for it ....")
#                         time.sleep (5)
#                         print ("Im working on it, DONT WORRY JUST WAIT.....")
#                         pi.set_servo_pulsewidth(ESC, 0)
#                         time.sleep(2)
#                         print ("Arming ESC now...")
#                         pi.set_servo_pulsewidth(ESC, min_value)
#                         time.sleep(1)
#                         print ("See.... uhhhhh")
#                         manual_drive() # You can change this to any other function you want

# def manual_drive(): #You will use this function to program your ESC if required
#         print ("Manual: give a value between 0 and you max value" )   
#         while True:
#                 inp = input()
#                 if inp == "x":
#                         stop()
#                         break
#                 else:
#                         pi.set_servo_pulsewidth(ESC,inp)

# while True:

#         # Example: Update latitude and longitude based on your aircraft's GPS data
#         calibrate()
#         imu.readSensor()
#         imu.computeOrientation()
#         height = bmp.altitude        #float(input("Enter height: "))
#         pitch = imu.pitch         #float(input("Enter pitch angle: "))
#         roll = imu.roll
#         yaw = imu.yaw
        # str = ''
        # try :
        #         str = serialPort.readline().decode().strip()
        # except Exception as e:
        #         print (e)
        #         # print (str)
        
        # if str.find('GGA') > 0:
        #         try :
        #                 msg = pynmea2.parse(str)
        #                 latitude = float(round(msg.latitude,6))
        #                 longitude = float(round(msg.longitude,6))
        #                 #print(msg.timestamp,'LAT : ',round(msg.latitude,6),'LON : ',round(msg.longitude,6), 'ALT : ',msg.altitude,'SATS : ',msg.num_sats)
        #         except Exception as e:
        #                 print (e)
        # current_heading = initialize(latitude, longitude, height, pitch)
        # # Calculate the desired heading
        # desired_heading = 0 # using latitude and longitude of GPS once dropped

        # heading_error = desired_heading-current_heading

        # print(f"\nHeading error: {heading_error} degrees\n")

        # if (heading_error!=0):
        #         if(heading_error<0):
        #                 servo.max()
        #                 print("Servo 180")

        #         elif(heading_error>0):
        #                 servo.min()
        #                 print("Servo 0")

        #         else :
        #                 servo.mid()
        #                 print("Servo 90")

        #if (roll!=0):
                #move rudders(?)

        # time.sleep(0.1)