try:
    # Prompt the user to enter a number
    number = int(input())
    
    # Perform the left shift operation (<<)
    result = 2**(number)
    
    # Check if the result is zero and display the appropriate message
    if result == 0:
        print("Warning: The result of << is zero.")
    else: 
        print(f"The result of << is {result}")
    
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")

