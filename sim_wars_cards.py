cards_basic = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jopek', 'Dama', 'Król', 'As']

from random import shuffle
from time import sleep
import os

# Shuffle all cards in deck
def shuffle_cards():
    cards_all = cards_basic*4
    shuffle(cards_all)
    return cards_all

# Return strength of cards
def cards_str(card_name):
    card_str = str(cards_basic.index(card_name)+2)
    return card_str

# Add cards to the field
def add_cards(field, t):
    for i in range(t):
        field.append(cards_all[i])
        cards_all.remove(cards_all[i])
    return field

# Generate printed choosen fields of players
def player_field(field):
    print(('-'*9+' ')*(len(field)))

    for i in range(len(field)):
        print('-'+field[i].center(7)+'- ', end='')

    print('\n'+('-'+' '*7+'- ')*(len(field)))
    print(('-'+'Siła:'.center(7)+'- ')*(len(field)))

    for i in range(len(field)):
        print('-'+cards_str(field[i]).center(7)+'- ', end='')

    print('\n'+('-'+' '*7+'- ')*(len(field)))
    print(('-'*9+' ')*(len(field)))
    

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def clear_fields():
    field_pTwo.clear()
    field_pOne.clear()
            
clear_terminal()
cards_all = shuffle_cards()
points_pOne = 0 
points_pTwo = 0
card_iteration = 0
moves = 0
draws = 0

field_pOne = []
field_pTwo = []

while len(cards_all) != 0:
    add_cards(field_pOne, 1)
    add_cards(field_pTwo, 1)
    
    
    print('Player 1 ||| Points:', points_pOne)
    player_field(field_pOne)
    print('Player 2 ||| Points:', points_pTwo)
    player_field(field_pTwo)


    if (int(cards_str(field_pOne[card_iteration])) > int(cards_str(field_pTwo[card_iteration]))):
        print('Player number 1 win this battle!')
        points_pOne = points_pOne+1
        clear_fields()
        if draws != 0:
            draws = 0
            card_iteration = 0
    elif (int(cards_str(field_pOne[card_iteration])) < int(cards_str(field_pTwo[card_iteration]))):
        print('Player number 2 win this battle!')
        points_pTwo = points_pTwo+1
        clear_fields()
        if draws != 0:
            draws = 0
            card_iteration = 0
    else:
        print('Draw!')
        card_iteration = card_iteration+1
        draws = draws+1
    
    moves = moves+1
    print('\n')

if (points_pOne > points_pTwo):
    print('This war win player number 1! Congratulations!')
elif (points_pOne < points_pTwo):
    print('This war win player number 2! Congratulations!')
else:
    print('This war is a draw! Fight again!')

print('\nPlayer 1 ||| Points:', points_pOne)
print('Player 2 ||| Points:', points_pTwo)
