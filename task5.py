                         # TASK : 5
                      # DATE : March 3, 2025

# Number guessing game
import random

secret_number = random.randint(1, 100)
max_attempts = 7
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print(f"You have {max_attempts} attempts to guess the number between 1 and 100.")

while attempts < max_attempts:
    guess = int(input("Guess the number: "))
    attempts += 1
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Congratulations! You guessed the correct number in {attempts} attempts.")
        break
else:
    print(f"❌ You've used all {max_attempts} attempts! The correct number was {secret_number}.")
    print("Game Over! Better luck next time.")