# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math
import example2


# def calc_pv_array_size(building_width, building_length, angle, pv_width, pv_height, pv_power):

#     adjusted_roof_width = ((building_width))/math.cos(angle)
#     # print(adjusted_roof_width)
#     # print("\n")
    
#     num_panel = (building_length//pv_width)*(adjusted_roof_width//pv_height)
#     # print(num_panel)
#     # print("\n")
    
#     power_capacity = num_panel*pv_power
#     power_capacity = power_capacity/1000
#     # print(power_capacity)
#     # print("\n")
    
#     return num_panel, power_capacity

#Request for user input
building_width = int(input("Enter building width in metres: "))
print(building_width)
print("\n")

building_length = int(input("Enter building length in metres: "))
print(building_length)
print("\n")

roof_angle = int(input("Enter the roof angle: "))
print(roof_angle)
print("\n")
angle = math.radians(roof_angle)

pv_width = int(input("Enter PV Width in millimetres: "))
print(pv_width)
print("\n")
pv_width = pv_width/1000

pv_height = int(input("Enter the PV height in millimetres: "))
print(pv_height)
print("\n")
pv_height = pv_height/1000

pv_power = int(input("Enter the PV power in Wp: "))
print(pv_power)
print("\n")

num_panel, power_capacity = example2.calc_pv_array_size(building_width, building_length, angle, pv_width, pv_height, pv_power)

    
#calc_pv_array_size(num_panel, power_capacity) 
# adjusted_roof_width = ((building_width))/math.cos(angle)
# print(adjusted_roof_width)
# print("\n")

# num_panel = (building_length//pv_width)*(adjusted_roof_width//pv_height)
print(num_panel)
print("\n")

# power_capacity = num_panel*pv_power
# power_capacity = power_capacity/1000
print(power_capacity)
print("\n")
