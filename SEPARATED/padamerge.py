from bmp388w import Alt, pressure
from padampu import roll, pitch, yaw
from gpstrials import latitude, longitude
from padaheading import initialize, dist, angle
from padaservo import servo
from padamotor import motor

while True:
    
    current_heading = initialize(latitude, longitude, Alt, pitch)
    # Calculate the desired heading for static
    desired_heading = 0 # using latitude and longitude of GPS once dropped take first heading direction and set it as desired heading

    heading_error = desired_heading-current_heading

    print(f"Height : {Alt} m")
    print(f"Pressure : {pressure}")
    print(f"Distance : {dist} m")
    print(f"Angle : {angle} deg")
    print(f"Current Heading : {current_heading}")
    print(f"\nHeading error: {heading_error} degrees\n")

    servo(heading_error)

    motor(pitch,Alt)