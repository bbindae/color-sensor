import RPi.GPIO as GPIO
import time
import board
import adafruit_tcs34725

def convert_to_gray_scale(r, g, b):
	''' converting r g b color value to gray scale '''
	return r*0.2126 + g*0.7152 + b*0.0722
	
button = 15

GPIO.setwarnings(False)  # Ignore warning for now
GPIO.setmode(GPIO.BCM)  # Use physical pin numbering
# Set pin 10 to be an input and set initial value to be pulled low (off)
GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# create sensor object
i2c = board.I2C()
sensor = adafruit_tcs34725.TCS34725(i2c)
#sensor.integration_time = 240



try:
	while True:
		if GPIO.input(button) == GPIO.HIGH:  # Read button state
			#print("Button was pushed!")
			print("---------Start detecting Ink level------------")
			print("Start reading RGB color")
			color = sensor.color
			color_rgb = sensor.color_rgb_bytes
			
			# Read RGB color and print
			print("RGB color as 8 bits per channel int: #{0:02X}".format(color))
			print("RGB: {0}".format(color_rgb))			
			print("")
			# Convert RGB to GrayScale to check the ink level easier
			print("Converting RGB to Grayscale (0 - 255)")
			gray_scale = convert_to_gray_scale(color_rgb[0], color_rgb[1], color_rgb[2])
			
			print("Gray Scale Value: " + str(gray_scale))
			if gray_scale < 10.0:
				print("More than 1/2 ink remaining.")
			else:
				print("Less than 1/2 ink remaining! Consider replacing the ink.")
			print("---------Ink level detection is done-------------")
			print("")
			print("")
			print("")
			
			
			time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()



	

	

