try:
    # Prompt the user for three integers
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    
    # Calculate the sum
    total = num1 + num2 + num3
    
    # Display the sum using f-strings
    print(f"{total}")
    
except ValueError:
    print("Invalid input. Please enter valid integers.")
except Exception as e:
    print(f"An error occurred: {e}")
