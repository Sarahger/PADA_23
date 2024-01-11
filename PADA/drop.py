from PADA.signal import GPIO,GPIO_PIN,time
from PADA.bmp388w import Alt
from PADA.green import green_zone

print(f"Altitude : {Alt}")
if(Alt<=50):
    Altitude = True

if green_zone and Altitude:
    try:
        #Taking rising edge as drop signal
            # GPIO.output(GPIO_PIN, GPIO.LOW)
            # print("Low signal sent to arduino")
            # time.sleep(2)
            GPIO.output(GPIO_PIN, GPIO.HIGH)
            print("High signal sent to arduino")
            time.sleep(2)

    finally:
         GPIO.cleanup()
