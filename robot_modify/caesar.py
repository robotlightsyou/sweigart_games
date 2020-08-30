#!/usr/bin/python3

'''This program applies a simple caesar shift.'''

import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python caesar.py key")
        return 1
    else:
        for i in sys.argv[1]:
            if not i.isdigit():
                print("Usage: python caesar.py key")
                return 1
        cipher = int(sys.argv[1])

        print('plaintext: ',end='')
        plain = input()
        encrypted = ''
        for word in list(plain):
            for letter in word:
                if letter.isupper():
                    letter = chr(((ord(letter) + cipher - 64) % 26) + 64)
                    encrypted += letter
                    # encrypted += (((letter + cipher - 64) % 26) + 64)
                elif letter.islower():
                    # encrypted += (((letter + cipher - 96) % 26) + 96)
                    letter = chr(((ord(letter) + cipher - 96) % 26) + 96)
                    encrypted += letter
                else:
                    encrypted += letter
        print(f'ciphertext: {encrypted}')

if __name__ == '__main__':
    main()

