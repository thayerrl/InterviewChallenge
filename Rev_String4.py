# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 21:30:50 2022

@author: rosst
"""
import time
import random
import string

# This way of reversing a string uses recursion. Each "loop" that is ran 
# through the function again cuts a letter off of x and adds it to the buffer
# variable. For this version I was trying to be as conscise as possible. 

def rev_string4(x, buffer=""):
    if len(x) == 0: return buffer
    else: return rev_string4(x[:-1], buffer = buffer + x[len(x)-1])
        
txt = "Reverse this string"       
 
print(rev_string4(txt))

# The rest of this code is for time testing purposes 

# Similar to the last versions this creates a random strirng of length x

def random_string(x):
    
    a = string.ascii_lowercase
    return("".join(random.choice(a) for i in range(x)))

# This clocks the time before and after the function is ran to see how long 
# This method took. For this revision of the code, the test could only be ran
# until loop 2184 due to recursion limits.
test_string = random_string(2184)
current = time.perf_counter()
txt= rev_string4(test_string)
elasped = time.perf_counter() - current  

print("\nThis test took",elasped,"seconds")