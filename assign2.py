# Stack Approach
n = int(input())
row_move = [-2,-1,1,2,2,1,-1,-2]
col_move = [1,2,2,1,-1,-2,-2,-1]

def create_grid(n):
    return [[-1 for i in range(n)] for j in range(n)]

def show_grid(grid) :
    for row in grid:
        for value in row:
            print(value,end=" ")
        print()

grid = create_grid(n)
show_grid(grid)

def valid_move(grid,row,col):
    return 0<=row<n and 0<=col<n and grid[row][col] == -1 

def KnightTour(grid,start_row,start_col,count,stack):
    while count != n*n :
        for i in range(stack[-1][2],8):
            next_row = start_row + row_move[i]
            next_col = start_col + col_move[i]

            if valid_move(grid,next_row,next_col):

                stack[-1] = (start_row,start_col,i+1) # giving the updated direction index to the move at the top
                grid[next_row][next_col] = count
                stack.append((next_row,next_col,0)) # default direction index is 0
                count += 1

                start_row = next_row
                start_col = next_col
                break
        else:
            popped = stack.pop()
            grid[popped[0]][popped[1]] = -1
            count -= 1
            if stack :
                start_row = stack[-1][0]
                start_col = stack[-1][1]
            else:
                return False
    return True


stack = [(n//2,n//2,0)]
grid[n//2][n//2] = 0
if KnightTour(grid,n//2,n//2,1,stack):
    show_grid(grid)
    print("Solution Successful")
else:
    print("Solution does not exist")
