#Import random

import random
from unicodedata import name

from numpy import False_

#Rule of the game
R = "Rock"
P = "Paper"
S = "Scissors"
rules = "\t\t*****Rules of the Game*****\n1. Rock beats Scissors\n2. Paper beats Rock\n3. Scissors beats Paper\n"

#creating list for possible options 
#where R= rock, p=paper and s=scissors
options_to_chose = ["R", "P", "S"]

#creating list of players at a time
list_of_players =[]


def init():

 print( "******Welcome to Rock-Paper-Scissors Game, Have fun!******")

 name = input("What is your name?\n")
 name = name.capitalize()
 list_of_players.append(name)
 print(list_of_players)
 
 isvalid_input = True

 while isvalid_input:
    wants_to_play =input("\t Would you like to Play?, \n Enter \"Y\" for yes and \"N\" for no\n")
    wants_to_play = wants_to_play.upper()

    if wants_to_play == "Y":
        rock_paper_scissors()
        break
    elif wants_to_play == "N":
        isvalid_input = False
    else:
        print("Invalid input, Enter Y or N")
        
#function to run the game
def requestPlayAgain(name):
    print(f"{name}, Would you like to Play again?\n")
    while( True ):
        another_try = input("Please enter Y for yes or N for no\n")
        another_try = another_try.upper()
        
        if another_try == "Y":
            return True

        if another_try == "N":
                
            return False
        
        print("Invalid input, enter \"Y\" or \"N\"")

def rock_paper_scissors():
    name = list_of_players[0]
    print(f"Welcome on Board {name}! The Game master is waiting for you\n")

    print(rules)
    
    #Get players choice 
    while True: 
        player_input =input(f"R = {R}\tP = {P}\tS = {S}\nPlease Enter Your Choice:\n")

        #convert it to uppercase incase a user enters lowercase
        player_input =player_input.upper()

        #Get the CPU choice by calling our generate Cpu_choice which, we've defined already.
        cpu_input = generate_cpu_choice()

        isATie = False

        

        #check of user enter the valid options
        if player_input == "R" or player_input =="P" or player_input =="S":
            
            #if user option is valid, compare it with CPU generated option and determine winner according to the set rules 
            if player_input == "R" and cpu_input == "S":
                print(f"{name} ({R}) : CPU ({S})\n")
                print(f"{name} you Won, Congrats!")

            elif player_input == "S" and cpu_input == "R":
                print(f"{name} ({S}) : CPU ({R})\n")
                print(f"{name} you Lost, Try again!")

            elif player_input == "P" and cpu_input == "R":
                print(f"{name} ({P}) : CPU ({R})\n")
                print(f"{name} you Won, Congrats!")

            elif player_input == "R" and cpu_input == "P":
                print(f"{name} ({R}) : CPU ({P})\n")
                print(f"{name} you Lost, Try again!")

            elif player_input == "S" and cpu_input == "P":
                print(f"{name} ({S}) : CPU ({P})\n")
                print(f"{name} you Won, Congrats!")

            elif player_input == "P" and cpu_input == "S":
                print(f"{name} ({P}) : CPU ({S})\n")
                print(f"{name} you Lost, Try again!")
                     
            elif player_input == cpu_input:
                print(f"{name} ({player_input}) : CPU ({cpu_input})\n")
                print("It's a tie, Play again...")
                isATie = True
                
            if not isATie:
                if not requestPlayAgain(name):
                    break;
        else:
            print(f"{name}, Your entry is Invalid, Chose either \"R\" or \"P\" or \"S\" ")
    


#function to generate CPU choices at random
def generate_cpu_choice():
   
    return random.choice(options_to_chose)
     
#calling the initialisation function to start the app.
init()