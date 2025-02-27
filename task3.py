             # TASK : 3
            # Date : 27 feb 2025

# Arithmetic calculator using python

while True:
    # Display menu choose number 1-5 to perform operation
    print("\n📌 Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit 🚪")

    # Ask user for choice
    choice = input("Enter choice (1-5): ")

    # Exit the program
    if choice == '5':
        print("🚪 Exiting... Thank you for using the calculator!")
        break  

    # Validate choice
    if choice not in ('1', '2', '3', '4'):
        print("❌ Invalid choice! Please enter a number between 1-4.")
        continue  

    # Take two numbers as input
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # Perform calculations
    if choice == '1':
        result = num1 + num2
        print(f"🧮 {num1} + {num2} = {round(result, 2)}")
    elif choice == '2':
        result = num1 - num2
        print(f"🧮 {num1} - {num2} = {round(result, 2)}")
    elif choice == '3':
        result = num1 * num2
        print(f"🧮 {num1} × {num2} = {round(result, 2)}")
    elif choice == '4':
        if num2 == 0:
            print("❌ Error: Cannot divide by zero!")
        else:
            result = num1 / num2
            print(f"🧮 {num1} ÷ {num2} = {round(result, 2)}")

