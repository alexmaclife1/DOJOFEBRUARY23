#MINESWEEPER GAME ALEX EXERCISE 2
#CHANGES: RENAMED FILE, EXTENDED THE BOARD TO A 4X4 GRID 


#INITAlIZE VARIABLES



#CREATE GAMEBOARD
board= [
    ["." , "." ,"*", "."],
    ["." ,"." ,".","." ],
    [".", "*", ".","." ],
    [".", "*", ".","." ],       
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
    

#OUTPUT BOARD HOW MANY MINES ARE IN THE NEIGHBORHOOD OF EACH FIELD 
board2= [
    [0, 0, 0, 0],
    [0 ,0 ,0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],    
    ]

#COUNT NEIGHBORING MINES OF EACH POSITION

def countmines(row, col):
    count = 0
    
    #checkifonpositionisamine
    if board[row][col] != "*":
        
    
        # check up 
        if row - 1 >= 0 and board[row -1][col] == "*":
            count += 1 
        
        # check down 
    
        if row +1 <= 3 and board[row +1][col] == "*":
            count += 1
        
        # check left 
        if col - 1 >= 0 and board[row][col -1] == "*":
            count += 1 
        
        # check right 
        if col + 1 <= 3 and board[row][col + 1] == "*":
            count += 1 
        
        #check diagonal up left
        if col -1 >= 0 and row -1 >= 0 and board[row -1][col-1] == "*": 
            count += 1  
    
        #check diagonal up right 
        if col +1 <=3 and row - 1 >= 0 and board[row-1][col+1] == "*":
            count += 1  
    

        #check diagonal down left
        if col -1 >= 0 and row +1 <= 3 and board[row +1][col-1] == "*": 
            count += 1
    
        
        #check diagonal down right 
        if col +1 <=3 and row + 1 <= 3 and board[row +1][col+1] == "*":
            count += 1
            
            
        #assign new value 
        board2[row][col] = count
        
    else:
        board2[row][col] = "*"


    
            
#MASTERFUNCTION
    
print("Welcome to the game minesweeper!")
    # ITERATE OVER EACH CELL
for i in range(len(board)):
    for j in range(len(board[i])):      
        countmines(i,j)
        
printBoard(board2)
