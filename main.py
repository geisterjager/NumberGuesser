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
        elif user_guess == answer:
            print("Congratulations!  You got the right answer!")
            return
        else:
            print("Sorry, your guess was too low.  The answer was:", answer)
        print("Game Over.")
        return
    elif user_guess == answer:
        print("Congratulations!  You got the right answer!")
        return
    elif user_guess > answer:
        print("Sorry, your answer was too high.  Try again.")
        user_guess = int(input())
        number_check(user_guess, answer, count + 1)
    elif user_guess < answer:
        print("Sorry, your answer was too low.  Try again.")
        user_guess = int(input())
        number_check(user_guess, answer, count + 1)

number_check(user_guess, answer, count)
