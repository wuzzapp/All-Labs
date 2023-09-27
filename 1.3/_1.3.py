try:
    # Prompt the user for the first number
    first_number = int(input(""))
    
    # Calculate the next two consecutive numbers
    second_number = first_number + 1
    third_number = first_number + 2
    
    # Display the consecutive numbers on separate lines
    print(f"{first_number}")
    print(f"{second_number}")
    print(f"{third_number}")
    
except ValueError:
    print("Invalid input. Please enter a valid integer.")
except Exception as e:
    print(f"An error occurred: {e}")

