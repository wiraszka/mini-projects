import random
import os

# Create global variables for deck, user hand and dealer hand
deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
user_hand = []
dealer_hand = []
line = "--------------------------------------------------------------------------------"

# Clear interface before game start
def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

# Calculates points after first card is dealt to user
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

# Deals random card from deck, then calculates total points of cards in hand
def hit_me(user_hand = '', user_points = '', dealer_hand = '', dealer_points = ''):
	points = 0
	aces = 0
	sum_points = []
	for card in user_hand or dealer_hand:
		if card == 'J': points = 10
		elif card == 'Q': points = 10
		elif card == 'K': points = 10
		elif card == 'A':
			points = 11
			aces = aces + 1
		else: points = card
		sum_points.append(points)
	# Sum up points in hand, taking aces into account
	total_points = 0
	for points in sum_points:
		total_points = total_points + points
	if total_points > 21 and aces >= 1:
		total_points = total_points - 10 * aces
	return total_points

# Determines outcome after points are calculated
def check_points(user_points):
	if user_points < 21:
		return user_points
	elif user_points == 21:
		blackjack(user_points)
	elif user_points > 21:
		went_over(user_points)
	return user_points

# Blackjack!
def blackjack(total_points):
	print("Blackjack!")
	return total_points

# Compare user_points to dealer_points to determine final outcome and statement
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
	# Start game
	print(line,"\nWelcome to Adam's Blackjack game!")
	print("You win by getting to 21 points without going over, or by beating the dealer's score.\n",line)
	input("Press any key to continue: ")

	# Deal face card to dealer then append to list (dealer_hand)
	deal_card = random.choice(deck)
	dealer_hand.append(deal_card)
	dealer_points = score(dealer_hand)
	print(line,"\nThe dealer deals themselves a card and places it face up:", dealer_hand)

	# Deal first card to user then append to list (user_hand)
	deal_card = random.choice(deck)
	user_hand.append(deal_card)
	user_points = score(user_hand)
	print("The dealer deals you the card:",user_hand,"\nYou have:", user_points,"points")
	print("What do you want to do?")

	# Check user's current points tally
	while True:
		if user_points == 21:
			blackjack(user_points)
			break
		# If user busts, break loop and skip to endgame
		elif user_points > 21:
			break
		# If points below 21, prompt user for choice to hit or stay
		else:
			choice = input("--- Press 'h' to HIT --- 's' to Stay --- 'q' to Exit Game: ---")
			print(line)
			# If user choice is to hit, deal new card and append to user_hand, then call hit_me function
			if choice == 'h':
				deal_card = random.choice(deck)
				user_hand.append(deal_card)
				user_points = hit_me(user_hand, user_points)
				print("The dealer's face up card is:", dealer_hand,"\nYour hand is: ",user_hand)
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
	# Determine dealer decision based on user_points
	while True:
		if dealer_points >= 21:
			break
		elif dealer_points > user_points:
			break
		elif dealer_points < user_points:
			deal_card = random.choice(deck)
			dealer_hand.append(deal_card)
			dealer_points = hit_me(dealer_hand, dealer_points)
		else:
			break

	end_game(user_points, dealer_points, dealer_hand)

	# Prompt user to play again
	# If yes then clear and re-start game
	print("Game over")
	again = input("Press 's' to play again ")
	if again == 's':
		clear()
		game()
	else:
		exit()

clear()
game()
