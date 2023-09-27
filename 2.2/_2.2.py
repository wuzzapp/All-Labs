try:
    # Prompt the user for a four-digit number
    number = int(input())
    
    # Check if the entered number has exactly four digits
    if 1000 <= number <= 9999:
        # Extract individual digits
        thousands_digit = number // 1000
        hundreds_digit = (number // 100) % 10
        tens_digit = (number // 10) % 10
        ones_digit = number % 10
        
        # Display the digits using f-strings
        print(f"The digit in the thousands position is {thousands_digit}")
        print(f"The number in the hundreds position is {hundreds_digit}")
        print(f"The digit in the tens position is {tens_digit}")
        print(f"The digit in the position of units is {ones_digit}")
    else:
        print("The entered number is not a four-digit number.")
    
except ValueError:
    print("Invalid input. Please enter a valid four-digit integer.")
except Exception as e:
    print(f"An error occurred: {e}")
