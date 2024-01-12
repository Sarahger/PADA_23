import time
import board
import adafruit_bmp3xx
from pada_calib import calibrate_bmp_sensor

# I2C setup
i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)

# SPI setup
# from digitalio import DigitalInOut, Direction
# spi = board.SPI()
# cs = DigitalInOut(board.D5)
# bmp = adafruit_bmp3xx.BMP3XX_SPI(spi, cs)

bmp.pressure_oversampling = 8
bmp.temperature_oversampling = 2
bmp.sea_level_pressure = calibrate_bmp_sensor(bmp) #1010.5419

while True:
    # print(
    #     "Pressure: {:6.4f}  Temperature: {:5.2f}".format(bmp.pressure, bmp.temperature)
    # )
    pressure = bmp.pressure
    Alt = bmp.altitude
    # print('Altitude: {} meters'.format(bmp.altitude))
    time.sleep(1)
