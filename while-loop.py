import random
print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
#Si l'utilisateur n'a pas deviné la bonne réponse, la boucle se répète.
#Demander à l'utilisateur de deviner.
#A-t-il deviné le bon nombre ?
#Si le chiffre deviné est correct, indiquer à l'utilisateur qu'il a deviné juste et quitter la boucle.
#S'il n'a pas deviné le bon chiffre, indiquer à l'utilisateur qu'il s'est trompé et répéter la boucle.
