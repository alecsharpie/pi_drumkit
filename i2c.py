import time
import board
import digitalio
import adafruit_lis3dh
print(dir(board))
i2c = board.I2C()
print(i2c.scan())
int1 = digitalio.DigitalInOut(board.D21)  # Set this to the correct pin for the interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
while True:
	time.sleep(0.5)
	x, y, z = lis3dh.acceleration
	print(x, y, z)
