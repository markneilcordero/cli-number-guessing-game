import random

def guess_number():
    secret_number = random.randint(1, 100)

    attempts = 0
    max_attempts = 10

    print("Welcome to the Number Guessing Game!")
    print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == secret_number:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")

if __name__ == "__main__":
    guess_number()