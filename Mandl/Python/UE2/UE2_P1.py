# -*- coding: utf-8 -*-
"""
====================================================================
Author:        Lucas Mandl
Company:       FH Joanneum
Date:          11.10.2020
Description:   Implementation of laboratory session 2 - P.1 functions
====================================================================
"""

# clear command line and workspace:
try:
    from IPython import get_ipython
    get_ipython().magic('clear')
    get_ipython().magic('reset -f')
except:
    pass

def check_prime(num):
    if num == 1:
        return False
    if num <= 3:
        return True
    elif num%2 == 0 or num%3 == 0:
        return False
    
    i = 3
    
    while i*i <= num:
        if num%i == 0:
            return False
        i = i + 1
        
    return True
    
a = check_prime(31)