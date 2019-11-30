# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:52:52 2019

@author: Ashley
"""
import guess_lib as gl
from colorama import Fore

# Main program loop.
def main():        
    while True:
        gl.title_screen()
        gl.menu_select = input(Fore.GREEN + "Please select an option: ")
        if gl.menu_select not in gl.menu:
            print(Fore.RED + "\nInvalid menu selection.\n")
        elif gl.menu_select == "3":
            break
        else:
            if gl.menu_select == "1":
                gl.player_guesses()
                        
            else:
                gl.cpu_guesses()
                
if __name__ == "__main__":
    main()
