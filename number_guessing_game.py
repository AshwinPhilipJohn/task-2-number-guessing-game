# Number Guessing Game
# The computer selects a random number and the user tries to guess it.
# The program gives hints and tracks the number of attempts.

import random

# Allow the user to play multiple rounds
while True:

    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)

    # Initialize the attempt counter
    attempts = 0

    print("\n--- Number Guessing Game ---")
    print("I have selected a number between 1 and 100.")

    # Keep asking until the user guesses correctly
    while True:
        try:
            # Ask the user to enter a guess
            guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the guess and give a hint
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed the number.")
                print("Number of attempts:", attempts)
                break

        # Handle invalid input
        except ValueError:
            print("Please enter a valid number.")

    # Ask if the user wants to play another round
    play_again = input("Do you want to play another round? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break
