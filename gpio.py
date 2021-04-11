import RPi.GPIO as GPIO
import time
from time import sleep
import urllib.request
import urllib.parse

GPIO.setmode(GPIO.BCM)
PIR_PIN = 17
GPIO.setup(PIR_PIN, GPIO.IN)

try:
	print("PIR Module Test (CTRL+C to exit)")
	time.sleep(2)
	print("Ready")
	while True:
		if GPIO.input(PIR_PIN):
			print("Motion Detected!")

			url = 'http://192.168.1.3:3000/audio?firstname=tony&lastname=toon'
			f = urllib.request.urlopen(url)
			print(f.read().decode('utf-8'))
			
		time.sleep(1)

except KeyboardInterrupt:
	print("Quit")
	GPIO.cleanup()