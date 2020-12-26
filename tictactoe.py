### IMPORTANT! SINCE I AM LAZY YOU WILL NOT WIN/LOSE IN THE CASE OF A DIAGONAL ###
from time import sleep
from random import randint
import sys
from sys import exit
import os
def display(a,b,c):
    print(','.join(a))
    print(','.join(b))
    print(','.join(c))
# Tic Tac Toe
# December 2020
# Initial Playfield
def initial_state():
    global gamewin
    global gamelose
    global row1
    global row2
    global row3
    global user_sym
    global opposite
    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']
    repeat_game = 'Irrelevant string'
    gamewin = False
    gamelose = False
# Starting the game!
    print("Welcome to Tic Tac Toe! Here is your board: ")
    display(row1,row2,row3)
    user_sym = input("Would you like to be X or O? ").upper()
    if user_sym == 'O':
        opposite = 'X'
    else:
        opposite = 'O'
initial_state()
# Choosing the row and column
def __main__():
    global pick_row
    global pick_pos
    pick_row = "Not a digit"
    pick_pos = "Also not a digit"
    while isinstance(pick_row,int) == False:
        pick_row = int(input("Pick your row! "))
    while isinstance(pick_pos,int) == False: 
        pick_pos = int(input(f"Which place would you like to place your {user_sym}? "))
    # Editing the row/column
    if pick_row == 1:
        if pick_pos == 1:
            row1[0] = user_sym
        elif pick_pos == 2:
            row1[1] = user_sym
        elif pick_pos == 3:
            row1[2] = user_sym
    # Second row
    if pick_row == 2:
        if pick_pos == 1:
            row2[0] = user_sym
        elif pick_pos == 2:
            row2[1] = user_sym
        elif pick_pos == 3:
            row2[2] = user_sym
    # Third row
    if pick_row == 3:
        if pick_pos == 1:
            row3[0] = user_sym
        elif pick_pos == 2:
            row3[1] = user_sym
        elif pick_pos == 3:
            row3[2] = user_sym
    # Display result
    display(row1,row2,row3)
__main__()

#Check if the game is over
def gameovercheck():
    global gamewin
    global gamelose
    if row1[0] == row1[1] == row1[2] == user_sym or row2[0] == row2[1] == row2[2] == user_sym or row3[0] == row3[1] == row3[2] == user_sym:
        gamewin = True
    elif row1[0] == row1[1] == row1[2] == opposite or row2[0] == row2[1] == row2[2] == opposite or row3[0] == row3[1] == row3[2] == opposite:
        gamelose = True
    elif row1[0] == row2[0] == row3[0] == user_sym or row1[1] == row2[1] == row3[1] == user_sym or row1[2] == row2[2] == row3[2] == user_sym:
        gamewin = True
    elif row1[0] == row2[0] == row3[0] == opposite or row1[1] == row2[1] == row3[1] == opposite or row1[2] == row2[2] == row3[2] == opposite:
        gamelose = True
    if gamewin == True:
        print("Congrats! You won!")
    if gamelose == True:
        print("You lost lulz")

gameovercheck()

# Placing an X or O randomly

def robot_hax():
    sleep(1)
    print("Alright! It's time for your opponent to make their move!")
    sleep(1)
    bot_row = randint(1,3)
    bot_pos = randint(1,3)
    if bot_row == 1:
        while row1[bot_pos-1] != ' ':
            bot_pos = randint(1,3)
    elif bot_row == 2:
        while row2[bot_pos-1] != ' ':
            bot_pos = randint(1,3)
    elif bot_row == 3:
        while row3[bot_pos-1] != ' ':
            bot_pos = randint(1,3)
    # Row 1
    if bot_row == 1:
        if row1[bot_pos-1] == ' ':
            if user_sym == 'O':
              row1[bot_pos-1] = 'X'
            elif user_sym == 'X':
              row1[bot_pos-1] = 'O'
    # Row 2
    if bot_row == 2:
        if row2[bot_pos-1] == ' ':
            if user_sym == 'O':
              row2[bot_pos-1] = 'X'
            elif user_sym == 'X':
              row2[bot_pos-1] = 'O'
    # Row 3
    if bot_row == 3:
        if row3[bot_pos-1] == ' ':
            if user_sym == 'O':
              row3[bot_pos-1] = 'X'
            elif user_sym == 'X':
              row3[bot_pos-1] = 'O'
    display(row1,row2,row3)
    

if gamewin == False and gamelose == False:
    robot_hax() 
    gameovercheck()

def whole_program():
    while gamewin == False or gamelose == False:
        __main__()
        gameovercheck()
        robot_hax()
        gameovercheck()
        if gamewin == True or gamelose == True:
            restart_check = input("Would you like to play again? (Y/N) ").upper()
            if restart_check == 'Y':
                initial_state()
                whole_program()
            if restart_check == 'N':
                exit("Okay then! Goodbye...")
        sleep(1)
        print("Your turn!")
        sleep(1)
    
whole_program()



