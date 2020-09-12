#!/usr/bin/python3

"""
Alphabetize Word Quiz, by Al Sweigart
A time-based quiz game to see how fast you can alphabetize words.
"""

'''
@TODOS
* Only print at end of game
'''

__version__ = 0
import random, time

#Set the constraints
QUESTION_SIZE = 3 #eah question shows 3 words
WORD_RANGE = 50 #How closely grouped the words are
QUIZ_DURATION = 30 #the quiz lasts 30 seconds

##look into further:
assert QUIZ_DURATION

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
REVERSE_ALPHABET = ''.join(sorted(ALPHABET, reverse = True))

#Read in the words from the word file.
#This file can be downloaded from
#https://inventwithpython.com/commonenglishwords.txt
with open('utils/commonenglishwords.txt') as wordfile:
    all_words = wordfile.read().splitlines()

def main():
    #fancy animation
    slow_print(ALPHABET, 0.2)
    slow_print('   Alphabetize Word Quiz', 0.2)
    slow_print(REVERSE_ALPHABET, 0.2)
    time.sleep(0.5)

    print('''
by Al Sweigart 

To play, enter the alphabetical order of the words shown as fast as
possible. Try to get as many as possibble in {} seconds!

Examle:
    trade tracks transmit  <-- The 1st, 2nd, and 3rd word.
    1     2       3        <-- Word numbers
    > 213                  <-- Enter the alphabetical order.

'''.format(QUIZ_DURATION))
    input('Press Enter to begin')

    start_time = time.time()
    num_correct = 0
    while True:
        #Come up with QUESTION_SIZE words for the question:
        #qustionletters = random.sample(ALPHABET,QUESTION_SIZE)
        game_range = random.randint(0,len(all_words) - WORD_RANGE)
        possible_words = all_words[game_range:game_range + QUESTION_SIZE]
        quiz_words = random.sample(possible_words, QUESTION_SIZE)
        random.shuffle(quiz_words)

        print('    ', ' '.join(quiz_words))

        #print the number labels
        print('    ', end='')
        for i, word in enumerate(quiz_words):
            print(i + 1, end ='')
            print(' ' * (len(word)), end='')
        print() 

        response = input('>').replace(' ','') #remove any spaces

        #check game time
        if time.time() - 30 > start_time:
            print("TIME'S UP!!")
            break

        #check if response correct
        is_correct = True
        for i, number in enumerate(response):
            if quiz_words[int(number) - 1] != sorted(quiz_words)[i]:
                is_correct = False

        if is_correct:
            print('     Correct\n')
            num_correct += 1
        else:
            print('     Ack :(\n')

        #after loop exits show final score
        print('In {} seconds you'.format(QUIZ_DURATION))
        print('got {} correct!'.format(num_correct))
        print('thanks for playing!')

def slow_print(text, pause_amount):
    for character in text:
        print(character, flush=True, end='')
        time.sleep(pause_amount)
    print()

if __name__ == '__main__':
    main()

