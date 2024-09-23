import random

def number_guessing_game():
       secret_number = random.randint(1, 100)
    attempts = 0
    guess = None

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try guessing a higher number.")
            elif guess > secret_number:
                print("Too high! Try guessing a lower number.")
            else:
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

number_guessing_game()
