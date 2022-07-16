# Importing Random Number Generator
import random

# Greeting the User and Explaining the Game
print("Welcome to the Number Guesser!\n", "In this game, you will guess a number between 1 and 20.\n", "You will have three tries!\n", "What is your first guess?")

# User's First Guess, Setting Answer, Setting Count
user_guess = int(input())
answer = int(random.randint(1, 20))
count = 0

# Defining a Function to Check Answers
def number_check(user_guess, answer, count):
    if count >= 2:
        if user_guess > answer:
            print("Sorry, your guess was too high.  The answer was:", answer)
            rerun()
        elif user_guess == answer:
            print("Congratulations!  You got the right answer!")
            rerun()
        else:
            print("Sorry, your guess was too low.  The answer was:", answer)
        print("Game Over.")
        rerun()
    elif user_guess == answer:
        print("Congratulations!  You got the right answer!")
        rerun()
    elif user_guess > answer:
        print("Sorry, your answer was too high.  Try again.")
        user_guess = int(input())
        number_check(user_guess, answer, count + 1)
    elif user_guess < answer:
        print("Sorry, your answer was too low.  Try again.")
        user_guess = int(input())
        number_check(user_guess, answer, count + 1)

# Rerun Function
def rerun():
    print("")
    print("Would you like to play again?")
    rerun_choice = int(input("1 for Yes, 2 for No."))
    if rerun_choice == 1:
        print("Welcome back to the Number Guesser!\n", "What is your first guess?")
        user_guess = int(input())
        answer = int(random.randint(1, 20))
        count = 0
        number_check(user_guess,answer, count)
    elif rerun_choice == 2:
        print("Hope you had fun!")
        return
    else:
        print("ERROR!  Try Again.")
        rerun()

number_check(user_guess, answer, count)

