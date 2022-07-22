#### Rock paper scissor rope ####
import random

from numpy import true_divide
#defining the conditions of the game
def game(comp, you):
    if you == comp:
        return None
    elif comp == '1':
        if you =='2':
            return True
        elif you == '3':
            return False
        elif you == '4':
            return True
    elif comp == '2':
        if you =='1':
            return False
        elif you == '3':
            return True
        elif you == '4':
            return False
    elif comp == '3':
        if you =='2':
            return False
        elif you == '1':
            return True
        elif you == '4':
            return False
    elif comp == '4':
        if you =='2':
            return True
        elif you == '3':
            return True
        elif you == '1':
            return False
#giving the options to choose for the player
print("Computer's turn : Rock(1),Paper(2),Scissor(3),Rope(4)")
print("Your turn : Rock(1),Paper(2),Scissor(3),Rope(4)")

#getting a random input for the computer player
randNo = random.randint(1,4)
if randNo == 1:
    comp = '1'
elif randNo == 2:
    comp = '2'
elif randNo == 3:
    comp = '3'
else:
    comp = '4'
#getting an input from the human player
you = input("Your turn : Rock(1)Paper(2)scissor(3)Rope(4) : ")

#printing what the computer and the human choose
print(f"computer choose : {comp}")
print(f"You choose : {you}")

# win or loose
a = game(comp, you)
if (a == None):
    print("The game is a tie !")
elif (a == True):
    print("You have won, Congrats! :)")
else:
    print("You have lost :( ")