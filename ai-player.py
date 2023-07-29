#this is the random number game, played by an AI algorithm

#import the random module

import random

#define the range of numbers

randomNumber = random.randrange(1,100)

#create variable numberOfGuesses and assign it to 1

numberOfGuesses = 1

#define lowerLimit of guesses to 1 and higherLimit of guesses to 100

lowerLimit = 1
higherLimit = 100

#define guess as an int input
#have AI pick a the number in between lowerLimit and higherLimit

guess = int((lowerLimit + higherLimit)/2)
print ("AI guesses ", guess)

#begin loop that will keep running as long as 'guess' does not equal 'randomNumber'
#while 'guess' does not equal randomNumber add +1 to guess
#if guess is greater than randonNumber print guess is too high and then ask for a number lower than guess
#if guess is smaller than randomNumber print guess is too low and then ask for a number smaller than guess
#if guess is the same as randomNumber print you got it!


while guess != randomNumber:
    numberOfGuesses +=1
    if guess > randomNumber:
        print(guess, "is too high.")
        #reset higherLimit to guess
        higherLimit = guess
        guess = int((lowerLimit + higherLimit)/2)
        print ("AI guesses ", guess)
    elif guess < randomNumber:
        print(guess, "is too low.")
        #reset lowerLimit to guess
        lowerLimit = guess
        guess = int((lowerLimit + higherLimit)/2)
        print ("AI guesses ", guess)
    else: 
       print("AI got it!")

#display number of guesses        
        
print("AI got it! The number was", guess, "And it took AI:", numberOfGuesses, "guesses.")
        