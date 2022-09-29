# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 07:26:07 2022

@author: rosst
"""

import time
import string
import random

# This method of reversing a string takes advantage of pythons lists simply
# making the string a list, then reversing it using the inbuilt reverse
# method, then joining the list

def rev_string5(x):
    txt = list(x)
    txt.reverse()
    return "".join(txt)

print(rev_string5("Reverse this string"))

# Similar to the last versions this creates a random strirng of length x

def random_string(x):
    
    a = string.ascii_lowercase
    return("".join(random.choice(a) for i in range(x)))

test_string = random_string(5000)
current = time.perf_counter()
txt= rev_string5(test_string)
elasped = time.perf_counter() - current  

print("\nThis test took",elasped,"seconds")