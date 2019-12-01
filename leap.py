#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Leap Year Checker
Created on Sun Dec  1 04:33:20 2019

@author: luminohelix
"""
import datetime as dt

while True:
    
    try:
        # Get a year from the user, as well as the current year.
        year = int(input("Please enter a year: "))
        today = dt.datetime.now()
        current_year = int(today.strftime("%Y"))
        # Year will be invalid if it's less than 1 and more than 9999.
        if year < dt.MINYEAR or year > dt.MAXYEAR:
            message = "\nInvalid year.\n"
        # Tenses for past/present/future years.
        if year > current_year or year == current_year:
            tense = "is"
        else:
            tense = "was"
        # Tailor message according to whether or not year is a leap year.
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                
            message = f"\n{year} {tense} a leap year.\n"
        
        else:
            message = f"\n{year} {tense} not a leap year.\n"
            
        print(message)
     # End program if something other than an int was entered.
    except ValueError:
        break