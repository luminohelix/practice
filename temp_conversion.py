# -*- coding: utf-8 -*-
"""
Temperature Conversion
Created on Wed Nov 20 05:20:50 2019

@author: Ashley
"""



temperature = ""
while temperature.upper() != "Q":
    # Get a temperature, specified in Kelvin, Centigrade, or Fahrenheit.
    temperature = input("Enter a temperature number and scale letter" +
                       "(K, C, or F) or Q to quit: " )
    if temperature.upper() == "Q":
        break
    else:
        scale = temperature[-1]
        temp_num = ""
       
        for i in range(0, len(temperature)-1):
            temp_num += temperature[i]
        try:
            temp_num = float(temp_num)
            # Check the last letter of the temperature string to see what 
            # we're converting from/to.
            if scale.upper() == "F" or scale.upper() == "C" or scale.upper() == "K":
                convert_to = input("Enter scale letter to convert to: ")
                if convert_to.upper() != "F" and convert_to.upper() != "C" and convert_to.upper() != "K":
                    print("Invalid scale.")
                else:    
                    # Don't try to convert to the same scale.
                    if scale.upper() == convert_to.upper():
                        print(f"{temperature} is already the correct temperature.")
                    else:
                        if convert_to.upper() == "F":
                            if scale.upper() == "C":
                                # Celsius to Fahrenheit
                                new_temp = (temp_num * (9/5) + 32)
                            if scale.upper() == "K":
                                # Kelvin to Fahrenheit
                                new_temp = (temp_num * (9/5) - 459.67)
                        elif convert_to.upper() == "C":
                                # Fahrenheit to Celsius
                            if scale.upper() == "F":
                                new_temp = ((temp_num - 32) / 1.8)
                                # Kelvin to Celsius
                            if scale.upper() == "K":
                                new_temp = temp_num - 273.15
                        elif convert_to.upper() == "K":
                                # Fahrenheit to Kelvin
                            if scale.upper() == "F":
                                new_temp = ((temp_num + 459.67) * (5/9))
                                # Celsius to Kelvin
                            if scale.upper() == "C":
                                new_temp = temp_num + 273.15
                        else:
                            print("Invalid scale.")
                        print(f"{temp_num}{scale.upper()} is {new_temp}{convert_to.upper()}.")
        #Throw an exception if given a temperature that's not valid.
        except ValueError:
            print("Invalid temperature.")
        
            
          