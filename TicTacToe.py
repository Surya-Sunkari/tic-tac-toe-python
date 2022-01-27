# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 13:35:54 2022

@author: 100031985
"""



#tictactoe, my solution

#figure out order
#print out grid and explain indexes
#ask for input (check if valid)
#clear grid, print new grid, check for winner, switch turns



from random import randint

def createOrder():
    print('You are player 1. I will flip a coin to determine who goes first.')
    s = ""
    
    while s not in ['h', 't']:
        s = input('Heads or Tails? (type h or t): ').lower()
    if s == 'h':
        print('You picked heads.')
    else:
        print('You picked tails.')
        
    print('\nNow flipping the coin...')
    rand = randint(0,1)
    if rand == 0:
        print('The coin landed on heads!')
        p1first = s == 'h'
    else:
        print('The coin landed on tails!')
        p1first = s == 't'
        
    if p1first:
        print('\nPlayer 1 goes first.')
        return True
    else:
        print('\nPlayer 2 goes first.')
        return False

def printGrid():
    print()
    for i,row in enumerate(grid):
        line = "|".join(row)
        print(line)
        if(0<=i<=1):
            print("-----")
    print()
    
def clearGrid():
    for row in range(0,3):
        for col in range(0,3):
            grid[row][col] = ' '
    
def checkWinner():
    for row in grid:
        if "".join(row) == "XXX":
            return 1
        elif "".join(row) == 'OOO':
            return 2
    for i in range(0,3):
        if grid[0][i] == grid[1][i] == grid[2][i]:
            if grid[0][i] == 'X':
                return 1
            elif grid[0][i] == 'O':
                return 2
    if grid[0][0] == grid[1][1] == grid[2][2]:
        if grid[0][0] == 'X':
            return 1
        elif grid[0][0] == 'O':
            return 2
    if grid[2][0] == grid[1][1] == grid[0][2]:
        if grid[2][0] == 'X':
            return 1
        elif grid[2][0] == 'O':
            return 2
    return 0


turn = createOrder() #true means player 1 turn, and vice versa
print('Here is the grid and the indexes associated with each box:')
grid = [['1','2','3'],['4','5','6'],['7','8','9']]
printGrid()
clearGrid()

winner = 0
while(winner == 0):
    printGrid()
    hold = ''
    ind = 0
    if turn:
        valid = False
        print('Player 1, it is your turn. Please input an index.')
        while not valid:
            hold = 'X'
            ind = int(input('Index: '))
            if(ind < 1 or ind > 9 or grid[(ind-1)//3][(ind-1)%3] != ' '):
                valid = False
                print('Please enter a valid index')
            else:
                valid = True
    else:
        valid = False
        print('Player 2, it is your turn. Please input an index.')
        while not valid:
            hold = 'O'
            ind = int(input('Index: '))
            if(ind < 1 or ind > 9 or grid[(ind-1)//3][(ind-1)%3] != ' '):
                valid = False
                print('Please enter a valid index')
            else:
                valid = True
    
    row = (ind-1)//3
    col = (ind-1)%3
    grid[row][col] = hold
    turn = not turn
    winner = checkWinner()
printGrid()


if winner == 1:
    print('Player 1 wins! Good game!')
else:
    print('Player 2 wins! Good game!')
