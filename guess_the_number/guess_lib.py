# -*- coding: utf-8 -*-
"""
Guess the Number - Function Library
Created on Fri Nov 29 22:47:08 2019

@author: Ashley
"""

from random import randint
from colorama import Fore, Style

# Menu elements.

menu = {
       "1" : "1. Guess the CPU's Number",
       "2" : "2. CPU Guesses Your Number",
       "3" : "3. Quit"
        }

titles = {
        1: "\nWelcome to Guess the Number!",
        2: "\nGuess the CPU's Number",
        3: "\nCPU Guesses Your Number"
        }
menu_select = ""

# Initialize Colorama
#init()

# "Title screen" and menu display.
def title_screen():
    print(Fore.BLUE + Style.BRIGHT + titles[1])
    print("=" * len(titles[1]))
    for i in menu:
        print(Style.RESET_ALL + menu[i])
    return menu.get(menu_select, Fore.RED + "\nInvalid menu selection.\n")

# Player guesses CPU's number.    
def player_guesses():
    play_again = True
    print(Fore.BLUE + Style.BRIGHT + titles[2])
    print("=" * len(titles[2]))
    # Start game loop.
    while play_again == True:
        guess = 0
        guesses = 0
        number = randint(1,100)
        print(Style.RESET_ALL + "\nThe CPU has selected a number between 1-100 for you to"
              + " guess!")
        # While guess and number don't match, make sure the guess is in a valid
        # range before processing.
        while guess != number:
            try:
                guess = int(input(Fore.GREEN + "Enter your guess: "))
                if guess < 1 or guess > 100:
                    print(Fore.RED + "Invalid guess.")
                # Now increment the guesses and process how high or low the
                # guess is.
                else:
                    guesses += 1
                    if guess > number:
                        print(Style.RESET_ALL + f"{guess} is too high! Try again.")
                    elif guess < number:
                        print(Style.RESET_ALL + f"{guess} is too low! Try again.")
                    else:
                        print(Style.RESET_ALL + f"{guess} is the right number! You got it in "
                             + f"{guesses} guesses.")
                        # Ask the player if they would like to play again.
                        # Kick back to the main menu if not.
                        while play_again == True:       
                            play_again_prompt = input(Fore.GREEN + "Would you like to play "
                                                      + "again? (Y/N): ")
                            if play_again_prompt.upper() == "N":
                                play_again = False
                                break
                            elif play_again_prompt.upper() != "N" and play_again_prompt.upper() != "Y":
                                    print(Fore.RED + "Invalid input. Please enter Y or" 
                                          + " N.")
                            else:
                                break
            except ValueError:
                print(Fore.RED + "Invalid guess.")   
                
# CPU guesses player's number.
def cpu_guesses():
    play_again = True
    print(Fore.BLUE + Style.BRIGHT + titles[3])
    print("=" * len(titles[3]))
    print(Style.RESET_ALL + "\nPick a number and the CPU will try to guess what it is!")
    # Start the game loop.
    while play_again == True:
        guess_low = 1
        guess_high = 100
        guess = int((guess_low + guess_high) / 2)
        guesses = 0
        
        try:
            # Make sure player enters number within the appropriate range.
            number = int(input(Fore.GREEN + "Enter a number for the CPU to guess: "))
            if number < 1 or number > 100:
                print(Fore.RED + "Invalid input. Please enter a number between 1 and "
                      + "100.")
            else:
                # Use bisection search algorithm for calculating guesses.
                while abs(guess - number) > 0:
                    guesses += 1
                    guess = randint(guess_low, guess_high)
                    if guess == number:
                        break
                    # Adjust lower and upper bounds for recalculation of 
                    # subsequent guesses.
                    elif guess > number:
                        print(Style.RESET_ALL + f"Oops! The CPU guessed {guess}, but that's too" 
                              + " high!")
                        guess_high = guess
                    else:
                        print(Style.RESET_ALL + f"Oops! The CPU guessed {guess}, but that's too"
                              + " low.")
                        guess_low = guess
                    guess = int((guess_low + guess_high) / 2)
                    
                print(Style.RESET_ALL + f"Eureka! The CPU guessed the number {number} in " +
                      f"{guesses} guesses.")
                #Ask the player if they would like to play again.
                # Kick back to the main menu if not.
                while play_again == True:
                    play_again_prompt = input(Fore.GREEN + "Would you like to play again? "
                                              + "(Y/N): ")
                    if play_again_prompt.upper() == "N":
                        play_again = False
                        break
                    elif play_again_prompt.upper() != "N" and play_again_prompt.upper() != "Y":
                            print(Fore.RED + "Invalid input. Please enter Y or N.")
                    else:
                        break
        except ValueError:
            print(Fore.RED + "Invalid input. Please enter a number between 1 and 100.")


