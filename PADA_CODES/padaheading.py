import math
from math import radians, cos, sin, asin, sqrt
import numpy as np
import time

dist = 0
angle = 0

def distance(lat1, lat2, lon1, lon2):
    lon2 = radians(lon2)
    lon1 = radians(lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    
    # Haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    a = sin(dlat / 2)*2 + cos(lat1) * cos(lat2) * sin(dlon / 2)*2
    c = 2 * asin(sqrt(a)) 
    r = 6400
    return(c * r)

def find_angle(height, dist):
        # Calculate the angle in radians
        angle_radians = math.atan(height / dist)
        
        # Convert radians to degrees 
        angle_degrees = math.degrees(angle_radians)
          
        return angle_degrees

def initialize (latitude, longitude, height):
        lat1 = 19.044356759382666 % 10000 #CRCE
        lon1 = 72.82036700137729 % 10000

        lat2 = latitude % 10000     # 19.04395680561915 #TAJ
        lon2 = longitude % 10000     # 72.8192707034145

        dist = distance(lat1, lat2, lon1, lon2) * 1000
        dist_f= dist * 3.28084
        print(f"Distance:\nMeters = {dist} m\nFeet = {dist_f} ft")
        print(f"Height = {height} m")
        # Hypotenuse
        hypo = sqrt(dist*2 + height*2)
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
        # Heading
        print(f"Heading = {headangle} {direction}\n")
        return headangle
