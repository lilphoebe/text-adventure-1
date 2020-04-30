#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 10:36:16 2020

@author: phoebethatcher
"""


#PHOEBE'S TEXT ADVENTURE
# playername = input("What's your name? >")
# print("Your name is{}".format(playername, "knight"))

# dir()

import sys

def main():
    playername = input("What is your name? > ")
    print(f"Your name is {playername}")
    housename = input("What was your father's name? > ")
    print(f"So you are {playername} of the house of {housename}")
    start_room(1)
    
def start_room(roomnumber):
    print(initiate_string(roomnumber))
    either_or(roomnumber)
    
def initiate_string(roomnumber):
    if roomnumber == 1:
        return "You are alone in the war tent of your clan on the eve of battle. You must flee!"
    if roomnumber == 2:
        return "The tunnel is dark and squelchy and narrow. After some time you come to a crossing with an underground river."
    if roomnumber == 3:
        return "Across the the bridge you find a weeping turtle and a fine platinum treasure chest."  
    
def either_or(roomnumber):
    choice = input(choice_string(roomnumber))
    if choice == "quit":
        sys.exit()
    if choice == good_choice(roomnumber):
        start_room(roomnumber +1)
    if choice == bad_choice(roomnumber):
        print(bad_choice_string(roomnumber))
        startover()
    else:
        print(tryagain(roomnumber))
        start_room(roomnumber)         
        
def choice_string(roomnumber):
    if roomnumber == 1:
        return "Do you go through the trapdoor in the ground, or out the back of the tent? > "
    if roomnumber == 2:
        return "Do you cross the bridge, or swim along the river? > "
    if roomnumber == 3:
        return "Do you comfort the turtle or raid the chest? > "
        
def good_choice(roomnumber):
    if roomnumber == 1:
        return "trapdoor"
    if roomnumber == 2:
        return "cross the bridge"
    if roomnumber == 3:
        return "comfort the turtle"
        
    
def good_choice_string(roomnumber):
    if roomnumber == 1:
        return "You go through the trapdoor."
    
def bad_choice(roomnumber):
    if roomnumber ==1:
        return "back of the tent"
    if roomnumber ==2:
        return "swim"

def bad_choice_string(roomnumber):
    if roomnumber == 1:
        return "you go through the back of the tent. Your clan's warlord stands before you, polearm raised. Oops."
    if roomnumber ==2:
        return "You jump in and initiate breaststroke before you recall you are in full plate armor. Oops."
    
def tryagain(roomnumber):
    if roomnumber ==1:
        return "You must pick 'trapdoor' or 'back of tent'... hurry, there is not much time!"
    if roomnumber ==2:
        return "Will you 'cross the bridge' or 'swim'? Quick!"
        
def startover():
    initiate_startover = input("You lost! Would you like to start over? > ")
    if initiate_startover == "yes":
        start_room(1)
    if initiate_startover == "no":
        print("goodbye!")
        sys.exit()    

    
        
main()
    
if __name__ == '__main__':
    main()

# def startadventure():
#     print("You are alone in the war tent of your clan on the eve of battle. You must flee.")
#     door_picked = input("Do you go through the trapdoor in the ground, or out the back of the tent? >")
#     if door_picked == "trapdoor":
#         print("You picked the trapdoor.")
#     elif door_picked == "back of tent":
#         print("You go through the back of the tent.")
#     else:
#         print("You must pick 'trapdoor' or 'back of tent' ... hurry, there is not much time!")
    

# if __name__ == '__main__':
#     main()