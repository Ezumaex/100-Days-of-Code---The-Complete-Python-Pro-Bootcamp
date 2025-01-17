from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_guess(guess, random_number):
    """Checks the guess against the random number and provides feedback."""
    if guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        return True
    elif guess > random_number:
        print("Too high.")
    else:
        print("Too low.")
    return False


def set_difficulty():
    """Sets the difficulty level and returns the number of attempts."""
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS
    else:
        print("Invalid difficulty. Defaulting to 'easy'.")
        return EASY_LEVEL_TURNS


def game():
    """Main game function."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    random_number = randint(1, 100)
    attempts = set_difficulty()

    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue

        is_correct = check_guess(guess, random_number)
        if is_correct:
            break

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts remaining.")
        else:
            print("You've run out of guesses. You lose!")
            print(f"The correct number was {random_number}.")


game()
