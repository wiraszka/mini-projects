import random
import os
# print(help(random))
line = "--------------------------------------------------------------------------------"
deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
#deck = ['A', 'A', 'Q', 'K']

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def win_counter():

	return score

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

def hit_me(user_hand, user_points):
	points = 0
	aces = 0
	sum_user_points = []
	for card in user_hand:
		if card == 'J': points = 10
		elif card == 'Q': points = 10
		elif card == 'K': points = 10
		elif card == 'A':
			points = 11
			aces = aces + 1
		else: points = card
		sum_user_points.append(points)
# Add together points in user's hand
	total_points = 0
	for points in sum_user_points:
		total_points = total_points + points
	if total_points > 21 and aces >= 1:
		total_points = total_points - 10 * aces
	return total_points

def hit_dealer(dealer_hand, dealer_points):
	points = 0
	aces = 0
	sum_dealer_points = []
	for card in dealer_hand:
		if card == 'J': points = 10
		elif card == 'Q': points = 10
		elif card == 'K': points = 10
		elif card == 'A':
			points = 11
			aces = aces + 1
		else: points = card
		sum_dealer_points.append(points)
	total_points = 0
	for points in sum_dealer_points:
		total_points = total_points + points
	if total_points > 21 and aces >= 1:
		total_points = total_points - 10 * aces
	return total_points

def check_points(user_points):
	if user_points < 21:
		return user_points
	elif user_points == 21:
		blackjack(user_points)
	elif user_points > 21:
		went_over(user_points)
	return user_points

def blackjack(total_points):
	print("Blackjack!")
	print()
	return total_points

def end_game(user_points, dealer_points, dealer_hand):
	final_tally = "The dealer's hand is:", dealer_hand, "for a total of", dealer_points, "points"
	if user_points > 21:
		print("You went over. Boo, you suck!")
	elif user_points <= 21 and dealer_points > 21:
		print(final_tally)
		print("The dealer went bust. You win!")
	elif dealer_points < 21 and user_points > dealer_points:
		print(final_tally)
		print("You win!")
	elif user_points < dealer_points and dealer_points <= 21:
		print(final_tally)
		print("You lost! You suck.")
	elif user_points == 21 and dealer_points == 21:
		print(final_tally)
		print("You both got Blackjack! I guess you have to be content with a tie.")
	elif user_points == dealer_points:
		print(final_tally)
		print("You both have the same amount of points, dealer wins!")
	return user_points

def game():
	user_hand = list()
	dealer_hand = list()
	print(line)
	print("Welcome to Adam's Blackjack game!")
	print("You win by getting to 21 points without going over, or by beating the dealer's score.")
	print(line)
	input("Press any key to continue: ")
# Dealer deals themselves first card
	deal_card = random.choice(deck)
	dealer_hand.append(deal_card)
	dealer_points = score(dealer_hand)
	print(line)
	print("The dealer deals themselves a card and places it face up:", dealer_hand)
# Dealer deals user first card
	deal_card = random.choice(deck)
	user_hand.append(deal_card)
	user_points = score(user_hand)
	print("The dealer deals you the card:",user_hand)
	print("You have:", user_points,"points")
	print("What do you want to do?")
# Check current score, then chose to hit or stay
	while True:
		if user_points == 21:
			blackjack(user_points)
			break
		elif user_points > 21:
			break
		else:
			choice = input("--- Press 'h' to HIT --- 's' to Stay --- 'q' to Exit Game: ---")
			print(line)
			if choice == 'h':
				deal_card = random.choice(deck)
				user_hand.append(deal_card)
				user_points = hit_me(user_hand, user_points)
				print("The dealer's face up card is:",dealer_hand)
				print("Your hand is: ",user_hand)
				print("You have:",user_points,"points")
			elif choice == 's':
				print("Your final tally is:",user_points)
				break
			elif choice == 'q':
				print("Ok, goodbye.")
				exit()
				break
			else:
				print("Wrong key. Try again.")
				continue
	while True:
		if dealer_points >= 21:
			break
		elif dealer_points > user_points:
			break
		elif dealer_points < user_points:
			deal_card = random.choice(deck)
			dealer_hand.append(deal_card)
			dealer_points = hit_dealer(dealer_hand, dealer_points)
		else:
			break

	end_game(user_points, dealer_points, dealer_hand)

	print("Game over")
	again = input("Press 's' to play again.")
	if again == 's':
		clear()
		game()
	else:
		exit()

clear()
game()
