# Author: Josiah Boman
# Date: 04/15/2020
# Description: This program prompts the user for an integer that the player will try to guess.
# If the player's guess is higher or lower than the target number, the program should display
# "Too high" or "Too low" respectively. The program uses a loop that repeats itself until the user
# correctly guesses the number and records the amount of guesses it took.

print("Enter the number for the player to guess.")
number_to_guess = int(input())

print("Enter your guess.")
player_guess = int(input())

guess_count = 1

while player_guess != number_to_guess:              # While the user's guess is incorrect, the loop will run
    if int(player_guess) > int(number_to_guess):    # This block runs if the player's guess is too high
        print("Too high - try again:")
        player_guess = input()                          # Requires input from user for new guess
        guess_count = guess_count + 1                   # Adds to guess count total

    elif int(player_guess) < int(number_to_guess):  # This block runs if the player's guess is too low
        print("Too low - try again:")
        player_guess = input()                          # Requires input from user for new guess
        guess_count = guess_count + 1                   # Adds to guess count total

    elif int(player_guess) == int(number_to_guess): # This block runs if the player guesses correctly
        print("You guessed it in " + str(guess_count) + " tries.")
        break                                       # Break free from loop after the correct guess
