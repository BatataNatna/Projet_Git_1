# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 00:20:54 2022

@author: Khedoudja Rym Merad
"""

import math

def pythagore(a,b):
    if type(a)== str:
        a = input ("entrez la valeur de A ")
    if type(b)== str:
        b= input("entrer la valeur de b")
    return math.sqrt(a**2+b**2)

