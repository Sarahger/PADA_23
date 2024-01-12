import RPi.GPIO as GPIO
import time

GPIO_PIN = 16

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIO_PIN, GPIO.OUT)

def pada_drop():
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
