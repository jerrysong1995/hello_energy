# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 15:10:10 2024

@author: Jerry
"""

import math

def calc_pv_array_size(building_width, building_length, angle, pv_width, pv_height, pv_power):

    adjusted_roof_width = ((building_width))/math.cos(angle)
    # print(adjusted_roof_width)
    # print("\n")
    
    num_panel = (building_length//pv_width)*(adjusted_roof_width//pv_height)
    # print(num_panel)
    # print("\n")
    
    power_capacity = num_panel*pv_power
    power_capacity = power_capacity/1000
    # print(power_capacity)
    # print("\n")
    
    return num_panel, power_capacity