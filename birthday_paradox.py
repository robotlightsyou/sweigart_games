#!/usr/bin/python3

'''
DOCSTRING: Birthday Paradox Simulation, by Al Sweigart
Explore the surprising probabilities of the "Birthday Paradox".

Tags: short, math, simulation'''

import datetime, random

def get_birthdays(number_of_birthdays):
    '''
    DOCSTRING: Returns a list of number random date objects for birthdays.'''
    birthdays = []
    for i in range(number_of_birthdays):
        #the year is unimportant for our simulationm as long as all
        #birthdays have the same year
        start_of_year = datetime.date(2001, 1, 1)

        #get a random day into the year
        random_number_of_days = datetime.timedelta(random.randint(0,364))
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays):
    '''
    DOCSTRING: Returns the date object of a birthday that occurs more than 
        once in the birthdays list.'''
    if len(birthdays) == len(set(birthdays)):
        return None #all birthdays are unique

    #compare each birthday to every other birthday
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays):
            if birthdayA == birthdayB:
                return birthdayA  #return the matching birthday

#display the intro
print('''Birthday Paradox, by Al Sweigart

The birthday paradox shows us that in a group of N people, the odds
that two of them have matching birthdays is surprisingly large.
This program does a Monte Carlo simulation (that is, repeated random
simulations) to explore this concept.

(It's not actually a paradox, it's just a surprising result.)
''')

#Set up a tuple of month names in order
MONTHS = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')

while True:
    print('How many birthdays shall I generate? (Max 100)')
    response = input(">")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break #user has entered a valid response
print()

#generate and display the birthdays
print('Here are ', num_bdays, ' birthdays:')
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        #display a comma after each birthday after the first
        print(', ', end='')
    month_name = MONTHS[birthday.month - 1]
    date_text = '{} {}'.format(month_name, birthday.day)
    print(date_text, end='')
print()
print()

#determine if there are two birthdays that match
match = get_match(birthdays)

#display the results
print('In this simulation, ', end='')
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text - '{} {}'.format(month_name, match.day)
    print('multiple people have a birthday on ', date_text)
else:
    print('there are no matching birthdays.')
print()

#run through 100,000 simulations
print('Generating ', num_bdays, ' random birthdays 100,000 times...')
print('Press Enter to begin...')

print("Let's run another 100,000 simulations.")
sim_match = 0  # how many simulations have had matching birthdays
for i in range(100_000):
    #report the progress every 10,000 simulations
    if i % 10_000 == 0:
        print(i, ' simulations run...')
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) != None:
        sim_match += 1
print('100,000 simulations run.')

#diplay simulation results
probability = round(sim_match / 100_000 * 100, 2)
print('Out of 100,000 simulations of ', num_bdays, ' people, there was a')
print('matching burthday in that group ', sim_match, ' times. This means')
print('that', num_bdays, ' people have a ', probability, '% chance of')
print('having a matching birthday in their groupp.')
print("That's probably more than you would ever think.")






