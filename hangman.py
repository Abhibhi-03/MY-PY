#Abhi Patel
import random
from words import word_list

##################################################################
# MAIN
##################################################################

def hangman():
  # hangman() Generates a random word that the player has 
  #           to guess through either a letter or a word. It 
  #           replaces all instances of the players guess
  #           if they are correct, and returns nothing otherwise.
  
  # @type: user_input <int>
  # @rtype: str
  
  # Generate the number to guess
  computer_word = random.choice(word_list).upper()
  length = len(computer_word)
  
  blank = list('-'*length)
  guessed_words = list()
  print("Lets play hangman!")
  stand(len(guessed_words))
  wrong_guesses = 0

  # Loops Through Player Turns
  while wrong_guesses<6:
    # Take Players Guess
    p_guess = pg_checker(length,guessed_words)
    guessed_words.append(p_guess)

    # Quit
    if p_guess == None: 
      break

    # Replace '-' in computer word with the players guess, 
    # if that is the correct digit
    switch = False
    if len(p_guess) == 1:
      for index in range(length):
        if p_guess == computer_word[index]: #Ex// pg: 1 cn: 1212521 -> 1-1---1
          blank[index] = p_guess
          switch = True
    
    # Check if player wins
    if '-' not in blank or p_guess == computer_word:
      print("Congratulations! You guessed {} correctly".format(computer_word))
      return rematch()
    
    # Let player know how they did
    # If their guess is in the computer number or not
    if switch:
      print("\n")
      print("Correct Guess: {}".format(''.join(blank)))
      print('Already guessed: ', guessed_words)
      stand(wrong_guesses)
      print("\n")
    else:    
      print("\n")
      print("Incorrect Guess: {}".format(''.join(blank)))
      print('Already guessed: ', guessed_words)
      wrong_guesses += 1
      stand(wrong_guesses)
      print("\n")
  
  # If the player loses
  print("You lose! The word was {}".format(computer_word))
  return rematch()

#############################################################################
# HELPER FUNCTIONS
#############################################################################

def pg_checker(length,guessed_words):
  # pg_checker() Checks if a user input is a single letter, or word of 
  #              the length <length>. Neither of which can be in guessed_words
  
  # @type: length = int, guessed_words = list, User_input
  # @rtype: None, str
  
  p_guess = input('Guess a letter, word that is ' + 
                      ' {} letters long, or press enter to quit: '.format(length)) 
  
  # Check if user wants to quit
  if p_guess == '':
    return None

  # Checks if user input is actually a number
  # Check if length of the guess is correct (1 or the length of the pin)
  # Checks if theyve already guessed it
  elif p_guess.isalpha() and (len(p_guess) == 1 or len(p_guess) == length):
    if p_guess in guessed_words:
      print('Youve already guessed that!')
      return pg_checker(length,guessed_words)
    else:
      return p_guess.upper()

  else:
    print("That was not a letter or word of the correct size, please try again.")
    return pg_checker(length, guessed_words)

def stand(numWrongGuesses):
  # stand() Draws the hangman stand and each piece of the hangman every turn

  # @type: numWrongGuesses = int
  # @rtype: 

  stand =[
    """
      --------
      |      |
      |      
      |    
      |      
      |     
      -
    """,
    """
      --------
      |      |
      |      0
      |    
      |      
      |     
      -
    """,
    """
      --------
      |      |
      |      0
      |      |
      |      |
      |     
      -
    """,
    """
      --------
      |      |
      |      0
      |      |\\
      |      |
      |     
      -
    """,
    """
      --------
      |      |
      |      0
      |     /|\\
      |      |
      |     
      -
    """,
    """
      --------
      |      |
      |      0
      |     /|\\
      |      |
      |     /
      -
    """,
    """
      --------
      |      |
      |      0
      |     /|\\
      |      |
      |     / \\
      -
    """
    ]
  
  print(stand[numWrongGuesses])

def rematch():
  # rematch() Tests if a user wants to play the hangman() game again
  
  # @type: User_input
  # @rtype: None, str
  print("Rematch? [Y/N]: ")
  replay = input()
  if replay.upper() == "Y": 
    return hangman()
