# -*- coding: utf-8 -*-
import time
import random
import string

# This function takes the string and slices it backwards returning the inverse string

def rev_string1(x):
    return(x[::-1])

# The timers here track how long it takes to run the function above

current = time.perf_counter()
txt= rev_string1("Reversing the string")
elasped = time.perf_counter() - current    

# Printing out the reversed string along with 

print(txt)

# to test this methods speed, a random string is created of length 5000

# This function creates a random string of length x
def random_string(x):
    
    a = string.ascii_lowercase
    return("".join(random.choice(a) for i in range(x)))

# This clocks the time before and after the function is ran to see how long 
# This method took
test_string = random_string(5000)
current = time.perf_counter()
txt= rev_string1(test_string)
elasped = time.perf_counter() - current  

print("\nThis test took",elasped,"seconds")
    

