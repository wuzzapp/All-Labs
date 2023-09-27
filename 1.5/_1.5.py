try:
    # Prompt the user for the edge length
    edge_length = int(input())
    
    # Calculate the volume and surface area
    volume = edge_length ** 3
    surface_area = 6 * (edge_length ** 2)
    
    # Display the results using f-strings
    print(f"{volume}")
    print(f"{surface_area}")
    
except ValueError:
    print("Invalid input. Please enter a valid numeric value for the edge length.")
except Exception as e:
    print(f"An error occurred: {e}")
