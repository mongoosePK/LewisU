#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 14:30:21 2019

@author: szczurpi

Machine Problem 2
Gen-Tic-Tac-Toe Minimax Search with alpha/beta pruning
"""

import numpy as np
import random
import math


class GenGameBoard: 
    
    # Constructor method - setrs board size and blanks
    def __init__(self, boardSize):
        self.boardSize = boardSize  
        self.marks = np.empty((boardSize, boardSize),dtype='str') 
        self.marks[:,:] = ' '
    
    
    def printBoard(self): 
        print(' ',end='')
        for j in range(self.boardSize):
            print(' '+str(j+1), end='') 
        print()
        
        # Print the rows with marks
        for i in range(self.boardSize):
            # print the line separating the row
            print(' ',end='')
            for j in range(self.boardSize):
                print("--",end='')
            print('-')

            # print the row number
            print(i+1,end='')
            
            # print the marks on row
            for j in range(self.boardSize):
                print('|'+self.marks[i][j],end='')
            
            print('|')
                
        
        # print the line separating the last row
        print(' ',end='')
        for j in range(self.boardSize):
            print('--',end='')
        
        print("-")
    
    
    # Attempts to make a move given the row,col and mark
    # If move cannot be made, returns False and prints a message if mark is 'X'
    # Otherwise, returns True
    def makeMove(self, row, col, mark):
        possible = False  # Variable to hold the return value
        if row== -1 and col==-1:
            return False
        
        if row < 0 or row >= self.boardSize or col < 0 or col >= self.boardSize:
            print("Not a valid row or column!")
            return False
        
        # Check row and col, and make sure space is empty
        # If empty, set the position to the mark and change possible to True
        if self.marks[row][col] == ' ':
            self.marks[row][col] = mark
            possible = True    
        
        # Print out the message to the player if the move was not possible
        if not possible and mark=='X':
            print("\nself position is already taken!")
        
        return possible
    
    
    # Determines whether a game winning condition exists
    # If so, returns True, and False otherwise
    def checkWin(self, mark):
        won = False 
        
        # Check each row
        for i in range(self.boardSize):
            won = True
            for j in range(self.boardSize):
                if self.marks[i][j]!=mark:
                    won=False
                    break        
            if won:
                break
        
        # Check each column
        if not won:
            for i in range(self.boardSize):
                won = True
                for j in range(self.boardSize):
                    if self.marks[j][i]!=mark:
                        won=False
                        break
                if won:
                    break

        # Check first diagonal
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[i][i]!=mark:
                    won=False
                    break
                
        # Check second diagonal
        if not won:
            for i in range(self.boardSize):
                won = True
                if self.marks[self.boardSize-1-i][i]!=mark:
                    won=False
                    break

        return won
    
    # Determines whether the board is full
    def noMoreMoves(self):
        return (self.marks!=' ').all()

    #def max_value(self):
    def max_value(self, alpha, beta):
        utility = -2 #no need for negative infinity cuz -1 is a bad as it gets.
        move_row = None
        move_col = None
    # checkWin and then see if there are no more moves (in this order)
        if (self.checkWin('X')==True):
            return -1,0,0
        elif (self.checkWin('O')==True):
            return 1,0,0
        elif (self.noMoreMoves()==True):
            return 0,0,0
        
       
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if (self.marks[i][j] == ' '):
                    self.marks[i][j] = 'O'
                    #(u, newRow, newCol) = self.min_value()
                    (u, newRow, newCol) = self.min_value(alpha, beta)
                    # saving superior move
                    if u > utility:
                        utility = u
                        move_row = i
                        move_col = j
                    self.marks[i][j] = ' ' #undo move

                    # if utility >= beta:
                    #     return (utility, move_row, move_col)
                    # alpha = max(alpha, utility)

        return (utility, move_row, move_col)

    def min_value(self, alpha, beta):

        utility = 2 #math.inf not needed cuz it doesn't get beter than 1
        move_row = None
        move_col = None

        if (self.checkWin('X')==True):
            return -1,0,0
        elif (self.checkWin('O')==True):
            return 1,0,0
        elif (self.noMoreMoves()==True):
            return 0,0,0
        

        
        for i in range(self.boardSize):
            for j in range(self.boardSize):
                if (self.marks[i][j] == ' '):
                    self.marks[i][j] = 'X'
                    (u, newRow, newCol) = self.min_value(alpha, beta)
                    # saving superior move
                    if u < utility:
                        utility = u
                        move_row = i
                        move_col = j
                    self.marks[i][j] = ' ' #undo move

                    # if utility <= beta:
                    #     return (utility, move_row, move_col)
                    # beta = min(beta, utility)
        
        return (utility, move_row, move_col)


    def alpha_beta_search(self):
        (utility, move_row, move_col) = self.max_value(-2,2)
        return (utility, move_row, move_col)

    ##### TODO #####
    # Create function to check for best move
    #####      #####
    
    # TODO - this method should run MINIMAX to determine the value of each move
    # Then make best move for the computer by placing the mark in the best spot
    def makeCompMove(self):
        
        ######################DUMMY_CODE#############################
        # row, col = -1, -1
        # while not self.makeMove(row, col, 'O'):
        #     col = random.randint(1,boardSize)
        #     row = random.randint(1,boardSize)
        # print("Computer chose: "+str(row)+","+str(col))
        #########################END_DUMMY_CODE##########################
        utility, row, col = self.max_value(-2,2)
        self.makeMove(row, col, 'O')

# Print out the header info
print("CLASS: Artificial Intelligence, Lewis University")
print("NAME: [put your name here]")

LOST = -1
WON = 1
DRAW = 0    
wrongInput = False
boardSize = int(input("Please enter the size of the board n (e.g. n=3,4,5,...): "))
        
# Create the game board of the given size
board = GenGameBoard(boardSize)
        
board.printBoard()  # Print the board before starting the game loop
        
# Game loop
while True:
    # *** Player's move ***            
    # Try to make the move and check if it was possible
    # If not possible get col,row inputs from player    
    row, col = -1, -1
    while not board.makeMove(row, col, 'X'):
        print("Player's Move")
        row, col = input("Choose your move (row, column): ").split(',')
        row = int(row)-1
        col = int(col)-1

    # Display the board again
    board.printBoard()
            
    # Check for ending condition
    # If game is over, check if player won and end the game
    if board.checkWin('X'):
        result = WON
        break
    elif board.noMoreMoves():
        result = DRAW
        break
            
    # *** Computer's move ***
    board.makeCompMove()
    board.printBoard()    
    
    # Check for ending condition
    if board.checkWin('O'):
        result = LOST
        break
    elif board.noMoreMoves():
        result = DRAW
        break
        
# Check the game result and print out the appropriate message
print("GAME OVER")
if result==WON:
    print("You Won!")            
elif result==LOST:
    print("You Lost!")
else: 
    print("It was a draw!")


###########################################################################
############ END USED CODE ##############################################
###########################################################################
# def max_value(self, alpha, beta):

#     # checkWin and then see if there are no more moves (in this order)
#     if (self.checkWin('X')==True):
#         return 1
#     elif (self.checkWin('O')==True):
#         return -1
#     elif (self.noMoreMoves()==True):
#         return 0
       
#     utility = -2 #no need for negative infinity cuz -1 is a bad as it gets.
#     move_row = None
#     move_col = None
#     unusedComp = []
#     for i in range(self.boardSize):
#         for j in range(self.boardSize):
#             if (self.marks[i][j] == ' '):
#                 #unusedComp.append([i, j])
#                 self.marks[row][col] = 'O'
#                 # v = self.min_value(alpha, beta)
#                 (u, newRow, newCol) = self.min_value(alpha, beta)
#                 # saving superior move
#                 if u > utility:
#                     utility = u
#                     move_row = i
#                     move_col = j
#             self.marks[row][col] = ' ' #undo move

#             if utility >= beta:
#                 return utility, move_row, move_col
#             alpha = max(alpha, utility)

#     return utility, move_row, move_col

#     # for a in unusedComp:
#     #     # make move here
#     #     row, col = a
#     #     # directly mark
#     #     self.marks[row][col] = 'O'
#     #     # v = self.min_value(alpha, beta)
#     #     (u, )
#     #     # saving superior move

#     #     self.marks[row][col] = ' ' #undo move


#     #     if utility >= beta:
#     #         return utility
#     #     alpha = max(alpha, utility)


# def min_value(self, alpha, beta):

#     if (self.checkWin('X')==True):
#         return 1
#     elif (self.checkWin('O')==True):
#         return -1
#     elif (self.noMoreMoves()==True):
#         return 0
    
#     utility = 2 #math.inf not needed cuz it doesn't get beter than 1
#     move_row = None
#     move_col = None
#     unusedUser = []
#     for i in range(self.boardSize):
#         for j in range(self.boardSize):
#             if (self.marks[i][j] == ' '):
#                 #unusedUser.append([i, j])
#                 (u, newRow, newCol) = self.min_value(alpha, beta)
#                 # saving superior move
#                 if u < utility:
#                     utility = u
#                     move_row = i
#                     move_col = j
#             self.marks[row][col] = ' ' #undo move

#             if utility <= beta:
#                 return utility, move_row, move_col
#             alpha = min(alpha, utility)
    
#     return utility, move_row, move_col

#     # for a in unusedUser:
#     #     # make move here
#     #     row, col = a
#     #     # directly mark
#     #     self.marks[row][col] = 'X'
#     #     utility = self.max_value(alpha, beta)
#     #     self.marks[row][col] = ' '


#     #     if utility <= alpha:
#     #         return utility
#     #     beta = min(beta, utility)
    
    