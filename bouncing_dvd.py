#!/usr/bin/python3

'''
DOCSTRING: Bouncing DVD Logo by Ak Sweigart
A bouncing DVD logo animation. You have to be "of a certain age" to
appreciate this. Press Ctrl-C to stop.

NOTE: Do not resize the terminal window while this program is running.
Tags: short, artistic, bext, terminal
'''
__version__ = 0
import sys, random, time

try:
    import bext
except ImportError:
    print("""This progra requires the bext module, which you
          can install by following the instructions at
          https://pypi.org/project/bext/""")
    sys.exit()

#set up th e constants
WIDTH, HEIGHT = bext.size()
#We can't print to the last column on Winsows without it adding a
#newline automatically, so reduce the width by one
WIDTH -= 1

NUMBER_OF_LOGOS = 5  #TRY CHANGING THIS TO 1 OR 100
PAUSE_AMOUNT = 0.2
#(!) TRY CHANGING THIS LIST TO FEWER OPTIONS
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

#key names for logo dictiionaries:
COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()

    #generate some logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, (WIDTH - 4)),
                      Y: random.randint(1, HEIGHT - 1),
                      DIR: random.choice(DIRECTIONS)})
        if logos[-1][X] % 2 == 1:
            #make sure X is even so it can hit the corner
            logos[-1][X] -= 1

    cornerBounces = 0
    while True:
        for logo in logos:
            #erase the logo's current position
            bext.goto(logo[X], logo[Y])
            print('  ', end='')

            original_direction = logo[DIR]

            #see if the logo bounces off the corners
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                cornerBounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] == DOWN_LEFT
                cornerBounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] == UP_LEFT
                cornerBounces += 1

            # See if the logo bounces off the left edge:
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the right edge:
            # (WIDTH - 3 because 'DVD' has 3 letters.)
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT

            # See if the logo bounces off the top edge:
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT

            # See if the logo bounces off the bottom edge:
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT

            if logo[DIR] != original_direction:
                # Change color when the logo bounces:
                logo[COLOR] = random.choice(COLORS)

            #move the logo. (X moves by 2 because the terminal
            #vharacers are twice as tall as they are wide)
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            elif logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            elif logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            elif logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1

        #display the number of corner bounces
        bext.goto(5,0)
        bext.fg('white')
        print('Corner bounces:', cornerBounces, end='')

        for logo in logos:
            #draw the logos at their new location
            bext.goto(logo[X], logo[Y])
            bext.fg(logo[COLOR])
            print('DVD', end='')

        bext.goto(0,0)
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo, by Al Sweigart')
        sys.exit()


