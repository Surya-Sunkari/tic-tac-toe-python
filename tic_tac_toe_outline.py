
'''
STEPS

Quick Overview: 
    The purpose of this code is to provide you with an outline to code a Tic Tac Toe program in python.
The first four sections of code (start with 'def' keyword) are called functions. This means that if I call 
the name of the function in the main function (0 level identation), it will run the code that is in 
the function. You might also notice the 'from random import randint' line at the top of the code. This just means
that I am importing the function 'randint' from a python module called 'random', which is just a python program
that provides a bunch of methods related to creating randomized data. Above each function you will see a comment that
describes what the function does, as well as what it returns (if it returns something). Look through these comments and
understand what each funtion does. You don't need to understand how each function works, just know what it is capable of doing.
Outside of the functions  and steps that I provided, you will be doing all of the game logic and coding. I am providing these 
steps for those who want to work almost independently on this project, but I will also be going over this with the class, so don't
worry if you don't understand something. Let either me or Mrs. Munoz know if you have questions. Good luck!

1) create a 2d list named 'grid' that holds the index values of each position in the grid
2) create a variable named 'turn' that holds the boolean value of which player goes first
3) print out the grid with the index values (think about using the functions that I provided)
4) clear the grid so that the index values are no longer there (we want the grid to be empty at the start of the game)
5) create a variable 'winner' that is initialized to a default value to see if the game needs to continue to be played
6) start a while loop based on the 'winner' variable that continues looping as long as there is no winner and there is no tie
    7) at the start of each loop iteration, print the grid
    8) initialize two variables 'hold'(string) and 'ind'(integer) that are set to the default values '' and 0, respectively.
    9) create an if/else statement inside the while loop that is based on the player turn
        If it is player 1's turn, go through the if statement. Otherwise, go through the else statement.
        10) inside the if statement, create a boolean named 'valid' that describes if the index that the player selects
            is a valid index. If the index is not between 1-9 or the index value is already taken in the grid, then it
            is not a valid index.
        11) create another while loop that continues to iterate as long as there is not a valid index
            12) at the start of the while loop, initialize a variable named 'player_symbol' that holds a string value
                of either 'X' or 'O'. Player 1 should be 'X' and Player 2 should be 'O'.
            13) create a variable named 'ind' that gets the user input for the index that they want to put the player symbol in
            14) create another if/else statement that checks if the index is valid (in the range 1-9 and not taken in the grid)
                if the index is invalid, print 'Please enter a valid index'. Else, set the variable valid to True.
    15) in the else statement for the variable turn (one indentation), repeat steps 10-14 but for player 2 instead of player 1. 
        The code should be almost exactly the same.
    16) Figure out a way of translating the index (which is 1-9) into it's corresponding row and column in the grid variable.
        This can be done by using modulus (%) and floor division (//). Either google information about these operators or ask
        me (surya) or Mrs. Munoz about them if you don't understand what they do.
    17) assign the variable hold to the 2d grid variable at it's corresponding row and column
    18) switch the player turn. Because the 'turn' variable is a boolean, this can be done by using the 'not' keyword
    19) check to see if there's a winner using one of the methods that I provided and assign the returned value to
        to the variable 'winner' Remember, as long as winner == 0, the game should continue.
20) now that the game is over, print the grid one last time
21) create an if/elif/else statement based on whether winner == 1, winner == 2, or winner == 3. If winner == 1, let the user
    know that player 1 has won. Else if winner == 2, let the user know that player 2 has won. Else, that means that winner == 3
    and the game ended in a tie, so let the user know that the game ended in a tie.
22) You're done!
'''


from random import randint #used in createOrder() function to randomize if player1 or player2 goes first


#determines if player1 or player2 goes first by "flipping a coin."
#returns True if player1 goes first and False if player2 goes first.
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

#prints the elements in the tictactoe board in the proper tictactoe formatting
def printGrid():
    print()
    for i,row in enumerate(grid):
        line = "|".join(row)
        print(line)
        if(0<=i<=1):
            print("-----")
    print()

#clears the elements in the tictactoe board
def clearGrid():
    for row in range(0,3):
        for col in range(0,3):
            grid[row][col] = ' '

#checks to see if either player1 or player2 has won the game
#returns '0' if neither player has won yet, '1' if player1 wins, '2' if player2 wins, and '3' if there is a tie
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
    for row in grid:
        for i in row:
            if i == ' ':
                return 0
    return 3

'''
Start code under here! I initialized the grid variable so that there are no errors when
initially saving the code, but you'll need to change it to a 2d list so that it functions
as a 2d grid instead of a 1d list.
'''

grid = []


