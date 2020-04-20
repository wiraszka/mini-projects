import random
import os
# print(help(random))

deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

# user_hand = list()
# dealer_hand = list()

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def score(user_hand):
    points = 0
    for card in user_hand:
        if card == 'J': points = 10
        elif card == 'Q': points = 10
        elif card == 'K': points = 10
        elif card == 'A': points = 11
        else: points = user_hand[0]
    total_points = points
    return total_points

def hit_me(user_hand, user_points, dealer_hand, dealer_points):
    points = 0
    sum_user_points = []
    for card in user_hand:
        if card == 'J': points = 10
        elif card == 'Q': points = 10
        elif card == 'K': points = 10
        elif card == 'A':
            if user_points > 11:
                points = 1
            else:
                points = 11
        else: points = card
        sum_user_points.append(points)

# Add together point tally for all cards in hand
    total_points = 0
    for points in sum_user_points:
        total_points = total_points + points
    return total_points

def check_points(user_points):
    if user_points <= 20:
        return user_points
    elif user_points == 21:
        blackjack(user_points)
    elif user_points > 21:
        went_over(user_points)
    return user_points

def blackjack(total_points):
    print("Blackjack!")
    return total_points

def went_over(total_points):
    print("You went over! Boo you suck")
    return total_points

def game():
    user_hand = list()
    dealer_hand = list()
    print("--------------------------------------------------------------------------------")
    print("Welcome to Adas' Blackjack game!")
    print("You win by getting to 21 points without going over, or by beating the dealer's score.")
    print("--------------------------------------------------------------------------------")
# Dealer deals themselves a card
    deal_card = random.choice(deck)
    dealer_hand.append(deal_card)
    dealer_points = score(dealer_hand)
    print("The dealer deals themselves a card and places it face up:", dealer_hand)
# Dealer deals card to user
    deal_card = random.choice(deck)
    user_hand.append(deal_card)
    user_points = score(user_hand)
    print("The dealer deals you the card:",user_hand)
    print("You have:", user_points,"points")
    print("What do you want to do?")
# Check current score, then Hit or Stay
    while True:
        if user_points == 21:
            blackjack(user_points)
            break
        elif user_points > 21:
            went_over(user_points)
            break
        else:
            hit = input("--- Press 'h' to HIT, 's' to Stay, and 'q' to Exit Game: ---")
            print("--------------------------------------------------------------------------------")
            if hit == 'h':
                deal_card = random.choice(deck)
                user_hand.append(deal_card)
                user_points = hit_me(user_hand, user_points, dealer_hand, dealer_points)
                print("The dealer's face up card is:", dealer_hand[0])
                print("Your hand is: ",user_hand)
                print("You currently have:",user_points,"points")
            elif hit == 's':
                print("Your final tally is:",user_points)
            else:
                print("Ok, goodbye.")
                break

    print("Game over")

clear()
game()




    #deal_card = random.choice(deck)
    #dealer_hand.append(deal_card)
    #dealer_points = score(deal_card)

     # dealer_hand, dealer_points
