#!/usr/bin/python3


'''
DOCSTRING: Blackjack by Al Sweigart
    The classic card game also known as 21. (This vesion doesn't have
    splitting or insurance.)

    Tags: large, game, card came
'''

import random, sys

#set up the constants
HEARTS   = chr(9829)
DIAMONDS = chr(9839)
SPADES   = chr(9824)
CLUBS    = chr(9827)
BACKSIDE = 'backside'


def main():
    print("""Blackjack by Al Sweigart

    Rules:
        Try to get as close to 21 without going over.
        Kings, Queens, and Jacks are worth 10 points.
        Aces are worth 1 or 11 points.
        Cards 2 through 10 are worth their face value.
        (H)it to take another card.
        (S)tand t0 stop taking cards.
        On your first play, you can *D)ouble down to increase your bet
        but must hit exactly one more time before standing.
        In case of a tie, the bet is returned to the player.
        The dealer stops hitting at 17.
        """)

money = 5000
while True:
    #check if the player has run our of money
    if money <= 0:
        print("You're broke!")
        print("Good thing you weren't playing with real money.")
        print('Thanks for playing.')
        sys.exit()

    #let the player enter their bet for the round
    print(f"Money: {money}")
    bet = get_bet(money)

    #give the dealer and player 2 cards from the deck
    deck =  get_deck()
    dealer_hand = [deck.pop(), deck.pop()]
    player_hand = [deck.pop(), deck.pop()]

    #handle player actions
    print(f'Bet: {bet}')
    while True:
        display_hands(player_handm, dealer_hand, False)
        print()

        #check if the player has bust
        if get_card_value(player_hand) > 21:
            break

        #get the player's move, eithe H,S, D
        move = get_move(player_hand, money - bet)

        #handle the player's actions
        if move == 'D':
            #player is doubling down, they can increase their bet
            additional_bet = get_bet(min(bet, (moeny - bet)))
            bet += additional_bet
            print(f'Bet  has been increased to {bet}')
            print(f'Bet: {bet}')

            if move in ('H', "D"):
                #hit/doubling down takes another card
                new_card = deck.pop()
                rank, suit = new_card
                print(f'You drew a {rank} of {suit}.')
                player_hand.append(new_card)

                if get_card_value(player_hand) > 21:
                    #the player has busted
                    continue
            if move in ('S', 'D'):
                break

        #handle dealer's actions
        if get_card_value(dealer_hand) < 17:
            #the dealer hits
            print('Dealer hits...')
            dealer_hand.append(deck.pop())
            display_hands(player_hand, dealer_hand, False)

            if get_card_value(dealer_hand) > 21:
                break
            input('Press enter to continue...')
            print('\n\n')

        #show the final hands
        display_hands(player_hand, dealer_hand, True)

        player_value = get_card_value(player_hand)
        dealer_value = get_card_value(dealer_hand)
        if dealer_value > 21:
            print(f"Dealer busts! You win ${bet}!")
            money += bet
        elif (player_value >21) or (player_value < dealer_value):
            print('You lost!')
            money -= bet
        elif player_value > dealer_value:
            print(f'You won ${bet}!')
            money += bet
        elif player_value == dealer_value:
            print("It's a tie, the bet is returned to you")

        input('Press enter to continue...')
        print('\n\n')

def get_bet(max_bet):
    """Asl the player how much they want to bet"""
    prnt(f'How much do you bet? (1 - {max_bet})')
    while True:
        bet = input(">").upper().strip()
        if bet == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet


def get_deck():
    '''Return a list of (rank,suit) tuples for all 52 cards.'''
    deck =[]
    for suit in (HEARTS, SPADES, DIAMONDS, CLUBS):
        for rank in range(2,11):
            deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    '''Show the player's and dealer's cards. Hide the dealer's first
    card if show_dealer_hand is False'''
    print()
    if show_dealer_hand:
        print('DEALER: ', get_card_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')

    #show the player's cards
    print('Player: ', get_card_value(player_hand))
    display_cards(player_hand)


def get_card_value(cards):
    '''returns the value of the cards. Face cards are worth 10, aces are
    worth 11 or 1(this fu nction picks th e most suitable value).'''
    value = 0
    number_of_aces = 0

    for card in cards:
        rank = card[0]
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):
            value += 10
        else:
            value += int(rank)

    value += number_of_aces
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10

    return value
