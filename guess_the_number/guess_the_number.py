# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 17:52:52 2019

@author: Ashley
"""
import guess_lib

# Main program loop.
def main():        
    while True:
        title_screen()
        menu_select = input(Fore.GREEN + "Please select an option: ")
        if menu_select not in menu:
            print(Fore.RED + "\nInvalid menu selection.\n")
        elif menu_select == "3":
            break
        else:
            if menu_select == "1":
                player_guesses()
                        
            else:
                cpu_guesses()
                
if __name__ == "__main__":
    main()