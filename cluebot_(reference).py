from time import sleep
import RPi.GPIO as GPIO       ## Import GPIO library
GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)      
GPIO.setup(5, GPIO.OUT)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)      
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)


def forward():
    print("Moving Forward")
#     DRIVER 1
    GPIO.output(3,True)
    GPIO.output(5,True)
    GPIO.output(7,True)
    GPIO.output(11,True)
#     DRIVER 2
    GPIO.output(16,True)
    GPIO.output(18,True)
    GPIO.output(22,True)
    GPIO.output(24,True)
    
    

    
def backward():
    print("Moving backward")
#     DRIVER 3
    GPIO.output(26,True)
    GPIO.output(32,True)
    GPIO.output(36,True)
    GPIO.output(38,True)
#     DRIVER 4
    GPIO.output(29,True)
    GPIO.output(31,True)
    GPIO.output(33,True)
    GPIO.output(35,True)
    
    
forward()
sleep(50)

GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.OUT)      
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(29, GPIO.OUT)      
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
GPIO.setup(35, GPIO.OUT)



backward()
sleep(50)

GPIO.cleanup()