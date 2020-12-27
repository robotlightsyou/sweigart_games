""" Conway's Game of Life 2
This version of Conways's Game of Life uses squares instead of text
characters.
The classic cellular automata simulation. Press Ctrl-C to stop.
Do not resize the terminal window while program is running.
Tags: large, artistic, simulation, bext, terminal"""

__version__ = 0
import random
import sys
import time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install from pypi')
    sys.exit()

PAUSE_LENGTH = 0.25

WIDTH, HEIGHT = bext.size()
HEIGHT = (HEIGHT - 1) * 2

WIDTH -= 1
TOP_BLOCK = chr(9600)
BOTTOM_BLOCK = chr(9604)
FULL_BLOCK = chr(9608)


def main():
    print("Conway's Game of Life")
    print("by Al Sweigart")
    print("Press Ctrl-C to stop")
    time.sleep(3)

    currentCells = {}
    nextCells = {}
    previousCells = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if random.randint(0, 1) == 0:
                nextCells[x, y] = True

    bext.clear()

    while True:
        previousCells = currentCells
        currentCells = nextCells

        for y in range(0, HEIGHT, 2):
            for x in range(WIDTH):
                prevTopHalf = previousCells.get((x, y), False)
                curTopHalf = currentCells.get((x, y), False)
                topHalfHasChanged = prevTopHalf != curTopHalf

                prevBottomHalf = previousCells.get((x, y + 1), False)
                curBottomHalf = currentCells.get((x, y + 1), False)
                bottomHalfHasChanged = prevBottomHalf != curBottomHalf
                if bottomHalfHasChanged or topHalfHasChanged:
                    bext.goto(x, y//2)
                    if curTopHalf and curBottomHalf:
                        print(FULL_BLOCK, end='')
                    elif curTopHalf and not curBottomHalf:
                        print(TOP_BLOCK, end='')
                    elif not curTopHalf and curBottomHalf:
                        print(BOTTOM_BLOCK, end='')
                    elif not curTopHalf and not curBottomHalf:
                        print(' ', end='')

            print()
        print('Press Ctrl-C to quit.', end='', flush=True)

        nextCells = {}
        for x in range(WIDTH):
            for y in range(HEIGHT):
                # get neighboring coordinates
                leftCoord = (x - 1) % WIDTH
                rightCoord = (x + 1) % WIDTH
                topCoord = (x - 1) % HEIGHT
                bottomCoord = (x + 1) % HEIGHT

                # Count number of living neighbors
                numNeighbors = 0
                if (leftCoord, topCoord) in currentCells:
                    numNeighbors += 1
                if (x, topCoord) in currentCells:
                    numNeighbors += 1
                if (rightCoord, topCoord) in currentCells:
                    numNeighbors += 1
                if (leftCoord, y) in currentCells:
                    numNeighbors += 1
                if (rightCoord, y) in currentCells:
                    numNeighbors += 1
                if (leftCoord, bottomCoord) in currentCells:
                    numNeighbors += 1
                if (x, bottomCoord) in currentCells:
                    numNeighbors += 1
                if (rightCoord, bottomCoord) in currentCells:
                    numNeighbors += 1

                if currentCells.get((x, y), False):
                    if numNeighbors in (2, 3):
                        nextCells[x, y] = True
                else:
                    if numNeighbors == 3:
                        nextCells[x, y] = True

        time.sleep(PAUSE_LENGTH)


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        sys.exit()

# test edit
