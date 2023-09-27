try:
    # Prompt the user for the population of the universe
    population = int(input())
    
    # Check if the entered population is a non-negative integer
    if population < 0:
        print("Population cannot be negative.")
    else:
        # Calculate the number of survivors based on whether the population is even or odd
        if population % 2 == 0:
            survivors = population // 2
        else:
            survivors = (population + 1) // 2
        
        # Display the number of survivors using f-strings
        print(f"{survivors}")
    
except ValueError:
    print("Invalid input. Please enter a valid non-negative integer for the population.")
except Exception as e:
    print(f"An error occurred: {e}")
