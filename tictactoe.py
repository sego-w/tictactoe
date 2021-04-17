
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
    global list_rows
    row1 = [' ',' ',' ']
    row2 = [' ',' ',' ']
    row3 = [' ',' ',' ']
    list_rows = [row1,row2,row3]
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
        # Alternatively: while pick_row != int(pick_row):
        pick_row = int(input("Pick your row! "))
    while isinstance(pick_pos,int) == False: 
        pick_pos = int(input(f"Which place would you like to place your {user_sym}? "))
    # Editing the row/column
    list_rows[pick_row-1][pick_pos-1] = user_sym
    # Display result
    display(row1,row2,row3)
__main__()

#Check if the game is over
def gameovercheck():
    global gamewin
    global gamelose
    if list_rows[0][0:3] == user_sym or list_rows[1][0:3] == user_sym or list_rows[2][0:3] == user_sym:
        gamewin = True
    elif list_rows[0][0:3] == opposite or list_rows[1][0:3] == opposite or list_rows[2][0:3] == opposite:
        gamelose = True
    elif list_rows[0:3][0] == user_sym or list_rows[0:3][1] == user_sym or list_rows[0:3][2] == user_sym:
        gamewin = True
    elif list_rows[0:3][0] == opposite or list_rows[0:3][1] == opposite or list_rows[0:3][2] == opposite:
        gamelose = True
    elif row1[0] == row2[1] == row3[2] == user_sym or row1[2] == row2[1] == row3[0] == user_sym:
        gamewin = True
    elif row1[0] == row2[1] == row3[2] == opposite or row1[2] == row2[1] == row3[0] == opposite:
        gamelose = True
    if gamewin == True:
        print("Congrats! You won!")
    if gamelose == True:
        print("You lost lulz")

gameovercheck()

# Placing an X or O randomly

def robot_hax():
    global bot_row
    global bot_pos
    sleep(1)
    print("Alright! It's time for your opponent to make their move!")
    sleep(1)
    bot_row = randint(1,3)
    bot_pos = randint(1,3)
    while list_rows[bot_row-1][bot_pos-1] != ' ':
        bot_row = randint(1,3)
        bot_pos = randint(1,3)
    list_rows[bot_row-1][bot_pos-1] = opposite
    display(row1,row2,row3)
    

    

if gamewin == False and gamelose == False:
    
    gameovercheck()
    robot_hax() 


def whole_program():
    global gamewin
    global gamelose
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