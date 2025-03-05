                                         #  TASK : 6
                                    # Date : March 05 2025  

     # Random password generator

import random
import string

def generate_password(length, use_digits=True, use_symbols=True):
    if length < 8:
        print("Password must be at least 8 characters long!")
        return None

    characters = string.ascii_letters  # Uppercase + Lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        length = int(input("Enter password length (minimum 8): "))
        
        include_digits = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        include_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
        
        for i in range(num_passwords):
            password = generate_password(length, include_digits, include_symbols)
            if password:
                print(f"Generated Password {i+1}: {password}")
    
    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()
