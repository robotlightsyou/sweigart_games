#!/usr/bin/python3

'''
Barca by Al Sweigart
A chess-variamt where each player's mice, lions, and elephants try to
occupy the watering holes near the center of the board.

Barca was invented by Andrew Caldwell http://playbarca.com
'''

import sys

# set up the constants
SQUARE_PLAYER = "Square Player"
ROUND_PLAYER = "Round Player"
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

# The strings to display the board
SQUARE_MOUSE = '[Mo]'
SQUARE_LION = '[Li]'
SQUARE_ELEPHANT = '[El]'
ROUND_MOUSE = '[Mo]'
ROUND_LION = '[Li]'
ROUND_ELEPHANT = '[El]'

LAND = '__'
WATER = '~~'

# PLAYER_PIECES[x] is a tuple of the player's pieces:
PLAYER_PIECES = {
    SQUARE_PLAYER: (SQUARE_MOUSE, SQUARE_LION, SQUARE_ELEPHANT),
    ROUND_PLAYER: (ROUND_MOUSE, ROUND_LION, ROUND_ELEPHANT)
}

# FEARED_PIECE[x] is te piece tjat x is afraid of:
FEARED_PIECE = {SQUARE_MOUSE: ROUND_LION,
                SQUARE_LION: ROUND_ELEPHANT,
                SQUARE_ELEPHANT: ROUND_MOUSE,
                ROUND_MOUSE: SQUARE_LION,
                ROUND_LION: SQUARE_ELEPHANT,
                ROUND_ELEPHANT: SQUARE_MOUSE}

# Change to x and y for moving in different directions
UPLEFT = (-1, -1)
UP = (0, -1)
UPRIGHT = (1, -1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DOWNLEFT = (-1, 1)
DOWN = (0, 1)
DOWNRIGHT = (1, 1)
CARDINAL_DIRECTIONS = (UP, LEFT, RIGHT, DOWN)
DIAGONAL_DIRECTIONS = (UPLEFT, UPRIGHT, DOWNLEFT, DOWNRIGHT)
ALL_DIRECTIONS = CARDINAL_DIRECTIONS + DIAGONAL_DIRECTIONS

# @ANIMAL_DIRECTIONS[x] is a tuple of directions that x can move:
ANIMAL_DIRECTIONS = {SQUARE_MOUSE: CARDINAL_DIRECTIONS,
                     SQUARE_LION: DIAGONAL_DIRECTIONS,
                     SQUARE_ELEPHANT: ALL_DIRECTIONS,
                     ROUND_MOUSE: CARDINAL_DIRECTIONS,
                     ROUND_LION: DIAGONAL_DIRECTIONS,
                     ROUND_ELEPHANT: ALL_DIRECTIONS}

# FEARED ANIMAL_DIRECTIONS[x] is a tuplw of directions that the piece
# that is afraid of can move:
FEARED_ANIMAL_DIRECTIONS = {SQUARE_MOUSE: DIAGONAL_DIRECTIONS,
                            SQUARE_LION: ALL_DIRECTIONS,
                            SQUARE_ELEPHANT: CARDINAL_DIRECTIONS,
                            ROUND_MOUSE: DIAGONAL_DIRECTIONS,
                            ROUND_LION: ALL_DIRECTIONS,
                            ROUND_ELEPHANT: CARDINAL_DIRECTIONS}

EMPTY_SPACE = 'empty'
WATERING_HOLES = ((3, 3), (6, 3), (3, 5), (6, 6))


def main():
    print("""Barca, by Al Sweigart
Barca is a chess variant where each player has two mice (which move like
chess rooks), lions(bishops), and elephants(queens). Thr objext of the
game is to occupy three of the four watering hole spaces near the
middle of the board.

Mice are afraid of lions, lins are afraid of elephants, and elephants
are afraid of mice. Afraid animals are in"check", and mist move away
before othe animals can move.

Barca was invented by Andrew Caldwell
""")

    input("Press Enter to begin...")

    turn = ROUND_PLAYER
    game_board = get_new_board()
    while True:
        display_board(game_board)

        display_move(turn, game_board)
        if is_winner(turn, game_board):
            print(turn, " has won!")
            sys.exit()

        # Switch to the next player
        if turn == SQUARE_PLAYER:
            turn = ROUND_PLAYER
        elif turn == ROUND_PLAYER:
            turn = SQUARE_PLAYER


def get_new_board():
    '''Return a dict that represents the board. The keys are (x,y)
    integer tuples for the positions and the values are one of the animal
    piece constants e.g. SQUARE_ELEPHANT or ROUND_LION'''
    # First set the board completely empty:
    board = {}
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = EMPTY_SPACE
