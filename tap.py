import pyglet
import time
import board
import digitalio
import adafruit_lis3dh
# setup accelerometer
i2c = board.I2C()
int1 = digitalio.DigitalInOut(board.D21)  # Set this to the correct pin for the interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
lis3dh.set_tap(1, 90)
#setup music
sound = pyglet.resource.media('sounds/short-kick-low-jazz-single.wav', streaming=False)
print('Drum on!')
while True:
	if lis3dh.tapped:
		sound.play()
