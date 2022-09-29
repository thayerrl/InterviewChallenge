# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 18:25:33 2022

@author: rosst
"""

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
        self.i = 0
    
    # This uses list comprehention to split the string by each letter
    def split(self, x):
        return([a for a in x])
    # This reverses the string inputted by the user 
    def reverse2(self, flag=1):
        
        tmp = self.split(self.txt)
        while self.i < len(tmp):
            self.mpt_str += tmp[len(tmp)-self.i-1]
            self.i += 1
        return(print("\nThe reverse string is :\n",self.mpt_str))
            
            
txt = rev_string3()

txt.reverse2()

# To test the speed of this way of reversing a string, 
        

