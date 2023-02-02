#MINESWEEPER GAME ALEX EXERCISE 2
#CHANGES: RENAMED FILE, EXTENDED THE BOARD TO A 4X4 GRID 


#MY LAST COMMENTS: I got all functionality (including stopping the game when hitting bomb) to work.  
# I did not get exercise 3c) to work. I thought about stacking multiple if clauses, but that is not an ideal solution. Loop is the way to go.

#INITAlIZE VARIABLES

row = 0
col = 0 
GameOver = False 
number = [0,1,2]

#HIDDEN GAMEBOARD
board= [
    ["1" , "2" ,"*", "0"],
    ["0" ,"0" ,"2","1" ],
    ["1", "*", "2","0" ],
    ["0", "*", "2","2" ],       
]

#PLAYER INPUT BOARD 
board2= [
    ["-", "-", "-", "-"],
    ["-" ,"-" ,"-", "-"],
    ["-", "-", "-", "-"],
    ["-", "-", "-", "-"],    
    ]



#VISUALLY SHOWING BOARD
def printBoard(myboard):
    print(str(myboard[0][0]) + " | " + str(myboard[0][1]) + " | " + str(myboard[0][2])+ " | " + str(myboard[0][3]))
    print("--------------")
    print(str(myboard[1][0]) + " | " + str(myboard[1][1]) + " | " + str(myboard[1][2])+ " | " + str(myboard[1][3]))
    print("--------------")
    print(str(myboard[2][0]) + " | " + str(myboard[2][1]) + " | " + str(myboard[2][2])+ " | " + str(myboard[2][3]))
    print("--------------")
    print(str(myboard[3][0]) + " | " + str(myboard[3][1]) + " | " + str(myboard[3][2])+ " | " + str(myboard[3][3]))
    



        
#Uncover Neighbor Fields 
def uncoverfields(row,col):
    #uncover up
    if board[row-1][col] != "*":
        board2[row-1][col] == board[row-1][col]
    #uncover down
    if board[row+1][col] != "*":
        board2[row+1][col] == board[row+1][col]
    #uncover left
    if board[row][col-1] != "*":
        board2[row][col-1] == board[row][col-1]
    #uncover right
    if board[row][col+1] != "*":
        board2[row][col+1] == board[row][col+1]
    #uncover diagonal up left
    if board[row-1][col-1] != "*":
        board2[row-1][col-1] == board[row-1][col-1]
    #uncover diagonal up right
    if board[row-1][col+1] != "*":
        board2[row-1][col+1] == board[row-1][col+1]
    #diagonal down left 
    if board[row+1][col-1] != "*":
        board[row+1][col-1] == board[row+1][col-1]
    #diagonal down left 
    if board[row+1][col+1] != "*":
        board[row+1][col+1] == board[row+1][col+1]
        
        

#GET PLAYER INPUT

def playerinput(board2):
    global GameOver
    # Get user input
    wrongInput = True 
    while wrongInput:
        
        try:
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            # Check for wrong input
            if row > 3 or col > 3 or row < 0 or col < 0:
                print("Row and column need to be between 0 and 3. Please enter correct number.")
            else:
                wrongInput = False
        except:
            print("Please input number")
            
    # Check for bomb
    if board[row][col] == "*":
        board2[row][col] = board[row][col]
        print("Ups there is a bomb! You lost the game!")
        GameOver = True
        printBoard(board2)
        return GameOver
    
    # Check for non 0 number
    elif board[row][col] != 0 and board[row][col] != "*":
        board2[row][col] = board[row][col]
        
    # check for 0 number
    elif board[row][col] == 0:
        uncoverfields(row,col)
    
#Check for Win
def CheckForWin():
    global GameOver      
    if "-" not in board2:
        GameOver = True
        
    



#MASTERFUNCTION
def runGame():
    print(" ")
    print("Welcome to the game minesweeper! This is the blank gamefield that you need to uncover now! Pay attention to the bombs!")
    print("")
    # Run game
    while GameOver == False:
        printBoard(board2)
        playerinput(board2)
        uncoverfields(row,col)
        #CheckForWin()
    
runGame()