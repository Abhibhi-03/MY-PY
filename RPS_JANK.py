#Abhi Patel
# Our mission today is to build a Janky but functional rock paper
# scissors program: New additions 
# Funky stuff to add:
# -> Keep running the code until the player chooses to quit
#   (Use a for loop to say how many turns, or a while loop with 
#     A breakable condition, this you can do with else)
# -> Score keeping mechanism


# import is a way for us to use other peoples work. We chose to use
#        the random library, specifically the randint function
# randint() generates random integers from given range 

from random import randint
com_opts = ["Rock", "Paper", "Scissors"]
com_choice = com_opts[randint(0,2)]

play_choice = str(input("\'Rock\' , \'Paper\', or \'Scissors\'? : "))
print("The computers choice was {}".format(com_choice))

if play_choice == com_choice:
    print("Tie/Draw: Better luck next time sucker")
elif play_choice == "Rock":
  if com_choice == "Scissors":
      print("You beat the computer")
  else:
      print("You lose")

elif play_choice == "Paper":
    if com_choice == "Rock":
        print("You lose")
else:
    if com_choice == "Paper":
        print("You beat the computer")
    else:
        print("You lose")


    
