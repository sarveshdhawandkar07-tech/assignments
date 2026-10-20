#  The grid of 8x8 size, in which a mouse is located at 1x1 and needs to reach an 8x8 place, finds out
#  the possible unique paths from its own location

# For finding the number of ways

def factorial(n):
    product = 1
    for i in range(n,0,-1):
        product *= i
    return product


def nCr(n,r):
    return factorial(n) / (factorial(n-r) * factorial(r))

n = int(input("Enter the value of n for nXn grid: "))
print(nCr((n-1)*2,n-1))


# Finding the actual paths
def find_paths(n,row,col,path,paths):
    if row == n-1  or col == n-1:
        paths.append(path)
        return

    if row < n-1:
        find_paths(n,row+1,col,path+'D',paths)

    if col < n-1:
        find_paths(n,row,col+1,path+'R',paths)

paths = []
find_paths(n,0,0,'',paths)
print(paths)
print(len(paths))
