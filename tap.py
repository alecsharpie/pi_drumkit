import time
import board
import digitalio
import adafruit_lis3dh
i2c = board.I2C()
int1 = digitalio.DigitalInOut(board.D21)  # Set this to the correct pin for the interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
lis3dh.set_tap(1, 100)
while True:
    if lis3dh.tapped:
        print("Tapped!")
        time.sleep(0.01)

#while True:
#	time.sleep(0.5)
#	x, y, z = lis3dh.acceleration
#	print(x, y, z)
