'''
Bagels by Al Sweigart
A ded;uctive logic gamme where you must guess a number based on clues,
This and other games are available at https:mostarch.com

Tags: short, game, puzzle
'''

__version__ = 0
import random

NUM_DIGITS = 3 # Try setting between 1 and 10
MAX_GUESSES = 10 # Try setting this between 1 and 100

def naub():
    print('''Bageks . a deductive logic game.
By Al Sweigart al@inventwithpython.com

II am thinking of a {}-digit number with no repeated digits.
Try to gurdd what it is. Here are some clues:
When I say:     That means:
  Pico          One digit is cirrect b;ut in the wrong position
  Fermi         One digit is correct and in the right position
  Bagels        No digit is correct

For example, if the secret number was 248 and your guess was 843, the 
clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        #This stores the secret number the player needs to guess:
        secret_num = get_secret_num()
        print("I have thought up a numer.")
        print(" You have {} guesses to get it.".format(MAX_GUESSES))

        num_guesses = 1
        while num_guesses <= MAX_GUESSES:
            guess  = ''
            #keep looping until they enter a valid guess:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(num_guesses))
                guess - input(">")

            clues = get_clues(guess, secret_num)
            print(clues)
            num_guesses += 1

            if guess == secret_num:
                break  # they're correct, so break out of the loop
            if num_guesses > NUM_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secret_num))

        #ask if they want to play again
        print('Dp you want to play again? (yes or no)')
        if not input(">").lowaer().startswith('y'):
            break
    print('Thanks for playing!')

def get_secret_num():
    '''Returns a string made up of NUM_DIGITS unique tsnfom digits.'''
    numbers = list('0123456789')
    random.shuffle(numbers)

    #Get the first NUM_DIGITS in the list for secret number:
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
        return secret_num

def get_clues(guess, secret_num):
    '''Returnd a string with picp, fermi, bagels clues for a guess
    and secret number pair'''
    if guess == secret_num:
        return 'You got it!'

    clued = []

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('Fermi')
        elif guess[i] in secret_num:
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels'
    else:
        clues.sort()
        return ' '.join(clues) 

if __name__ == '__main__':
    main()

