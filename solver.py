board = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
    ]



def solve(bo):
    
    find = find_empty(bo)
    if not find:            # If no empty spaces are found, return True because board is solved
        return True
    else:
        row, col = find     # Save returned position of find to row, col
   
        
    for i in range(1, 10):
        if valid(bo, i, (row, col)): # check if i is valid at the given position
            bo[row][col] = i         # if it is valid, save it to the board at that position
            
            if solve(bo):       # Try to fill in the next empty spot, then the next, then the next..
                return True
            
            bo[row][col] = 0    # If you can't fill the next empty spot, set it back to zero and go back to the for loop and change
                                # the previous spot to the next possible value and then see if you can proceed to fill the rest of 
                                # the empty spots. This recursive backtracking continues until there are no empty spaces and solve(bo) 
                                # returns true. 
    
    return False



def valid(bo, num, pos):
    
    # Check Row
    for i in range(len(bo[0])):                     # for each item in row, 
        if bo[pos[0]][i] == num and pos[1] != i:    # check if item == num; except for the index at which we just placed num 
            return False                            # If the number already exists in the row, we can't use it, therefore return False
            
    # Check Column
    for i in range(len(bo)):                        # for each item in column,
        if bo[i][pos[1]] == num and pos[0] != i:     # check if item == num; except for the index at which we just placed num
            return False                            # If the number already exists in column, return False
    
    # Check box
    box_x = pos[1]//3
    box_y = pos[0]//3
    
    for i in range(box_y * 3, box_y * 3 + 3):       # For each row in the box,
        for j in range(box_x * 3, box_x * 3 + 3):   # check each item in the row.
            if bo[i][j] == num and (i, j) != pos:   # If any item == num; except for the index where we just placed num,
                return False                        # return false

    return True
    
def print_board(bo):
    
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")
        
        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ",end="")
                

def find_empty(bo):
    
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
    return None


# ~ print_board(board)
# ~ solve(board)
# ~ print("\n--------------------\n")
# ~ print_board(board)


