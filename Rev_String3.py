# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:25:33 2022

@author: rosst
"""
import time
import random
import string

# This method will use list comprehention in a while loop to reverse the string inside of
# A child class (I am copying the class rev_string2)

class rev_string2:
    
    # This creates the class opject with a property mpt_str or empty string
    def __init__(self):
        self.mpt_str = ""
        
    # This reverses the string iteritivly     
    def reverse(self,x, flag=1):
        
        tmp = [*x]

        for i in range(len(tmp)):
            tmp2 = tmp[len(tmp) - i - 1]
            self.mpt_str += tmp2
        if flag == 1:
            print(self.mpt_str)
            return
        else:
            return

# This class is a child class of the class created in Rev_Srting2 inheriting
# mpt_str from its parent class. This causes excess complexity but can be done

class rev_string3(rev_string2):
    def __init__(self):
        super().__init__()
        # This prompts the user for a string input when the object is created 
        self.txt = input("Enter the string you would like to reverse: \n")
        self.flag = self.txt
        self.i = 0
        
    # This uses list comprehention to split the string by each letter
    def split(self, x):
        return([a for a in x])
    # This reverses the string inputted by the user 
    def reverse(self, flag=1):
        
        buffer = self.split(self.txt)
        while self.i < len(buffer):
            self.mpt_str += buffer[len(buffer)-self.i-1]
            self.i += 1
        if self.flag == self.txt:        
            return(print("\nThe reverse string is :\n",self.mpt_str))
        else:
            return()
            
text = rev_string3()

text.reverse()

# To test the speed of this way of reversing a string, the initial object 
# self.txt value is overwritten

# This test is similar to the other tests, clocking the time before and 
# after running the method to see how long it took

def random_string(b):
    a = string.ascii_lowercase
    return("".join(random.choice(a) for i in range(b)))

text.txt = random_string(5000)

current = time.perf_counter()
text.reverse()
elasped = time.perf_counter() - current  

print("\nThis test took",elasped,"seconds")


        

