# random-number-game
A simple random number game.

randomnumbergame.py will randomly pick a number between 1 and 100. 

Then it will ask the user to enter a number. 

If the number is too high or too low, it will let them know and ask them to input another number.

This loop will continue until the user inputs the correct number and wins the game.

ai-player.py is the same game, but instead useses an algorithm so that the computer will play.

The algorithm defines the lowest number and the highest number, and always chooses a number in the middle.

If the number is too low, or too high, it will redfine the lowest number or highest number, and keep picking the number in between the two until it wins.