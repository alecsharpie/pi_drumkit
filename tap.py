from pyglet import media
import board
import digitalio
import adafruit_lis3dh
# setup accelerometer
i2c = board.I2C()
int1 = digitalio.DigitalInOut(board.D6)  # Sets input pin on board (BCM=6)
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, int1=int1)
lis3dh.set_tap(1, 90) # single tap & sensitivity
#setup music
sound = media.StaticSource(media.load('sounds/short-kick-low-jazz-single.wav'))
print('Drum on!')
while True:
	if lis3dh.tapped:
		sound.play()
