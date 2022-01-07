#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 23:56:53 2022

@author: jeff
"""
"""
function to calculate 
"""
def savings():
    n = int(input("enter number of days: ")) 
    z = n + 1
    x = sum(range(z))
    print ("Total Amount saved after",n,"Number of days:", x)
    
savings()
