#Number guessing game
#generate random number, ask user to guess

from random import random
from random import randint


guess = (int(input("Guess a whole number 0-10: ")))
print("You guessed " + str(guess))

random_number = randint(0, 10)
print ("The randomly generated number is " + str(random_number))

#compare the two
if guess == random_number:
    print("You guessed the correct number!\nYOU WIN!!")
else:
    print("Bummer, you lose.")





