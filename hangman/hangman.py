import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']

words = {
    'Colors':
        [('red orange yellow brown'.split(), 'es un color calido'),
        ('green blue indigo violet'.split(), 'es un color frio'),
        ('white black'.split(), 'es un color?')],
    'Shapes': 
        [('triangle  circle ellipse  chevron'.split(), 'tiene menos de cuatro lados'),
        ('square rectangle rhombus trapazoid'.split(), 'tiene cuatro lados'), 
        ('pentagon hexagon septagon octogon'.split(), 'tiene mas de cuatro lados')],
    'Fruits':
        [('apple orange watermelon grape cherry tomato grapefruit cantalope'.split(), 'tiene forma redonda'),
        ('lemon lime pear banana mango  strawberry'.split(), 'no tiene forma redonda')],
    'Animals':
        [('bear deer donkey lion moose panda zebra cougar tiger'.split(), 'es grande y esta cubierto de pelo'),
        ('beaver cat dog  goat  monkey  mouse otter rabbit rat wolf wombat  weasel skunk'.split(), 'es pequeño o mediano y esta cubierto de pelo'), 
        ('bat crab fish frog lizard python shark sheep squid turtle whale leech'.split(), 'no tiene ni pelo ni plumas'), 
        ('duck eagle owl turkey'.split(), 'esta cubierto de plumas')]
}
    
def getRandomWord(wordDict):
    ''' This function returns a random string from the passed dictionary of lists of strings, and the key also.'''
    
    # First, randomly select a key from the dictionary:
    wordKey = random.choice(list(wordDict.keys()))

    # Second, randomly select a touple from the key's list in the dictionary:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    # Third, randomly select a word from the list and save the hint
    tupleIndex = random.randint(0, len(wordDict[wordKey][wordIndex][0]) - 1)
    hint = wordDict[wordKey][wordIndex][1]

    return [wordDict[wordKey][wordIndex][0][tupleIndex], wordKey, hint]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=' ')
    print()

def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


print('H A N G M A N')

difficulty = 'X'
while difficulty not in 'EMH':
  print('Enter difficulty: E - Easy, M - Medium, H - Hard')
  difficulty = input().upper()
if difficulty == 'M':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'H':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet, hint = getRandomWord(words)
gameIsDone = False

while True:
    print('The secret word is in the set: ' + secretSet + '   Hint: ' + hint)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Check if the player has won
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Check if player has guessed too many times and lost.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

    # Ask the player if they want to play again (but only if the game is done).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet, hint= getRandomWord(words)
        else:
            break
