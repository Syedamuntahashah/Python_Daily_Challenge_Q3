                         # TASK : 4
                    # DATE : March 1, 2025

while True:
    user_input = input("Enter a number (or type 'exit' to quit): ")
    
    # Check if the user wants to exit the loop
    if user_input.lower() == 'exit':
        print("Exiting the program... Goodbye!")
        break

    # Validate the input and check if it's a number
    try:
        number = int(user_input)
    except ValueError:
        print("Error: Please enter a valid number.")
        continue
    
    # Check if the number is even or odd using the modulus operator
    if number % 2 == 0:
        print(f"🔢 {number} is an Even number.")
    else:
        print(f"🔢 {number} is an Odd number.")

