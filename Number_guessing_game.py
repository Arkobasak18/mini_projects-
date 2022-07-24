num1 = 27
print("This is a number guessing game :)")
num2 = int(input('Enter a number between 1 to 1000 : '))

game_over = False
guess = 1

while not game_over:
    if (num1 == num2):
        print(f"You win, Congrats!, You took {guess} attemptes to guess the number correctly")
        game_over = True
    else:
        if (num2>num1):
            print("You have guessed the wrong number, GUESS AGAIN : TRY SMALLER ")
            guess += 1
            num2 = int(input('Guess Again : '))
        else:
            print("You have guessed the wrong number, GUESS AGAIN : TRY LARGER ")
            guess += 1
            num2 = int(input('Guess Again : '))


