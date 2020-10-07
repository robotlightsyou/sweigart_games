""" Conway's Game of Life, by Al Sweigart
The classic cellular automat simulation. Press Ctrl-C to stop.
More info at wikipedia
Tags: short, artistic, simulation"""

__version__ = 0

import copy, random, sys, time

#set up the constants
WIDTH = 79
HEIGHT = 20

# Try changing  alive to a different character
ALIVE = 'O'
DEAD = ' '

#The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x,y) tuples and their values are one of the alive
# or dead values
nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            nextCells[(x,y)] = ALIVE
        else:
            nextCells[(x,y)] = DEAD

while True:

    print('\n' * 50)
    cells = copy.deepcopy(nextCells)

    # Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[(x, y)], end='')  # Print the # or space.
        print()  # Print a newline at the end of the row.
    print('Press Ctrl-C to quit.')

    for x in range(WIDTH):
        for y in range(HEIGHT):
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            numNeighbors = 0
            if cells[(left,above)] == ALIVE:
                numNeighbors += 1
            if cells[(x, above)] == ALIVE:
                numNeighbors += 1
            if cells[(right, above)] == ALIVE:
                numNeighbors += 1
            if cells[(left, y)] == ALIVE:
                numNeighbors += 1
            if cells[(right, y)] == ALIVE:
                numNeighbors += 1
            if cells[(left, below)] == ALIVE:
                numNeighbors += 1
            if cells[(x, below)] == ALIVE:
                numNeighbors += 1
            if cells[(right, below)] == ALIVE:
                numNeighbors += 1

            if cells[(x,y)] == ALIVE and (numNeighbors == 2
                                          or numNeighbors ==3):
                nextCells[(x,y)] = ALIVE
            elif cells[(x,y)] == DEAD and numNeighbors == 3:
                nextCells[(x,y)] = ALIVE
            else:
                nextCells[(x,y)] = DEAD

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nConway's Game of Life")
        print("By Al Sweigart")
        sys.exit()

