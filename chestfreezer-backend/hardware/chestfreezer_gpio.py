'''
Created on Apr 2, 2014

Utilities and methods to control rapsbery's GPIO pins

@author: theoklitos
'''
import RPi.GPIO as GPIO
import sys
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

def output_pin(pin_number, state):
    """ will set the (boolean) state of the given pin_number # in GPIO.BOARD mode. Throws ValueError """
    GPIO.setup(int(pin_number), GPIO.OUT)    
    GPIO.output(int(pin_number), state)
    
def output_pin_for_time(pin_number, state, seconds):
    """ will set the (boolean) state of the given pin_number # in GPIO.BOARD mode. 
    After given seconds have passed, will flip the state around. Throws ValueError. """
    output_pin(pin_number, state)
    time.sleep(seconds)
    GPIO.output(int(pin_number), not state)   

def cleanup():
    """ will call the RPi.GPIO library to cleanup all the hardware pin_number states """
    GPIO.cleanup()

# this module can also be used for some quick GPIO pin_number testing
if __name__ == "__main__":    
    number_of_arguments = len(sys.argv) 
    if number_of_arguments == 1: #no args, check all pins
        for pin_number in range(1,27):
            output_pin_for_time(pin_number, True, 2)
    elif (number_of_arguments >= 1) & (number_of_arguments < 4): #correct args number
        pin_number = sys.argv[1]
        if sys.argv[2] in ['true', 'True', 'yes', 'Yes', 'on', 'On']:
            state = True
        elif sys.argv[2] in ['false', 'False', 'no', 'No', 'off', 'Off']:
            statte = False
        else:
            sys.exit('Boolean pin_number state ' + sys.argv[2] + ' not understood.')
                    
        if(number_of_arguments == 3):
            seconds = sys.argv[3]
            output_pin_for_time(pin_number, state, seconds)
        else:
            output_pin(pin_number, state)                
        cleanup()
    else:        
        sys.exit('Wrong number of parameters, format should be [pin_number] [state] followed by an optional [time]')    

