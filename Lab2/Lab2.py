'''
1
def check_relation(number):
    try:
        if not isinstance(number, int) or number < 1000 or number > 9999:
            raise ValueError("Input must be a positive four-digit integer")
        
        # Extract individual digits
        thousands = number // 1000
        hundreds = (number // 100) % 10
        tens = (number // 10) % 10
        ones = number % 10

        # Check if the relation holds
        if thousands + ones == abs(tens - hundreds):
            return "YES"
        else:
            return "NO"
    except ValueError as e:
        return str(e)

# Input from the user
input_number = input()
try:
    input_number = int(input_number)
    result = check_relation(input_number)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid four-digit integer.") 
'''

'''
2
def check_access(age):
    try:
        age = int(age)
        if age >= 18:
            return "Access allowed"
        else:
            return "Access denied"
    except ValueError:
        return "Invalid input. Please enter a valid age as an integer."

# Input from the user
input_age = input()
result = check_access(input_age)
print(result)
'''

'''
3
def arithmetic_progression(a, b, c):
    try:
        a, b, c = int(a), int(b), int(c)
        
        if (c - b) == (b - a):
            return "YES"
        else:
            return "NO"
    except ValueError:
        return "Invalid input. Please enter three valid numbers as integers."

# Input from the user
try:
    num1 = input()
    num2 = input()
    num3 = input()
    
    result = arithmetic_progression(num1, num2, num3)
    print(result)
except ValueError:
    print("Invalid input. Please enter valid numbers as integers.")
'''

'''
4
def rook_move(x1, y1, x2, y2):
    try:
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        if x1 > 8 or x2 > 8 or y1 > 8 or y2 > 8:
            return "Invalid input. Coordinates must be between 1 and 8."

        if x1 == x2 or y1 == y2:
            return "YES"
        else:
            return "NO"
    except ValueError:
        return "Invalid input. Please enter valid coordinates as integers between 1 and 8."

# Input from the user
try:
    x1 = input()
    y1 = input()
    x2 = input()
    y2 = input()
    
    result = rook_move(x1, y1, x2, y2)
    print(result)
except ValueError:
    print("Invalid input. Please enter valid coordinates as integers between 1 and 8.")
'''

'''
5
def king_move(x1, y1, x2, y2):
    try:
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

        if x1 > 8 or x2 > 8 or y1 > 8 or y2 > 8:
            return "Invalid input. Coordinates must be between 1 and 8."

        if abs(x1 - x2) == abs(y1 - y2):
            return "YES"
        else:
            return "NO"
    except ValueError:
        return "Invalid input. Please enter valid coordinates as integers between 1 and 8."

# Input from the user
try:
    x1 = input()
    y1 = input()
    x2 = input()
    y2 = input()
    
    result = king_move(x1, y1, x2, y2)
    print(result)
except ValueError:
    print("Invalid input. Please enter valid coordinates as integers between 1 and 8.")
'''

'''
6
def average(a, b, c):
    try:
        a, b, c = int(a), int(b), int(c)

        # Create a list of the three numbers and sort it in ascending order
        numbers = [a, b, c]
        numbers.sort()

        # The average number is the second number in the sorted list
        average = numbers[1]
        return average
    except ValueError:
        return "Invalid input. Please enter valid integers."

# Input from the user
try:
    num1 = input()
    num2 = input(
    num3 = input()

    result = average(num1, num2, num3)
    print(result)
except ValueError:
    print("Invalid input. Please enter valid integers.")
'''

'''
7
def days(month):
    try:
        month = int(month)
        if 1 <= month <= 12:
            # Use a list to store the number of days in each month
            days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return days_in_months[month - 1]
        else:
            return "Invalid input. Please enter a month between 1 and 12."
    except ValueError:
        return "Invalid input. Please enter a valid month as an integer."

# Input from the user
try:
    month = input()
    result = days(month)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid month as an integer.")
'''

'''
8
def weight_category(weight):
    try:
        weight = int(weight)
        if weight <= 60:
            return "Lightweight"
        elif weight <= 64:
            return "First Welterweight"
        elif weight <= 69:
            return "Welterweight"
    except ValueError:
        return "Invalid input. Please enter a valid weight as an integer."

# Input from the user
try:
    boxer_weight = input()
    result = weight_category(boxer_weight)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid weight as an integer.")
'''

'''
9
def compare_passwords(password1, password2):
    if password1 == password2:
        return "Password accepted"
    else:
        return "Password not accepted"

# Input from the user
password1 = input()
password2 = input()

result = compare_passwords(password1, password2)
print(result)
'''

'''
10
def evenodd(number):
    try:
        number = int(number)
        if number % 2 == 0:
            return "Even number"
        else:
            return "Odd number"
    except ValueError:
        return "Invalid input. Please enter a valid integer."

# Input from the user
try:
    input_number = input()
    result = evenodd(input_number)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid integer.")
'''

'''
11
def smallestnumber(number1, number2):
    try:
        number1, number2 = int(number1), int(number2)
        if number1 < number2:
            return number1
        else:
            return number2
    except ValueError:
        return "Invalid input. Please enter two valid integers."

# Input from the user
try:
    num1 = input()
    num2 = input()
    
    result = smallestnumber(num1, num2)
    print(result)
except ValueError:
    print("Invalid input. Please enter valid integers.")
'''

'''

12
def agegroup(age):
    try:
        age = int(age)
        if age <= 13:
            return "childhood"
        elif 14 <= age <= 24:
            return "youth"
        elif 25 <= age <= 59:
            return "maturity"
        else:
            return "old age"
    except ValueError:
        return "Invalid input. Please enter a valid age as an integer."

# Input from the user
try:
    user_age = input()
    result = agegroup(user_age)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid age as an integer.")
'''

'''
13
def triangle(side1, side2, side3):
    try:
        side1, side2, side3 = int(side1), int(side2), int(side3)
        if side1 == side2 == side3:
            return "Equilateral"
        elif side1 == side2 or side1 == side3 or side2 == side3:
            return "Isosceles"
        else:
            return "Versatile"
    except ValueError:
        return "Invalid input. Please enter valid positive integers."

# Input from the user
try:
    side1 = input()
    side2 = input()
    side3 = input()
    
    result = triangle(side1, side2, side3)
    print(result)
except ValueError:
    print("Invalid input. Please enter valid positive integers.")
'''
