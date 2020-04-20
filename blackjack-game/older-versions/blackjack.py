import random
import os
# print(help(random))

deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

user_hand = list()
dealer_hand = list()

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def score(deal_card):
    points = 0
    if deal_card == 'J' or 'Q' or 'K':
        points = 10
    if deal_card == 'A':
        points = 11
    if deal_card is type(int):
        points = deal_card
    return points

def game():
    deal_card = random.choice(deck)
    user_hand.append(deal_card)
    user_points = score(deal_card)

    deal_card = random.choice(deck)
    dealer_hand.append(deal_card)
    dealer_points = score(deal_card)

    return user_hand, user_points, dealer_hand, dealer_points

print(game())
print(game())
