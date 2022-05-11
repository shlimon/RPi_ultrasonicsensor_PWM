import RPi.GPIO as GPIO
import time
import sys

TRIG=21
ECHO=20
GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.OUT)

led = GPIO.PWM(4,400)

def distance():
    GPIO.setup(TRIG,GPIO.OUT) #set Trigger as output
    GPIO.setup(ECHO,GPIO.IN)  #set Echo as Input
    
    GPIO.output(TRIG,False)  #intially the triger is off
    time.sleep(0.2)
    
    GPIO.output(TRIG,True) #turn the trigger on 
    time.sleep(0.00001)
    GPIO.output(TRIG,False) #turn off trigger
    
    while GPIO.input(ECHO)==0:   #take reading of time sonic wave sent
        pulse_start=time.time()
    while GPIO.input(ECHO)==1: #take reading of time when sonic wave returns
        pulse_end=time.time()
    
    pulse_duration=pulse_end-pulse_start  # get duration
    
    cal_distance=(pulse_duration/2) *343 *100 #calculate in cm
    cal_distance=round(cal_distance,2)
    return cal_distance



    
try:
    while True:
        print(distance())
        
        if distance() > 0 and distance() < 4:
            led.start(90)
        elif distance()>4 and distance()<9:
            led.ChangeDutyCycle(40)
        elif distance()>9 and distance()<15:
            led.ChangeDutyCycle(10)
        else:
            led.ChangeDutyCycle(5)
            
except keyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)
        
        
    
    
    
    
    
    
    
