# -*- coding: utf-8 -*-
"""
Calculate Radius/Diameter/Circumference/Area
Created on Fri Nov 22 23:12:23 2019

@author: Ashley
"""
from math import pi, sqrt

measurement = ""
def radius_given(measure):
    radius = measure
    diameter = 2 * radius
    circumference = pi * diameter
    area = pi * radius **2
    return radius, diameter, circumference, area

def diameter_given(measure):
    radius = measure / 2
    diameter = measure
    circumference = pi * diameter
    area = pi * radius**2
    return radius, diameter, circumference, area

def circumference_given(measure):
     radius = (measure / pi) / 2
     diameter = measure / pi
     circumference = measure
     area = pi * radius**2
     return radius, diameter, circumference, area

def area_given(measure):
    radius = sqrt(measure) / sqrt(pi)
    diameter = 2 * radius
    circumference = pi * diameter
    area = measure
    return radius, diameter, circumference, area

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
    measure_suffix = measurement[-1].upper()
    
    #Is it a valid measurement suffix? If not, then print warning.
    if  measure_suffix != "R" and measure_suffix != "D" and measure_suffix != "C" and measure_suffix != "A":
            print("Invalid suffix. Use R for radius, D for diameter, C for " +
              "Circumference, A for area, or Q to quit.")
    else:
        # Convert measurement in preparation for calculation.
        for i in range (0, len(measurement)-1):
            measurement_num += measurement[i]
        try:
            measurement_num = float(measurement_num)
            # If radius is given...
            if measure_suffix == "R":
                result = radius_given(measurement_num)
            # If diameter is given...
            elif measure_suffix == "D":
                result =  diameter_given(measurement_num)
            # If circumference is given...
            elif measure_suffix == "C":
                result = circumference_given(measurement_num)
            # If area is given...
            else:
                result = area_given(measurement_num)
            # Show all results, in both calculated and simplified form.
            print_results(result[0],result[1], result[2], result[3])
        except ValueError:
            print("Invalid measurement.")
        

