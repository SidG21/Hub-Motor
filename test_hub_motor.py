import RPi.GPIO as GPIO
from time import sleep
import time
motorpin_left = 37
motorpin_right = 35
relay_1 = 3 #Définit le numéro du port GPIO qui alimente la relay_1
relay_2 = 5
relay_3 = 7
relay_4 = 11
relay_5 = 13
relay_6 = 15
relay_7 = 16
relay_8 = 18
# PWM pin connected to LED
GPIO.setwarnings(False)         #disable warnings
GPIO.setmode(GPIO.BOARD)
GPIO.setup(relay_1,GPIO.OUT)
GPIO.setup(relay_2,GPIO.OUT)
GPIO.setup(relay_3, GPIO.OUT)
GPIO.setup(relay_4, GPIO.OUT)
GPIO.setup(relay_5, GPIO.OUT)
GPIO.setup(relay_6, GPIO.OUT)
GPIO.setup(relay_7, GPIO.OUT)
GPIO.setup(relay_8, GPIO.OUT)
#set pin numbering system
GPIO.setup(motorpin_left,GPIO.OUT)
GPIO.setup(motorpin_right,GPIO.OUT)
pwm_left = GPIO.PWM(motorpin_left,100)
pwm_right = GPIO.PWM(motorpin_right,100)#create PWM instance with frequency
pwm_left.start(50)#start PWM of required Duty Cycle 
pwm_right.start(50)#pi_pwm.ChangeDutyCycle(70)
speed_value=60
stop_speed=0

def forward():
    print("forward")
    GPIO.output(relay_1, GPIO.LOW)
    GPIO.output(relay_2, GPIO.LOW)
    GPIO.output(relay_3, GPIO.LOW)
    GPIO.output(relay_4, GPIO.LOW)
    GPIO.output(relay_5, GPIO.HIGH)
    GPIO.output(relay_6, GPIO.HIGH)
    GPIO.output(relay_7, GPIO.HIGH)
    GPIO.output(relay_8, GPIO.HIGH)

    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)
    
    
def reverse():
    print("reverse")
    GPIO.output(relay_1, GPIO.HIGH)
    GPIO.output(relay_2, GPIO.HIGH)
    GPIO.output(relay_3, GPIO.HIGH)
    GPIO.output(relay_4, GPIO.HIGH)
    GPIO.output(relay_5, GPIO.LOW)
    GPIO.output(relay_6, GPIO.LOW)
    GPIO.output(relay_7, GPIO.LOW)
    GPIO.output(relay_8, GPIO.LOW)

    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(speed_value)
    
    
    

def left():
    print("left")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(speed_value)

def right():
    print("right")
    pwm_left.ChangeDutyCycle(speed_value)
    pwm_right.ChangeDutyCycle(stop_speed)

def stop():
    print("stop")
    pwm_left.ChangeDutyCycle(stop_speed)
    pwm_right.ChangeDutyCycle(stop_speed)
 
if __name__ == "__main__":
    delay=5
    print("hello")
      
    forward()
    time.sleep(5)
    reverse()
    time.sleep(delay)
    stop()
    print("hello")
    
    
    
    
"""
for i in range(50,100, 5):
    pwm_left.ChangeDutyCycle(i)
    pwm_right.ChangeDutyCycle(i)
    print("speed is",i)
    sleep(10)
                            
   
   



# 
    
    #for duty in range(100,-1,-1):
        #pi_pwm.ChangeDutyCycle(duty)
        #sleep(0.01)
    #sleep(0.1)
"""