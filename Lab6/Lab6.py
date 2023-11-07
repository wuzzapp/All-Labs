'''
1
def get_keys_with_value_true(input_dict):
    try:
        if not isinstance(input_dict, dict):
            raise ValueError("Input must be a dictionary")
        return [key for key, value in input_dict.items() if value is True]
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

dict = {
    "a": True,
    "b": False,
    "c": True
}

result = get_keys_with_value_true(dict)
print(result)  
'''

'''
2
def get_unique_elements(input_list):
    try:
        if not isinstance(input_list, list):
            raise ValueError("Input must be a list")
        unique_elements = [x for x in input_list if input_list.count(x) <= 1]
        return unique_elements
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

try:
    input_list = input()
    input_list = list(map(int, input_list.split()))
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
    input_list = []

result = get_unique_elements(input_list)
print(result)
'''

'''
3
def get_date_in_format(date):
    try:
        if not isinstance(date, str) or len(date) != 10 or date[4] != '.' or date[7] != '.':
            raise ValueError("Invalid date format. Please use 'yyyy.mm.dd' format.")
        year, month, day = date.split('.')
        return f"{day}.{month}.{year}"
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""


try:
    input_date = input()
    result = get_date_in_format(input_date)
    print(result)
except ValueError:
    print("Invalid input. Please use 'yyyy.mm.dd' format.")
'''

'''
4
def get_elements_with_no_more_than_two_occurrences(input_list):
    try:
        if not isinstance(input_list, list):
            raise ValueError("Input must be a list")
        result = []
        for item in input_list:
            if 1 < input_list.count(item) <= 2 and item not in result:
                result.append(item)
        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return []

try:
    input_list = input()
    input_list = list(map(int, input_list.split()))
except ValueError:
    print("Invalid input. Please enter numbers separated by spaces.")
    input_list = []

result = get_elements_with_no_more_than_two_occurrences(input_list)
print(result)
'''

'''
5
def get_words_from_string(input_string):
    try:
        if not isinstance(input_string, str):
            raise ValueError("Input must be a string")
        words = input_string.split()
        return words
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


try:
    input_string = input()
except ValueError:
    print("Invalid input. Please enter a valid string.")
    input_string = ""

result = get_words_from_string(input_string)
print(result)
'''

'''
6
def get_unique_elements_with_count(input_list):
    try:
        if not isinstance(input_list, list):
            raise ValueError("Input must be a list")
        unique_elements = {}
        for item in input_list:
            if item in unique_elements:
                unique_elements[item] += 1
            else:
                unique_elements[item] = 1
        return unique_elements
    except Exception as e:
        print(f"An error occurred: {e}")
        return {}


try:
    input_list = input()
    input_list = list(map(int, input_list.split()))
except ValueError:
    print("Invalid input. Please enter elements separated by spaces.")
    input_list = []

result = get_unique_elements_with_count(input_list)
print(result)
'''

'''
7
def get_prime_numbers(n):
    try:
        if not isinstance(n, int) or n < 2:
            raise ValueError("Input must be an integer greater than or equal to 2")
        prime_numbers = []
        for num in range(2, n + 1):
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)
        return prime_numbers
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


try:
    n = int(input("n = "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    n = 0

result = get_prime_numbers(n)
print(result)
'''

'''
8
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def get_prime_numbers_in_list(numbers):
    prime_numbers = [num for num in numbers if is_prime(num)]
    return prime_numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 27, 36, 48, 54, 67, 71, 73, 75, 83, 89, 99]

result = get_prime_numbers_in_list(numbers)
print(result)
'''

'''
9
from datetime import datetime

def get_difference_between_dates(date1, date2):
    date_format = "%Y.%m.%d"
    
    try:
        date1_obj = datetime.strptime(date1, date_format)
        date2_obj = datetime.strptime(date2, date_format)
        date_difference = abs((date2_obj - date1_obj).days)
        return date_difference
    except ValueError:
        return "Invalid date format. Please use YYYY.MM.DD."

# Input dates from the console
date1 = input()
date2 = input()

result = get_difference_between_dates(date1, date2)
print(result)
'''

'''
10
def get_decimal_number_from_binary_string():
    binary_string = input()
    decimal_number = int(binary_string, 2)
    return decimal_number

decimal_number = get_decimal_number_from_binary_string()
print(decimal_number)
'''

'''
11
def is_perfect_square(n):
    return n > 0 and int(n**0.5)**2 == n

def are_all_perfect_squares(numbers):
    for num in numbers:
        if not is_perfect_square(num):
            return False
    return True

input_numbers = input()
numbers = [int(num.strip()) for num in input_numbers.split(',')]
result = are_all_perfect_squares(numbers)
print(result)
'''

'''
12
def sort_shopping_list_by_price(shopping_list):
    sorted_list = sorted(shopping_list, key=lambda item: item['price'])
    return sorted_list

shopping_list = [
    {"name": "Apple", "price": 100},
    {"name": "Banana", "price": 50},
    {"name": "Orange", "price": 20}
]

sorted_shopping_list = sort_shopping_list_by_price(shopping_list)
print(sorted_shopping_list)
'''

'''
13
def get_words_starting_with_vowel(words):
    vowels = "AEIOUaeiou"
    vowel_words = [word for word in words if word[0] in vowels]
    return vowel_words

word_list = ["apple", "banana", "orange", "bear", "cat"]
vowel_words = get_words_starting_with_vowel(word_list)
print(vowel_words)
'''
