# -*- coding: utf-8 -*-
"""
Created April 9, 2020
Alisha Augustin (aia43@drexel.edu)
Connect 4
"""
import numpy as np
import random

# Connect4 board has 7 columns and 6 rows
numCols = 7
numRows = 6

# Offset indices for the diagonals of length 4 or more
dMin = -2
dMax = 4

# reset the board
def resetBoard():
	global board
	global columnHeight
	# Create board as numpy 2D array, initialized to hold zeros
	board = np.zeros((numRows, numCols), dtype=int)
	# Keep track of the row value of each column
	# initialized to (5,5,5,5,5,5,5)
	columnHeight = np.full(numCols, numRows-1)

# insert a piece of the given player in the given column
def insert(player, column):
	row = columnHeight[column]
	if row >= 0:
		board[row, column] = player
		columnHeight[column] -= 1
		return True
	else:
		print("ERROR: column {} is full".format(column))
		return False

# make a random play for player player
def randomPlay(player):
	openColumns = np.where(columnHeight >= 0)[0]
	randomColumn = random.choice(openColumns)
	insert(player,randomColumn)

# check if the board is full
def boardFull():
	openColumns = np.where(columnHeight >= 0)[0]
	return True if len(openColumns) == 0 else False

# play a random game
def randomGame():
	resetBoard()
	continuePlay = True
	player = 1
	winner = 0

	while continuePlay:
		randomPlay(player)
		if checkWin(player):
			winner = player
			continuePlay = False
		if boardFull():
			continuePlay = False
		player = 2 if player == 1 else 1
	return winner

# check if player p has won the game
def checkWin(p):
	return any([checkRows(p), checkCols(p), checkDiagsFor(p), checkDiagsRev(p)])

# check each row for a win for player p
def checkRows(p):
	return any([checkRow(i,p) for i in range(numRows)])

# check each column for a win for player p
def checkCols(p):
	return any([checkCol(i,p) for i in range(numCols)]) 

# check each forward diagonal for a win for player p
def checkDiagsFor(p):
	return any([checkDiagFor(i,p) for i in range(dMin, dMax)])

# check each reverse diagonal for a win for player p
def checkDiagsRev(p):
	return any([checkDiagRev(i,p) for i in range(dMin, dMax)]) 

# check row with index i for a win for player p
def checkRow(i, p):
	string = np.array2string(board[i,:], separator='')[1:-1]
	return checkRCDWin(string,p)

# check column with index i for a win for player p
def checkCol(i, p):
	string = np.array2string(board[:,i], separator='')[1:-1] 
	return checkRCDWin(string,p)

# check forward diagonal with index i for a win for player p
def checkDiagFor(i,p):
	diagArray = np.diagonal(board, i)
	string = np.array2string(diagArray, separator='')[1:-1]
	return checkRCDWin(string,p)

# check reverse diagonal with index i for a win for player p
def checkDiagRev(i, p):
	diagArray = np.diagonal(np.fliplr(board), i) 
	string = np.array2string(diagArray, separator='')[1:-1]  
	return checkRCDWin(string,p)

# check if winstring is in given string
def checkRCDWin(string, p):
	winString = '1111' if p == 1 else '2222'
	return True if (winString in string) else False

# play a random game with verbose output
def playRandomGameVerbose():
	winner = randomGame()
	if winner == 0:
		print("no winner")
	else:
		print("player {} wins".format(winner))
	print(np.matrix(board))


# playRandomGameVerbose() # <--------------- TRY THIS ONCE CheckWin() WORKS
# Uncomment the line above to let the AI plays randomly against each other



# --------------- YOU MAY TEST YOUR CODE BELOW -------------------------------
board = np.array([[0,0,0, 0,0,0,0],
                  [0,0,0, 0,0,0,0],
                  [0,0,0, 0,0,0,0],
                  [0,0,0, 0,2,0,0],
                  [0,0,0, 0,2,0,0],
                  [0,0,2, 1,1,1,1]])

print(board)
print(checkRow(1,2))  # check 2nd row, if contains'2222'
print(checkRow(-1,1)) # check last row, if contains '1111'
print(checkRow(5,1))  # check last row, if contains '1111'
print(checkRows(1))  # check if any rows contain '1111'
print(checkRows(2))  # check if any rows contain '2222'
