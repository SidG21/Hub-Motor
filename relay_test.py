import RPi.GPIO as GPIO #Importe la bibliothèque pour contrôler les GPIOs
import time

GPIO.setmode(GPIO.BOARD) #Définit le mode de numérotation (Board)
GPIO.setwarnings(False) #On désactive les messages d'alerte

relay_1 = 3 #pins defined for 8 relays
relay_2 = 5
relay_3 = 7
relay_4 = 11
relay_5 = 13
relay_6 = 15
relay_7 = 16
relay_8 = 18

GPIO.setup(relay_1, GPIO.OUT) #Active le contrôle du GPIO
GPIO.setup(relay_2, GPIO.OUT)
GPIO.setup(relay_3, GPIO.OUT)
GPIO.setup(relay_4, GPIO.OUT)
GPIO.setup(relay_5, GPIO.OUT)
GPIO.setup(relay_6, GPIO.OUT)
GPIO.setup(relay_7, GPIO.OUT)
GPIO.setup(relay_8, GPIO.OUT)

GPIO.output(relay_1, GPIO.LOW)
GPIO.output(relay_2, GPIO.LOW)
GPIO.output(relay_3, GPIO.LOW)
GPIO.output(relay_4, GPIO.LOW)
GPIO.output(relay_5, GPIO.HIGH)
GPIO.output(relay_6, GPIO.HIGH)
GPIO.output(relay_7, GPIO.HIGH)
GPIO.output(relay_8, GPIO.HIGH)

time.sleep(10)

GPIO.output(relay_1, GPIO.HIGH)
GPIO.output(relay_2, GPIO.HIGH)
GPIO.output(relay_3, GPIO.HIGH)
GPIO.output(relay_4, GPIO.HIGH)
GPIO.output(relay_5, GPIO.LOW)
GPIO.output(relay_6, GPIO.LOW)
GPIO.output(relay_7, GPIO.LOW)
GPIO.output(relay_8, GPIO.LOW)


