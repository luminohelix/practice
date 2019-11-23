# -*- coding: utf-8 -*-
"""
Calculate Radius/Diameter/Circumference/Area
Created on Fri Nov 22 23:12:23 2019

@author: Ashley
"""
from math import pi, sqrt

measurement = ""

# Function to do calculations based on suffix entered.
def calculate(measure, suffix):
    switcher = {
            # Radius
            "R" : [measure, 2 * measure, pi * (2 * measure), pi * measure**2 ],
            # Diameter
            "D" : [measure / 2, measure, pi * measure, pi * (measure/2)**2],
            # Circumference
            "C" : [(measure / pi) / 2, measure / pi, measure,
                   pi * ((measure / pi) / 2)**2],
            # Area
            "A" : [sqrt(measure) / sqrt(pi), 2 * (sqrt(measure) / sqrt(pi)),
                   pi * 2 * (sqrt(measure) / sqrt(pi)), measure]
            }
    return switcher.get(suffix, "Invalid suffix. Use R for radius, D for " +
                        "diameter, C for Circumference, A for area, or " +
                        "Q to quit.")
   

def print_results(radius, diameter, circumference, area):
     print(f"Radius: {radius} units\n" + 
           f"Diameter: {diameter} units\n"+
           f"Circumference: {circumference} units. or {diameter}π units\n" +
           f"Area: {area} units² or {radius**2}π units²")

while measurement != "Q":
   
    # Ask the user to input a measurement for a radius, diameter, circumference
    # or Area for calculations, or q to exit the program.
    measurement = input("Enter a number measurement and specify R (radius), D " 
                        + "(diameter), C (Circumference), or A (area). " +
                        "Enter Q to quit. ")
    if measurement.upper() == "Q":
        print("Quitting...")
        break
    measurement_num = ""
    # Get the entered suffix and turn the string into an actual number.
    measure_suffix = measurement[-1].upper()
    
    for i in range (0, len(measurement)-1):
        measurement_num += measurement[i]
    try:
        measurement_num = float(measurement_num)
          
        result = calculate(measurement_num, measure_suffix)
        # If a calculation happened, there will be 4 values. Otherwise, error.
        if len(result) == 4:
            print_results(result[0], result[1], result[2], result[3])
        else:
            print(result)
    except ValueError:
        print("Invalid measurement.")
        

