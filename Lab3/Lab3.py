'''
1
# Get user input for N
N = int(input())

# Check if N is a positive integer
if N <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize a variable to start with 2 (the first even number)
    even_number = 2
    
    # Use a while loop to print even numbers from 2 to N
    while even_number <= N:
        print(even_number)
        
        # Increment even_number by 2 to get the next even number
        even_number += 2
'''

'''
2
# Get user input for N
N = int(input())

# Check if N is a positive integer
if N < 0:
    print("Please enter a positive integer.")
else:
    # Initialize the result to 1
    factorial = 1
    
    # Use a while loop to calculate the factorial
    while N > 0:
        factorial *= N
        N -= 1

    # Print the factorial
    print(factorial)
'''

'''

3
while True:
    number = int(input())
    
    if number == 42:
        print()
        break
'''

'''
4
user_input = input()

# Initialize a variable to count the number of 'a's
count_a = 0

# Iterate through each character in the input string
for char in user_input:
    if char == 'a' or char == 'A':  # Count both lowercase and uppercase 'a'
        count_a += 1

# Print the number of 'a's in the string
print(f" {count_a}")
'''

'''
5 
user_input = input()

# Initialize a variable to store the sum of digits
sum_of_digits = 0

# Iterate through each digit character in the input string
for digit_char in user_input:
    if digit_char.isdigit():  # Check if the character is a digit
        digit = int(digit_char)  # Convert the character to an integer
        sum_of_digits += digit  # Add the digit to the sum

# Print the sum of the digits
print(f"{sum_of_digits}")
'''

'''
6
# Get user input for N
N = int(input())

# Check if N is a positive integer
if N <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1

    # Initialize a counter
    count = 0

    # Use a while loop to print the first N Fibonacci numbers
    while count < N:
        print(a, end=" ")  # Print the current Fibonacci number
        a, b = b, a + b  # Calculate the next Fibonacci number
        count += 1
'''

'''
7
user_input = input()

# Reverse the string using slicing
reversed_string = user_input[::-1]

# Print the reversed string
print(reversed_string)
'''

'''
8
oddnumbers = 0

while True:
    user_input = input("press f to see result")

    if user_input.lower() == 'f':
        break  # Exit the loop if the user enters 'f'

    try:
        number = int(user_input)
        if number % 2 == 0:
            continue  # Skip even numbers
        oddnumbers += number
    except ValueError:
        print("Invalid input. Please enter a number or 'f' to quit.")

print(oddnumbers)
'''

'''
9
import random

# Generate a random number between 1 and 100
secret_number = random.randint(1, 777)



while True:
    user_guess = int(input("Guess the number (between 1 and 100): "))
   
    if user_guess < secret_number:
        print("Too small. Try again.")
    elif user_guess > secret_number:
        print("Too large. Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number}")
        break
'''


'''
10
user_input = input()

# Remove spaces and convert the string to lowercase
cleaned_input = user_input.replace(" ", "").lower()

# Check if the cleaned string is equal to its reverse
if cleaned_input == cleaned_input[::-1]:
    print("The entered string is a palindrome.")
else:
    print("The entered string is not a palindrome.")
'''

'''
11
# Get user input for the base (X)
X = int(input("Enter a number X: "))

# Get user input for the exponent (Y)
Y = int(input("Enter the power Y: "))

# Initialize the result to 1
result = 1

# Calculate X to the power of Y using a while loop
while Y > 0:
    result *= X
    Y -= 1

# Print the result
print(f"{result}")
'''


'''
12
N = int(input())

# Check if N is a positive integer
if N <= 0:
    print("Please enter a positive integer.")
else:
    print("Prime numbers in the range from 1 to", N, "are:")

    # Start with the first prime number, 2
    number = 2

    while number <= N:
        is_prime = True
        divisor = 2

        while divisor * divisor <= number:
            if number % divisor == 0:
                is_prime = False
                break  # Break the inner loop if the number is not prime
            divisor += 1

        if is_prime:
            print(number)

        number += 1
'''


'''
13
user_input = input()

# Convert the input to a string, reverse it, and convert it back to an integer
reversed_number = int(str(user_input)[::-1])

# Print the reversed number
print(reversed_number)
'''


'''
14
def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Get user input for the number to test
user_input = int(input())

while True:
    if is_prime(user_input):
        print(f"{user_input} is a prime number.")
        break  # Exit the loop if the number is prime
    else:
        user_input += 1
        continue  # Skip to the next number and continue testing

# Print the next prime number if the entered number was not prime
next_prime = user_input + 1
while True:
    if is_prime(next_prime):
        print(f"The next prime number is: {next_prime}")
        break
    next_prime += 1

'''

'''
15
# Function to perform Caesar Cipher
user_input = input("Enter a string: ")
shift_value = int(input("Enter the shift value: "))

# Apply Caesar Cipher to the input string
encrypted_string = caesar_cipher(user_input, shift_value)


def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            is_upper = char.isupper()  # Check if it's an uppercase letter
            char = char.lower()  # Convert to lowercase for easier manipulation
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            if is_upper:
                shifted_char = shifted_char.upper()  # Convert back to uppercase if necessary
            encrypted_text += shifted_char
        else:
            encrypted_text += char  # Keep non-alphabetic characters as they are
    return encrypted_text



# Print the encrypted string
print("Encrypted string:", encrypted_string)
'''