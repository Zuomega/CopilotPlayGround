# create a 10 by 10 grid
# and play life game

import random
import time
import sys

# create a 10 by 10 grid
# and play life game
def main():
    # create a 10 by 10 grid
    grid = []
    for i in range(10):
        grid.append([])
        for j in range(10):
            grid[i].append(0)

    # fill the grid with random values
    for i in range(10):
        for j in range(10):
            grid[i][j] = random.randint(0, 1)

    # print the grid
    print_grid(grid)

    # play the game
    play_game(grid)
    
# print the grid
def print_grid(grid):
    # clear terminal
    sys.stdout.write("\x1b[2J\x1b[H")

    for i in range(10):
        for j in range(10):
            # decorate print output
            if grid[i][j] == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# play the game
def play_game(grid):
    while True:
        # print the grid
        print_grid(grid)

        # get the next grid
        grid = get_next_grid(grid)

        # wait for 1 second
        time.sleep(1)

# get the next grid
def get_next_grid(grid):
    # create a 10 by 10 grid
    next_grid = []
    for i in range(10):
        next_grid.append([])
        for j in range(10):
            next_grid[i].append(0)

    # fill the grid with random values
    for i in range(10):
        for j in range(10):
            # get the number of neighbors
            neighbors = get_neighbors(grid, i, j)

            # get the next value
            if grid[i][j] == 1:
                if neighbors < 2:
                    next_grid[i][j] = 0
                elif neighbors == 2 or neighbors == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0
            else:
                if neighbors == 3:
                    next_grid[i][j] = 1
                else:
                    next_grid[i][j] = 0

    # return the next grid
    return next_grid


# get the number of neighbors
def get_neighbors(grid, i, j):
    # get the number of neighbors
    neighbors = 0

    # check the neighbors
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            if i + x < 0 or i + x > 9:
                continue
            if j + y < 0 or j + y > 9:
                continue
            if grid[i + x][j + y] == 1:
                neighbors += 1

    # return the number of neighbors
    return neighbors

# call the main function
main()