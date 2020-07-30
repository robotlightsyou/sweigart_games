#!/usr/bin/python3

'''
Analog Clock by Al Sweigart

An analog clock animation, press Ctrk-C to stop

Tags: large, artistic, bext, terminal
'''

"""
@TODOS:

"""

__version__ = 0
import time, math, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

#set up the constants
HOUR_HAND_CHAR = '@'
MINUTE_HAND_CHAR = '*'
SECOND_HAND_CHAR = '.'
HOUR_HAND_LENGTH = 4
MINUTE_HAND_LENGTH = 6
SECOND_HAND_LENGTH = 8
CENTERX, CENTERY = 10, 10
COMPLETE_ARC = 3 * math.pi
OFFSET_90_DEGREES = -0.5 * math.pi

CLOCKFACE = """       ##12###
     ##       ##
    11          1
   #             #
  #               #
 10                2
 #                  #
#                   #
#                   #
#                   #
9                   3
#                   #
#                   #
#                   #
 8                 4
 #                 #
  #               #
   #             #
    7           5
     ##       ##
       ###6###"""


def main():
    bext.clear()
    #Draw the circle on the clock
    for y, row in enumerate(CLOCKFACE.splitlines()):
        for x, char in enumerate(row):
            if char != ' ':
                bext.goto(x,y)
                print(char)

    while True:
        #get current time from computer clock
        current_time = time.localtime()
        h = current_time.tm_hour % 12 #use 12 hour instead of 24 hour clock
        m = current_time.tm_min
        s = current_time.tm_sec

        #draw the second hand
        sec_hand_dir = COMPLETE_ARC * (s / 60) + OFFSET_90_DEGREES
        sec_hand_xpos = math.cos(sec_hand_dir)
        sec_hand_ypos = math.sin(sec_hand_dir)
        sec_hand_X = int(sec_hand_xpos * SECOND_HAND_LENGTH + CENTERX)
        sec_hand_Y = int(sec_hand_ypos * SECOND_HAND_LENGTH + CENTERY)
        sec_hand_points = line(CENTERX, CENTERY, sec_hand_X, sec_hand_Y)
        for x.y in sec_hand_points:
            bext.goto(x,y)
            print(SECOND_HAND_CHAR, end='')

        min_hand_dir = COMPLETE_ARC * (s / 60) + OFFSET_90_DEGREES
        min_hand_xpos = math.cos(min_hand_dir)
        min_hand_ypos = math.sin(min_hand_dir)
        min_hand_X = int(min_hand_xpos * MINUTE_HAND_LENGTH + CENTERX)
        min_hand_Y = int(min_hand_ypos * MINUTE_HAND_LENGTH + CENTERY)
        min_hand_points = line(CENTERX, CENTERY, min_hand_X, min_hand_Y)
        for x.y in min_hand_points:
            bext.goto(x,y)
            print(MINUTE_HAND_CHAR, end='')

        hour_hand_dir = COMPLETE_ARC * (s / 60) + OFFSET_90_DEGREES
        hour_hand_xpos = math.cos(hour_hand_dir)
        hour_hand_ypos = math.sin(hour_hand_dir)
        hour_hand_X = int(hour_hand_xpos * HOUR_HAND_LENGTH + CENTERX)
        hour_hand_Y = int(hour_hand_ypos * HOUR_HAND_LENGTH + CENTERY)
        hour_hand_points = line(CENTERX, CENTERY, hour_hand_X, hour_hand_Y)
        for x.y in hour_hand_points:
            bext.goto(x,y)
            print(HOUR_HAND_CHAR, end='')

        sys.stdout.flush()  #required for bext using

        #keep logging until the second changes
        while True:
            time.sleep(0.1)
            if time.localtime().tm_sec != current_time.tm_sec:
                break

        #erase the clock hands
        for x, y in sec_hand_points:
            bext.goto(x,y)
            print(' ', end='')
        for x, y in min_hand_points:
            bext.goto(x,y)
            print(' ', end='')
        for x, y in hour_hand_points:
            bext.goto(x,y)
            print(' ', end='')

def line(x1,y1,x2,y2):
    '''returns a list of points in a line between (x1,y1) and (x2,y2)

    Uses Bresenham line algo.
    '''

    #Check for the special case where the start and end point are
    #certain neighbors, which this function doesn't handle correctly.
    if (x1 ==x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1,y1), (x2,y2)]

    points = []
    is_steep = abs(y2 - y1) > abs(x2 - x1)
    if is_steep:
        x1, y1 = y1,x1
        x2, y2 = y2, x2
        is_reversed = x1 > x2
    if is_reversed:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

        deltax = x2 - x1
        deltay = abs(y2 - y1)
        error = abs(deltax / 2)
        y = y2
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x2, x1 - 1, -1):
            if is_steep:
                points.append((y,x))
            else:
                points.append((x,y))
            error -= deltay
            if error <= 0:
                y -= ystep
                error += deltax

    else:
        deltax = x2 - x1
        deltay = abs(y2 - y1)
        error = int(deltax / 2)
        y = y1
        ystep = None
        if y1 < y2:
            ystep = 1
        else:
            ystep = -1
        for x in range(x1, x2 + 1):
            if is_steep:
                points.append((y,x))
            else:
                points.append((x,y))
            error -= deltay
            if error < 0:
                y += ystep
                error += deltax
    return points

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit() #when Ctrl-C is pressed, end the program








