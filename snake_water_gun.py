#### Snake water gun ####
import random

def game(comp, you):
    if you == comp:
        return None
    if comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    if comp == 'w':
        if you == 'g':
            return True
        elif you == 's':
            return False
    if comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True

print("Computer's Turn : Snake(s) Water(w) or Gun(g) ")
print("Computer has choosen, Now it's your turn ")
randNo = random.randint(1,3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
else:
    comp = 'g'
you = input("Your Turn : Snake(s) Water(w) or Gun(g) ")

print(f"Computer choose {comp}")
print(f"You choose {you}")

a = game(comp, you)
if (a == None):
    print('The game is a tie!')
elif (a == True):
    print('You have won! Congrats :)')
else:
    print('You have lost :(')
