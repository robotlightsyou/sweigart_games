#!/usr/bin/python3

"""
Affine Cipher by Al Sweigert

The affine cipher is a simple substitution cipher that uses affition and
multiplication to encrypt and decrypt symbols.

"""

"""
@TODOS
* create random key broken, fatal
"""

__version__ = 0
try:
    import pyperclip
except ImportError:
    pass

import random

SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEF""" + \
          """GHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""

def main():
    print('''Affine Cipher, the Affine Cipher is a simple subsitution cipher 
            that uses addition and multiplication to encrypt and decrypt symbols.''')

    while True:
        print("Do you want to (e)ncrypt or (d)ecrypt")
        response = input('>').lower()
        if response.startswith('e'):
            myMode = 'encrypt'
            break
        elif response.startswith('d'):
            myMode = 'decrypt'
            break
        print('Please enter the letter e or d')

    while True:
        print('Please specify the key to use,')
        print('or RANDOM to havre one generated for you: ')
        response = input('>').upper()
        if response == 'RANDOM':
            myKey = genrate_Random_Key()
            print('The key is {}. KEEP THIS SECRET!'.format(myKey))
            break
        else:
            if not response.isdecimal():
                print('This key is not a number.')
                continue
            if checkKey(int(response), myMode):
                myKey = int(response)
                break
    print('Enter the message to {}.'.format(myMode))
    myMessage = input('>')

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)    
    print('%sed text: %' (myMode.title()))
    print(translated)

    try:
        pyperclip.copy(translated)
        print('Full %sed text copied too clipboard.' % (myMode))
    except:
        pass
def get_key_parts_from_key(key):
    """Get the two key A and key B parts from the key"""
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)

def checkKey(key, mode):
    """Return True if key is valid encryption key, otherwise False"""
    keyA, keyB = get_key_parts_from_key(key)
    if mode == 'encrypt' and keyA == 1 and keyB == 0:
        print('This key effectively does not do any encryption on the')
        print('message. Choose a defferent key.')
        return False
    elif keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        print('Key A must be greater than 0 and Key B must be between')
        print('0 and {}.'.format(len(SYMBOLS) - 1))
        return False
    elif gcd(keyA, len(SYMBOLS)) != 1:
        print('Key A ({}) anf the symbol set'.format(keyA))
        print('size ({}) are not relatively prine.'.format(len(SYMBOLS)))
        print('Choose a different key.')
        return False
    return True

def encryptMessage(key, message):
    """Encrypt the message using key"""
    checkKey(key, 'encrypt')
    keyA, keyB = get_key_parts_from_key(key)
    ciphertext = ''
    for symbol in SYMBOLS:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            new_index = (sym_index * keyA + keyB) % len (SYMBOLS)
            ciphertext += SYMBOLS[new_index] 
        else:
            ciphertext += symbol
    return ciphertext

def decryptMessage():
    """decrypt using key"""
    checkKey(key, 'decrypt')
    keyA, keyB = get_key_parts_from_key(key)
    plaintext = ''
    mod_inv_of_key = find_mod_inverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            sym_index = SYMBOLS.find(symbol)
            new_index = (sym_index - keyB) * mod_inv_of_key % len(SYMBOLS)
            plaintext += SYMBOLS[new_index]
        else:
            plaintext += symbol
    return plaintext

def genrate_Random_Key():
    """generate and return a random encryption key"""
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB

def gcd(a, b):
    """return the greatest common dividor of a and b using Euclid's Algo"""
    while a != 0:
        a,b = b%a, a
        return b

def find_mod_inverse(a,m):
    """return the modular inverse of a % m, which is the number x 
    such that a * x % m = 1"""
    if gcd(a, m) != 1:
        #no inverse exists, a and m are not relatively prime
        return None

    #calculate using Extended Euclidean Algo
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = ((u1 - q * v1),
                                   (u2 - q * v2),
                                   (u3 - q * v3),
                                   v1,v2,v3)
    return u1 % m

if __name__ == '__main__':
    main()










