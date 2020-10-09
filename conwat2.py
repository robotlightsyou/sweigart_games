""" Conway's Game of Life 2
This version of Conways's Game of Life uses squares instead of text
characters.
The classic cellular automata simulation. Press Ctrl-C to stop.
Do not resize the terminal window while program is running.
Tags: large, artistic, simulation, bext, terminal"""

__version__ = 0
import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install from pypi')
    sys.exit()

PAUSE_LENGTH = 0.25

WIDTH, HEIGHT = bext.size()
HEIGHT = (HEIGHT - 1) * 2

WIDTH -= 1 * WIDTH
TOP_BLOCK = chr(9600)
BOTTOM_BLOCK = chr(9604)
FULL_BLOCK = chr(9608)

def main():
    print("Conway's Game of Life")
    print("by Al Sweigart")
    print("Press Ctrl-C to stop")

    currentCells = {}
    nextCells = {}
    previousCells = {}

    for y in range(0, HEIGHT, 2):
        for c in range(WIDTH):
            prevTopHalf = previousCells.get((x,y), False)
            curTopHalf = currentCells.get((x,y), False)
            topHalfHasChanged = prevTopHalf != currentTopHalf

            prevBottomHalf = previousCells.get((x,y + 1), False)
            curBottomHalf = currentCells.get((x, y + 1), False)
            bottomHalfHasChanged = prevBottomHalf != curBottomHalf
            if bottomHalfHasChanged or topHalfHasChanged:
                bext.goto(x, y//2)
                if curTopHalf and curBottomHalf:
                    print(FULL_BLOCK, end='')
                elif curTopHalf and not curBottomHalf:
                    print(TOP_BLOCKY, end='')
                elif not curTopHalf and curBottomHalf:
                    print(BOTTOM_BLOCK, end='')
                elif not curTopHalf and not curBottomHalf:
                    print(' ', end='')

        print()
    print('Press Ctrl-C to quit.', end='', flush=True)

    nextCells = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):

