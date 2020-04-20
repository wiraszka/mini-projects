import os

# Clear command line window
def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def hang_that_man(wrong_guess):
    if wrong_guess == 0:
        print(' -----')
        print(' |   |')
        print(' |')
        print(' |           \o/  ')
        print(' |            |    ')
        print('/ \\          / \ ')

    if wrong_guess == 1:
        print(' -----')
        print(' |   |')
        print(' |')
        print(' |     \o/  ')
        print(' |      |    ')
        print('/ \\    / \ ')
        print("Bob is going to die dude. You gotta save him!")

    if wrong_guess == 2:
        print(' -----')
        print(' |   |')
        print(' |')
        print(' |  \o/  ')
        print(' |   |    ')
        print('/ \\ / \ ')
        print("One more bad guess and that's it for Bob.")

    if wrong_guess == 3:
        print(' -----')
        print(' |   |')
        print(' |   o')
        print(' |  /|\ ')
        print(' |  / \ ')
        print('/ \\')
        print('')
        print('Well... Bob is dead. You failed.')
        quit()

# PLAYER ONE: Input hangman phrase & process into hidden characters
input_phrase = input('Please enter a word:').upper()
hang_phrase = [x for x in input_phrase]
hidden_phrase = ['-' if x.isalpha() else x for x in hang_phrase]
hidden_string = ''.join(hidden_phrase)
clear()

# PLAYER TWO: Game Start - Introduce Bob
wrong_guess = 0
hang_that_man(wrong_guess)
print('')
print('Hi, this is Bob...')
print("He has been sentenced to death by hanging, but you can save him!")

# Ask user if they want to save Bob
save = input('Will you save Bob? (y/n)').lower()
if save == 'y':
    pass
elif save == 'n':
    wrong_guess = 3
    hang_that_man(wrong_guess)
else:
    quit()

solved = False
count = 0
used_letters = {}

# Guessing loop
while solved is False:
    count += 1
    if count == 3:
        print('-'*70)
        save = input('Are you sure you still want to save Bob? (y/n)').lower()
        if save == 'y':
            pass
        elif save == 'n':
            wrong_guess = 3
            hang_that_man(wrong_guess)
        else:
            print("That's not an answer. Y or N.")
    print('-'*70)
    print('Your phrase is:', hidden_string)
    user_letter = input('Please guess a letter:').upper()
    if not user_letter.isalpha():
        quit()
    else:
        letter_position = -1
        correct_guess = False
        for x in hang_phrase:
            letter_position += 1
            if user_letter == x:
                used_letters[letter_position] = user_letter
                correct_guess = True
            else:
                pass
        if correct_guess == True:
            print('Guessed correctly!')
        elif correct_guess == False:
            wrong_guess += 1
            print('Fail! You messed up.')
            hang_that_man(wrong_guess)
    for pos in used_letters:
        hidden_phrase[pos] = used_letters[pos]
    hidden_string = ''.join(hidden_phrase)
# End game, check if all letters have been guessed
    if '-' not in hidden_string:
        solved = True
        wrong_guess = 0
        hang_that_man(wrong_guess)
        print("You saved Bob!")
    else:
        pass
