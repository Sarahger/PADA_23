import math
import smbus
from imusensor.MPU9250 import MPU9250

address = 0x68
bus = smbus.SMBus(1)
IMU = MPU9250.MPU9250(bus, address)
IMU.begin()

heading_m = (math.atan2(IMU.getMagY_uT(), IMU.getMagX_uT()) * 180) / math.pi
print(f"Heading :{heading_m}")