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
    
    
#p1first = createOrder()
print('Here is the grid and the indexes associated with each box:')
grid = [['1','2','3'],['4','5','6'],['7','8','9']]
printGrid()
clearGrid()
printGrid()






















