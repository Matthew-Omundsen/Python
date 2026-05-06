#Author: Matthew Omundsen
#Date: 10/1/24
#Program description: ultimate number guessing game

#copy and paste the number guessing game code already made
#make it all a function and loop it so the game can be played as many
#times as the user wants
#extra credit for getting the user's name

import random

#******FUNCTION DEFINITION********
def guessingGame(user):
#important variables, magic number = random integer between 1-100
    magic_number = random.randint(1,100)
    quit_number = 0
    num_of_guesses = 0
    complete_round = 0
#prompts user for first guess
    guess = int(input("What number am I thinking of? (type 0 if you "
                      "give up): "))
    if guess < 0 or guess > 100:
            guess = int(input("OUT OF BOUNDS!!!!"
                      "Try a number between 1-100 this time. "))
    elif guess == quit_number:
        num_of_rounds = 0
        num_of_guesses = 0
        print("Round deleted.")
#loops guess until user guesses right or gives up
    while guess != magic_number and guess != 0 and guess != -1:
        num_of_guesses = num_of_guesses + 1
        print("Incorrect. Try again!")
        if guess > magic_number:
            print(user,"your guess is too high.")
        if guess < magic_number:
            print(user,"your guess is too low.")
        print("Number of guesses: ",(num_of_guesses))
        guess = int(input("What number am I thinking of?"
                     "(type 0 if you give up): "))
        while guess < 0 or guess > 100:
            guess = int(input("OUT OF BOUNDS!!!!"
                      "Try a number between 1-100 this time. "))
            
#This is what happens when the user gets the number right
        if guess == magic_number:
            num_of_guesses = num_of_guesses + 1
            complete_round = 1
            print("Congrats",user+", you guessed the right number in",
                num_of_guesses,"tries!")
#This is what happens when the user quits
        elif guess == quit_number:
            print(user,"your round has been deleted.")
            num_of_guesses = 0
            complete_round = 0
    return num_of_guesses,complete_round

        
#***************
#*****Main******
#***************

total_guesses = 0
total_rounds = 0

print("Welcome to the number guesing game!", "\n",
      "I'm thinking of a number between 1-100 and you must guess what"
      " that number is!")
user = input("What is your name? ")
print("Thank you",user+"!")
#asks user if they want to play again
user_choice = input("Type n to quit or type y to play! ")

#loops every round played after the first round
while user_choice == 'y':
    guesses,rounds = guessingGame(user)
    total_guesses = total_guesses + guesses
    total_rounds = total_rounds + rounds
    user_choice = input("Type n to quit or type y to play again! ")

if user_choice == 'n':
    if total_rounds == 0:
        print("Sorry",user,"but I can't give you statistics because you never"
              "completed \n a full round.")
    else:
        average = total_guesses / total_rounds
        print("Thanks for playing,",user+"! \n", total_rounds, "rounds complete \n",
            "Your average number of guesses per round was",
              format(average,".2f"))





