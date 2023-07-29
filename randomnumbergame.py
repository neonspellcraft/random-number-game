#this is a basic random number guessing game

#import the random module

import random

#define the range of numbers

randomNumber = random.randrange(1,100)

#create variable numberOfGuesses and assign it to 1

numberOfGuesses = 1

#define guess as an int input
#ask user to pick a number between 1 and 100 and store that in guess

guess = int(input("Guess a number between 1 and 100: "))

#begin loop that will keep running as long as 'guess' does not equal 'randomNumber'
#while 'guess' does not equal randomNumber add +1 to guess
#if guess is greater than randonNumber print guess is too high and then ask for a number lower than guess
#if guess is smaller than randomNumber print guess is too low and then ask for a number smaller than guess
#if guess is the same as randomNumber print you got it!


while guess != randomNumber:
    numberOfGuesses +=1
    if guess > randomNumber:
        print(guess, "is too high.")
        guess = int(input("Pick a number smaller number: "))
    elif guess < randomNumber:
        print(guess, "is too low.")
        guess = int(input("Pick a higher number: "))
    else: 
       print("You got it!")

#display number of guesses        
        
print("You got it! The number was", guess, "And it took you:", numberOfGuesses, "guesses.")
        