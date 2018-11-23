import RPi.GPIO as GPIO
import time
LedPin1 = 11    # pin11
LedPin2 = 13    # pin13
LedPin3 = 14    # pin14

def setup():
  GPIO.setmode(GPIO.BOARD)  
     
  GPIO.setup(LedPin, GPIO.OUT)    # First Led 
  GPIO.output(LedPin, GPIO.HIGH) 

  GPIO.setup(LedPin2, GPIO.OUT)   # Second LED
  GPIO.output(LedPin2, GPIO.HIGH)

  GPIO.setup(LedPin3, GPIO.OUT)   # Third LED
  GPIO.output(LedPin3, GPIO.HIGH)
def blink():
  while True:
    GPIO.output(LedPin, GPIO.HIGH)  # led1 on
    GPIO.output(LedPin2, GPIO.HIGH)  # led2 on
    GPIO.output(LedPin3, GPIO.HIGH)  # led3 on
    time.sleep(1)
    GPIO.output(LedPin, GPIO.LOW) # led off
     GPIO.output(LedPin2, GPIO.LOW)  # led2 off
    GPIO.output(LedPin3, GPIO.LOW)  # led3 off
    time.sleep(1)
def destroy():
  GPIO.output(LedPin, GPIO.LOW)   
  GPIO.output(LedPin2, GPIO.LOW)  
  GPIO.output(LedPin3, GPIO.LOW) 
  
  GPIO.cleanup()                  # Release resource
if __name__ == '__main__':     # Program start from here
  setup()
  try:
    blink()
  except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
    destroy()