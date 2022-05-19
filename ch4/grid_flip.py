# Chpater 4
# Copy the previous grid value, and write code that uses it to print the image 
#   - the image is rotated, from (x,y) to (y,x)

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def run():
    rowSize = len(grid[0])

    for y in range(rowSize):
        for x in range(len(grid)):
            print(grid[x][y], end=' ')
        
        print('\n')

run()