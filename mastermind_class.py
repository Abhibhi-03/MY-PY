from random import randint
##################################################################
# MAIN
##################################################################

def mastermind():
  # mastermind() Generates a random 4 digit number that the player has 
  #              to guess. It lets the player know if their guess has 
  #              a number in the correct spot, or a correct number but
  #              the wrong spot.
  
  # @type: user_input <int>
  # @rtype: str
  
  # Generate the number to guess
  computer_num = generate_num()

  # Loops Through Player Turns
  for i in range(0,12):
    print("Player has {} turns left".format(12-i))

    # Take Players Guess
    p_guess = pg_checker()
      
    # Quit
    if p_guess == None: 
      break

    # Check if player wins
    elif int(p_guess) == int(computer_num):
      print("Congratulations! You guessed it correctly")
      return rematch()
    
    # Count correct numbers in correct spot <spot>
    # Count the number of correct numbers in the wrong spot <num>
    spot = 0
    num = 0
    for index in range(4):
      if p_guess[index] == computer_num[index]:
        spot += 1
      elif p_guess[index] in computer_num:
        num += 1
    
    # Let player know how they did
    print("\n")
    print("Guess is: \n \t {}".format(p_guess))
    print("Correct Spot: {}".format(spot))
    print("Correct Number: {}".format(num))
    print("\n")
  
  # If the player loses
  print("You lose! The number was {}".format(computer_num))
  return rematch()

#############################################################################
# HELPER FUNCTIONS
#############################################################################

def pg_checker():
  # pg_checker() takes a user input and checks wether or not the input
  #              is a single letter, or a word of the correct length
  
  # @type: User_input
  # @rtype: None, str
  
  p_guess = input('Guess a 4 digit number, or press X to quit: ') 
  
  # Check if user wants to quit
  if p_guess == 'X' or p_guess == '':
    return None

  # Check if length of the guess is correct (4)
  # Checks if user input is actually a number
  elif len(p_guess) != 4 or not p_guess.isnumeric():
    print("That is NOT a 4 digit number. Try again")
    return pg_checker()

  # Test if there are duplicate digits in the guess
  elif len(p_guess) != len(set(p_guess)):
    print("Oops! No duplicate numbers allowed")
    return pg_checker()

  else:
    return p_guess

def generate_num():
  # generate_num() returns a 4 digit number as a string which has NO duplicate 
  #                digits
  
  # @type: None 
  # @rtype: str

  num = ""
  while len(num) < 4:
    n = str(randint(0,9))
    if n not in num:
      num += n 
  return num  

def rematch():
  # rematch() Tests if a user wants to play the mastermind() game again
  
  # @type: User_input
  # @rtype: None, str
  print("Rematch? [Y/N]: ")
  replay = input()
  if replay == "Y": 
    return mastermind()
