# Simple Implementation of hangman game

from random_word import RandomWords

random = RandomWords()

hangman = [ '''

    +---+
    |   |
        |
        |
        |
        |
        |
===============''','''
    +---+
    |   |
    0   |
        |
        |
        |
        |
===============''','''
    +---+
    |   |
    0   |
    |   |
        |
        |
        |
===============''','''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        |
===============''','''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        |
===============''','''
    +---+
    |   |
    0   |
   /|\  |
   /    |
        |
        |
===============''','''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
        |
        |
===============''']

play = True
word = random.get_random_word(hasDictionaryDef = 'true')
user_mistakes = 0


used_letters = ''
correct_letter = ''

while play:
    
    print(hangman[user_mistakes])


    print('This word has ' + str(len(word)) + ' letters.')
    print(f"Letters you've tried: {used_letters}")

    # For printing empty spaces
    for char in word:
        if char in correct_letter:
            print(char, end = ' ')
        else:
            print('_', end = ' ')

    # Player inputs letter    
    try:
        guess = str(input('\nGuess a letter: '))
    except:
        print('Enter a letter!')
        continue
    
    # Validation 
    if not guess.isalpha():
        print('Enter only a letter.')
    elif len(guess) > 1:
        print('Enter only a single letter')
    elif guess in used_letters or guess in correct_letter:
        print('You already guessed that letter.')
        continue


    
    if guess in word:
        num_letters = word.count(guess)
        correct_letter += guess * num_letters
    else:
        user_mistakes += 1
        used_letters += guess

    # If player wins, retry?
    if (len(correct_letter) == len(word)):
        print(f'Congratulations, you WON! The word was: {word}!')
        print('Would you like to play again? Y/N')
        
        if input().lower() == 'n':
            play = False
            break   # Break out of for loop
            
        else:
            word = random.get_random_word(hasDictionaryDef = 'true')
            user_mistakes = 0
            used_letters = ''
            correct_letter = ''
            
    
    
    # GAME OVER/ RETRY?
    if user_mistakes == 6:
        print(f"GAME OVER.\n The word was {word}.\n Would you like to play again? Y/N")
        if input().lower() == 'n':
            play = False
            break
            
        else:
            word = random.get_random_word(hasDictionaryDef = 'true')
            user_mistakes = 0
            used_letters = ''
            correct_letter = ''
            
                    
    
    
        
        





    
            

    
