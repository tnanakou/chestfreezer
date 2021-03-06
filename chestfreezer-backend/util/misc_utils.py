'''
Created on Apr 2, 2014

Various miscellaneous utils 

@author: theoklitos
'''
import os
import sys    
import termios
import fcntl
import datetime

def get_single_char():
    """ waits for user input and immediately reads the first char without waiting for a newline. 
    Found at: http://love-python.blogspot.de/2010/03/getch-in-python-get-single-character.html"""      
    fd = sys.stdin.fileno()   
    oldterm = termios.tcgetattr(fd)
    newattr = termios.tcgetattr(fd)
    newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, newattr)
    
    oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)
    
    try:
        while 1:
            try:
                c = sys.stdin.read(1)
                break
            except IOError: pass
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
        fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)
        return c
    
def timestamp_to_datetime(timestamp):
    """ converts a unix timestamp to a datetime object """
    return datetime.datetime.fromtimestamp(timestamp)