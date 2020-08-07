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

    # Next, place the pieces on their starting positions:
    board[(4, 0)] = board[(5, 0)] = SQUARE_ELEPHANT
    board[(3, 1)] = board[(6, 1)] = SQUARE_ELEPHANT
    board[(4, 1)] = board[(5, 1)] = SQUARE_ELEPHANT
    board[(4, 9)] = board[(5, 9)] = SQUARE_ELEPHANT
    board[(3, 8)] = board[(6, 8)] = SQUARE_ELEPHANT
    board[(4, 8)] = board[(5, 8)] = SQUARE_ELEPHANT

    return board


def display_board(board):
    '''display the board to the screen'''
    # a list og arguments t pass to format() to fill the board
    # template string's {}
    spaces = []
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[(x, y)] == EMPTY_SPACE:
                # this space is an empty land or water hole
                if board(x, y) in WATERING_HOLES:
                    spaces.append(WATER)
                else:
                    spaces.append(LAND)
            else:
                # this space has an animal piece on it
                spaces.append(get_Animal_String(board, x, y))

    print("""
 +--A---B---C---D---E---F---G---H---I---J-+
 |                                        |
 1{}{}{}{}{}{}{}{}{}{}1
 |                                        |
 2{}{}{}{}{}{}{}{}{}{}2
 |                                        |
 3{}{}{}{}{}{}{}{}{}{}3
 |                                        |
 4{}{}{}{}{}{}{}{}{}{}4
 |                                        |
 5{}{}{}{}{}{}{}{}{}{}5
 |                                        |
 6{}{}{}{}{}{}{}{}{}{}6
 |                                        |
 7{}{}{}{}{}{}{}{}{}{}7
 |                                        |
 8{}{}{}{}{}{}{}{}{}{}8
 |                                        |
 9{}{}{}{}{}{}{}{}{}{}9
 |                                        |
10{}{}{}{}{}{}{}{}{}{}10
 +--A---B---C---D---E---F---G---H---I---J-+""".format(*spaces))


def get_Animal_String(board, x, y):
    '''returns the 4-character string od the animal for te piece at (x,y)
    on the board. This string weill end with a ! ig the piece
    os afraid of another animl on the bvoard.'''
    checkX, checkY = x, y  # start at the piece's location
    while True:
        # The space check moves further in the current direction:
        checkX += offsetX
        checkY += offsetY
        if not is_on_board(checkX, checkY):
            break  # this space is off board, so stop checking
        if board[(checkX, checkY)] == FEARED_PIECE[piece]:
            return piece[0:-1] + '!'  # This piece is afraid
        elif board[(checkX, checkY)] != EMPTY_SPACE:
            break  # another animal is blockintg any feared animals
        elif board[(checkX, checkY)] == EMPTY_SPACE:
            continue  # this space is empty, so keep checking
    return piece  # this piece is not afraid


def is_on_board(player, board):
    '''returns True if (x, y) is a position on the board, otherwise
    returns False'''
    return (0 <= x < BOARD_WIDTH) and (0 <= y < BOARD_HEIGHT)


def do_player_move(player, board):
    '''Ask the player for their move, and if it is valid, carry it out
    on the board.'''
    valid_moves = get_piece_movements(player, board)
    assert len(valid_moves) > 0

    valid_moves_in_A1 = []
    for x, y in valid_moves.keys():
        valid_moves_in_A1.append(xy_to_A1(x, y))
        print(player + ', select a piece to move (or QUIT):',
              ', '.join(valid_moves_in_A1))
        while True:
            # keep asking the player unyil they select a valid piece
            response = input(">").upper()
            if response == 'QUIT':
                print("Thanks for playing!")
                sys.exit()
            if response in valid_moves_in_A1:
                move_from = A1_to_xy(response)
                break  # player has selected a valid piece
            print('Please select one of the given pieces.')

    move_to_in_A1 = []
    for x, y in valid_moves[move_from]:
        move_to_in_A1.append(xy_to_A1(x, y))
    move_from_str = get_Animal_String(board, move_from[0], move_from[1])
    print('Select where to move {}: {}'.format(
        move_from_str, ', '.join(move_to_in_A1)))
    while True:
        # keep asking player until they select a valid move.
        response = input(">")
        if response == 'QUIT':
            print("Thanks for playing!")
            sys.exit()
        if response in valid_moves_in_A1:
            move_to = A1_to_xy(response)
            break  # player has selected a valid piece
        print('Please select one of the given pieces.')

    # carry out the player's move
    move_piece(move_from, move_to, board)


def move_piece(move_from, move_to, board):
    '''Move the piece at move_from on the board to move_to. These are
    (x, y) integer tuples'''
    board[move_to]=board[move_from]  # place a piece at 'move_to'
    board[move_from]=EMPTY_SPACE  # blank space in original location

def get_piece_movements(player, board):
    '''Return a list of (x, y) tuples representing spaces that hold
    pieces that the player can move according to Barca rules.'''

    #Figure out which pieces can move(afraid ones must move first).
    afraid_piece_positions = []
    unafraid_piece_positions = []
    for y in range(BOARD_HEIGHT):
        for x in range(BOARD_WIDTH):
            if board[(x, y)] in PLAYER_PIECES[player]:
                #check if the animal is afraid or not
                if get_Animal_String(board, x, y).endswith('!'):
                    afraid_piece_positions.append((x, y))
                else:
                    unafraid_piece_positions.append((x, y))

    if len(afraid_piece_positions) != 0:
        #unafraid pieces can't move if there are afraid pieces.
        unafraid_piece_positions = []

    #go through all of the pieces to get their valid moves

    #the keys are (x, y) tuples, values are list of (x, y) tuples
    #of where thay can move
    valid_moves = {}
    for piece_position in afraid_piece_positions + unafraid_piece_positions:
        x, y = piece_position
        piece = board[(x, y)]
        #this list will contain this piece's valid move locations
        valid_moves[(x, y)] = []
        for offsetX, offsetY in ANIMAL_DIRECTIONS[piece]:
            checkX, checkY = x, y #start with the piece's location
            while True:
                #the space check moves further in the current direction:
                checkX += offsetX
                checkY += offsetY
                if not is_on_board(checkX, checkY) or board[(checkX, checkY)] != EMPTY_SPACE:
                    #this space is off board or blocked by another piece
                    #so stop checking
                    break
                elif board[(checkX, checkY)] == EMPTY_SPACE:
                    valid_moves[(x, y)].append((checkX, checkY))

        #remove the possible moves that would place the piece in fear
        for piece_position, possible_moves in valid_moves.items():
            x, y = piece_position
            piece = boaed[(x, y)]
            
            #list of (x, y) tuples where this piece doesn't want to move
            feared_positions = []
            for move_to_X, move_to_Y in possible_moves:
                #simulate what would happen if we move the piece
                #to move_to_X,move_to_Y
                move_piece(piece_position, (move_to_X, move_to_Y), board)
                if get_Animal_String(board, move_to_X, move_to_Y).endswith('!'):
                    #moving here would make the piece afraid
                    feared_positions.append((move_to_X, move_to_Y))
                #move the piece back to the original space
                move_piece((move_to_X,move_to_Y), piece_position, board)
            if len(possible_moves) != len(feared_positions):
                #some of the moves will make this piece afraid, so remove
                #those from the possible moves. (If all of the moves were
                #feared, then the piece isn't restricted at all.)
                for fearedX, fearedY in feared_positions:
                    valid_moves[piece_position].remove((fearedX, fearedY))
        return valid_moves

def xy_to_A1(x, y):
    '''convert (x, y) coordinates to user friendly coordinates'''
    return chr(x + 65) + str(y + 1)

def A1_to_xy(space):
    '''convert user firendly coordinates to x,y'''
    column = space[0]
    row = space[1:]
    return (ord(column) -65, int(row) - 1)

def is_winner(player, board):
    '''return True id te player occupies three of the four watering 
    holes on the board.'''
    square_claims = 0
    round_claims = 0
    for space in WATERING_HOLES:
        if board[space] in (SQUARE_MOUSE, SQUARE_LION, SQUARE_ELEPHANT):
            square_claims += 1
        elif board[space] in (ROUND_MOUSE, ROUND_LION, ROUND_ELEPHANT):
            round_claims += 1

    if player == SQUARE_PLAYER and square_claims >= 3:
        return True
    elif player == ROUND_PLAYER and round_claims >= 3:
        return True
    else:
        return False

if __name__ == '__main__':
    main()


