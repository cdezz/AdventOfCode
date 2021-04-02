import pprint
with open('input.txt', 'r') as fin:
    fin = fin.readlines()

grid = [l.strip() for l in fin]
height, width = len(grid), len(grid[0]) 


trees = 0
col = 0

from itertools import count

print("GRid: ", grid)

print(list(zip(range(height), count(0, 3))))

trees = 0
for row, col in zip(range(height), count(0, 3)):
    if grid[row][col % width] == '#':
        trees += 1

print('Part 1:', trees)

###############################################3

def tree_count(x, y=1):

    grid = [l.strip() for l in fin]
    height, width = len(grid), len(grid[0])

    trees = 0

    for row, col in zip(range(0, height, y), count(0, x)):
        if grid[row][col % width] == '#':
            trees += 1
    
    return trees


    # Right 1, down 1.
    # Right 3, down 1. (This is the slope you already checked.)
    # Right 5, down 1.
    # Right 7, down 1.
    # Right 1, down 2.


mult_trees = tree_count(x=1) * tree_count(x=3) * tree_count(x=5) * tree_count(x=7) * tree_count(x=1,y=2)

print(mult_trees)