"""Caesar Hacker by Al Sweigart
This program hacks messages encrypted with the Caesar cipher by doing a
brute force attack against every possible key.

Tags: tiny, beginner, cryptography, math"""

__version__ = 0

print('Caesar Cipher Hacker by Al Sweigart')

#Let the user specify the message to hack
print('Enter the encrypted Caesar cupher message to hack.')
message = input(">").upper()

#Every possible  symbol that can be encrypted/decrypted:
#This must match the SYBOLS used when encrypting the message.)
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for key in range(len(SYMBOLS)):
    translated = ''

    for symbol in message:
        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key

            if num < 0:
                num = num + len(SYMBOLS)

            translated = translated + SYMBOLS[num]
        else:
            translated = translated = symbol

    print(f'Key #{key}: {translated}')
