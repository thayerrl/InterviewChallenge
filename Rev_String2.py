import time
import random
import string
# This class will split a string using an iterative method

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


a = rev_string2()    
b = rev_string2()

rev = b.reverse("Reverse this string")
        
# to test this methods speed, a random string is created of length 5000

# This function creates a random string of length x

def random_string(b):
    a = string.ascii_lowercase
    return("".join(random.choice(a) for i in range(b)))

test_string = random_string(5000)
current = time.perf_counter()
a.reverse(test_string, flag=0)
elasped = time.perf_counter() - current  

print("\nThis test took",elasped,"seconds")
    