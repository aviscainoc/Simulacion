# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 08:52:44 2021

@author: Adrian
"""

import random
import matplotlib.pyplot as plt

result = []
def generarNum():
    num=random.randrange(1,7)
    return num

def generarHist(frecuencia):
    
    for i in range(frecuencia):
        num1 = generarNum()
        num2 = generarNum()
        
        total = num1+num2
        result.append(total)
        
    plt.hist(result)
        
        


#generarHist(100)
#generarHist(1000)
#generarHist(10000)
generarHist(100000)
