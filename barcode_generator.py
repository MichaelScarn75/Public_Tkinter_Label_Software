# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:02:17 2023

@author: user
"""

from decimal import Decimal


def barcode_generator(RSP, barcode):
    
    RSP = Decimal(RSP)
    RSP = str(round(RSP,2))
    RSP = RSP.replace('.', '')
    
    if len(RSP) == 3:
        RSP = "00" + RSP
    elif len(RSP) == 4:
        RSP = "0" + RSP
    elif len(RSP) == 5:
        pass
    else:
        pass
    
    
    temp_list = list(barcode)
    temp_list = temp_list[:7]
    barcode = ""
    barcode = barcode.join([i for i in temp_list])
    barcode = barcode + RSP
    
    sum_odd = 0
    sum_even = 0
    
    for i in range(1, 13):
        if i % 2 == 0:
            sum_even += int(barcode[i-1])
        
        else:
            sum_odd += int(barcode[i-1])
            
    sum_even *= 3
    sum_even += sum_odd
    if sum_even % 10 == 0:
        last_digit = str(sum_even % 10)
        
    elif sum_even % 10 != 0:
        last_digit = sum_even % 10
        last_digit = str(10 - last_digit)
    
    barcode = barcode + last_digit
    
    return barcode
