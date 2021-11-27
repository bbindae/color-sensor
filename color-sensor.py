import RPi.GPIO as GPIO
import time
import board
import adafruit_tcs34725


button = 15

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
# Set pin 10 to be an input and set initial value to be pulled low (off)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# create sensor object
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)



try:
	while True:
		if GPIO.input(button) == GPIO.HIGH:  # Read button state
			print("Button was pushed!")
			print("Start reading RGB color")
			color = sensor.color
			color_rgb = sensor.color_rgb_bytes
			print(
			"RGB color as 8 bits per channel int: #{0:02X} or as 3-tuple: {1}".format(
			color, color_rgb
			)
			)
			
			time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()


	
	
