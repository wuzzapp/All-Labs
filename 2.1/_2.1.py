try:
    # Prompt the user for the number of schoolchildren and tangerines
    N = int(input())
    K = int(input())
    
    # Calculate the number of whole tangerines each student gets
    whole_tangerines_per_student = K // N
    
    # Calculate the number of whole tangerines remaining in the basket
    remaining_tangerines_in_basket = K % N
    
    # Display the results using f-strings       
    print(f"{whole_tangerines_per_student}")
    print(f"{remaining_tangerines_in_basket}")
    
except ValueError:
    print("Invalid input. Please enter valid integer values for schoolchildren and tangerines.")
except ZeroDivisionError:
    print("The number of schoolchildren cannot be zero.")
except Exception as e:
    print(f"An error occurred: {e}")
