#!/usr/bin/python3

"""
Alphabetize Quiz by Al Sweigart 
A time-based quiz game to see how fast you can alphabetize letters.
This and other games are available at nostarch.com

Tags: short, game, word
"""

__version__ = 0
import random, time

#Set up the constants:
# (!) Try changing the constands:
QUESTION_SIZE = 5
QUIZ_DURATION = 30

ALPHABET='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REVERSE_ALPHABET = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'

def main():
    #fancy animation for title
    slowPrint(ALPHABET, 0.2)
    slowPrint('     Alphabetize Quiz', 0.2)
    time.sleep(0.5)

    print('''by Al Sweigart

Enter the alphabetical order of the letters shown as fast 
as possible. Try to alphabetize as many as possible in {} seconds!

Example:
    P M O T Q <-- The letters.
    > mopqt   <-- Enter the correct alphabetical order.
    '''.format(QUIZ_DURATION))
    input('Press Enter to begin...')

    start_time = time.time()
    num_correct = 0
    while True:
        quiz_letters = random.sample(ALPHABET, QUESTION_SIZE)
        print(' '.join(quiz_letters))
        response = input('>').upper()
        response = response.replace(' ','')

        if time.time() - 30 > start_time:
            print("TIME's UP!")
            break

        if list(response) == sorted(quiz_letters):
            print('     Correct!\n')
            num_correct += 1
        else:
            print('     Sorry, wrong. :(\n')

    #after loop exits quiz is over
    print('In {} seconds you'.format(QUIZ_DURATION))
    print('got {} correct'.format(num_correct))
    print('Thanks for playing')

def slowPrint(text, pause_amount = 0.1):
    """slowly  print out the characters one at a time"""
    for character in text:
        print(character, flush=True, end='')
        time.sleep(pause_amount)
    print()

if __name__ == '__main__':
    main()
