from random import randint

#MAIN

def gameOfNim():
  
  # gameOfNim() generates a random number of coins for three bags and 
  #             returns the bags or asks the user for a rematch.
  # @type: User_input <int>
  # @rtype: bag = list
  
  print("gameOfNim is a game were two players pick coins\n\
  from three bags till there are no coins left.\n\
  The rules of the game:\n\
  The bag generates a random number of coins.\n\
  The player doesn't know the number of coins in each bag.\n\
  You can't pick more than three coins from a bag.\n\
  The last player to pick a coin wins")
  
  # Creates the bags and stores a random number of coins <between 1 and 6>
  # inside the bags
  bag_1 = randint(1,6)
  bag_2 = randint(1,6)
  bag_3 = randint(1,6)
  bags = []
  bags.append(bag_1)
  bags.append(bag_2)
  bags.append(bag_3)
  
  #Counts the player turn while checking if the sum of the bags is greater than Zero
  turn = 0
  while sum(bags) > 0:
    player = turn%2+1
    print("Player {}\'s turn.".format(player))
    p_choice = pickABag(bags)
    bags = howManyCoins(bags, p_choice)
    turn+=1
    
  # Asks the player if they want a rematch
  print("Player {} wins".format(player))
  replay = input("Rematch? [Y/N]: ")
    
  if replay.upper() == "Y":
    return gameOfNim()
  else: 
    print ("Game Over")
  return bags
  
#  HELPER Functions: #

def pickABag(bags):
  
  # pickABag() takes in the number of bags and asks the user for the bag they want
  #            to remove coins from and returns the player's choice<p_choice>.
  # @type: bags = list,
  # @rtype: P_choice = str
  #Allows the player to pick a bag and Prevents players from 
  #picking a bag that is not available and also prevents users from entering 
  #any other data types apart from int
  
  p_choice = input("Pick a bag (1,2,3): ")
  if not p_choice.isnumeric():
    print('Thats not a valid number, try again!')
    return pickABag(bags)
  
  # Checks when a bag is empty and notifies the player  
  p_choice = int(p_choice) - 1
  if p_choice in range(3):
    if bags[p_choice] == 0:
      print("This bag is empty... Pick a new one")
      return pickABag(bags)
    else:
      return p_choice


def howManyCoins(bags,choice):
  
  # howManyCoins(): takes in the bags and asked the user how many coins they 
  #                 wants to remove from the bag and removes it from the 
  #                 corresponding bag using choice
  #@type: bags = list, choice = none
  #@rtype: none
  
  #Asks the user how many coins they want to take 
  size = bags[choice]
  coins = input("How many coins do you want to take?")
  
  #subtracts the number of coins from the corresponding bag chosen by the player
  if coins.isnumeric():
    if int(coins) in range(1,min(size,3) + 1):
      bags[choice] -= int(coins)
      return bags
    
    #checks if user inputs a zero to remove no coin and alert them that they must pick 
    # a coin
    elif int(coins) == 0:
      print("Can't take no coins!")
      return howManyCoins(bags,choice)
      
    #prevents the player from taking more than three coins per turn
    else:
      print("Thats too many coins. You greedy ...")
      return howManyCoins(bags,choice)
