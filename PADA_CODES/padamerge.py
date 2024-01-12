from bmp388w import Alt, pressure
from padampu import roll, pitch, yaw
from gpstrials import latitude, longitude
from padaheading import initialize, dist, angle
from padaservo import servo
from padamotor import motor
from green import green_zone
from signal import pada_drop
# from prop import prop_speed, land_speed

while True:
    
    if(Alt<=50):
        Altitude = True
    
    if green_zone and Altitude:
        pada_drop()
    
    # prop_speed() (within 0.5 sec)
        
    # if Alt<=5 :
    #     land_speed()

    current_heading = initialize(latitude, longitude, Alt, pitch)
    # Calculate the desired heading for static
    desired_heading = 0 # using latitude and longitude of GPS once dropped take first heading direction and set it as desired heading

    heading_error = desired_heading-current_heading
    
    servo(heading_error)

    motor(pitch,Alt)

    print(f"Height : {Alt} m")
    print(f"Pressure : {pressure}")
    print(f"Distance : {dist} m")
    print(f"Angle : {angle} deg")
    print(f"Current Heading : {current_heading}")
    print(f"\nHeading error: {heading_error} degrees\n")
