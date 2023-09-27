try:
    # Ask the user to enter two numbers
    num1 = float(input("Please enter the first number: "))
    num2 = float(input("Please enter the second number: "))
    
    # Ask the user to choose an operation
    operation = input("Please choose the operation (+, -, *, /): ")
    
    # Perform the selected operation and display the result
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        result = num1 / num2
    else:
        print("Invalid operation.")
        result = None
    
    if result is not None:
        print(f"{num1} {operation} {num2} = {result:.3f}")

except ValueError as ve:
    print(f"Error: {ve}")
except Exception as e:
    print(f"An error occurred: {e}")
