'''
1
def display_file_content(file_name):
    try:
        with open(file_name, 'r') as file:
            for line in file:
                print(line, end='')
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "text1.txt"
display_file_content(file_name)
'''

'''
2
import random

def read_random_line(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            if lines:
                random_line = random.choice(lines)
                print("Random line is:", random_line.strip())
            else:
                print("File is empty.")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "text1.txt"  
read_random_line(file_name)
'''

'''
3
def count_uppercase_characters(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            uppercase_count = sum(1 for char in content if char.isupper())
            print("Number of Uppercase Characters:", uppercase_count)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "text1.txt" 
count_uppercase_characters(file_name)
'''

'''
4
def count_lines_not_starting_with_D(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            lines_without_D = [line.strip() for line in lines if not line.startswith('D')]
            count = len(lines_without_D)
            print(count)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "No_D.txt"  
count_lines_not_starting_with_D(file_name)
'''

'''
5
def count_words_ending_with_F(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            words = content.split()
            words_ending_with_F = [word.strip(".,!?") for word in words if word.lower().endswith('f')]
            count = len(words_ending_with_F)
            print(count)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "Ends_F.txt"  
count_words_ending_with_F(file_name)
'''

'''
6
def count_all_and_none_words(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read().lower()  # Convert the content to lowercase for case-insensitive matching
            count_all = content.count("all ")
            count_none = content.count("none ")
            print("Number of occurrences of 'all':", count_all)
            print("Number of occurrences of 'none':", count_none)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "all_none.txt"  
count_all_and_none_words(file_name)
'''

'''
7
from collections import Counter
import string

def count_word_frequency(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read().lower()  # Convert the content to lowercase for case-insensitive matching
            words = content.translate(str.maketrans('', '', string.punctuation)).split()
            word_frequency = Counter(words)
            
            # Print the word frequency
            print("Word Frequency:")
            for word, frequency in word_frequency.items():
                print(f"{word}: {frequency}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "text1.txt" 
count_word_frequency(file_name)
'''

'''
8
def find_longest_word(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read().lower()  # Convert the content to lowercase for case-insensitive matching
            words = content.translate(str.maketrans('', '', ",.!?")).split()  # Remove common punctuation
            longest_word = max(words, key=len)
            print(longest_word)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "text1.txt" 
find_longest_word(file_name)
'''

'''
9
def replace_chars_in_file(file_name, original_char, replacement_char):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            corrected_content = content.replace(original_char.lower(), replacement_char.lower())
            
            # Display the corrected version of the content
            print("Corrected Version:")
            print(corrected_content)
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_name = "b_to_j.txt"  
replace_chars_in_file(file_name, 'B', 'J')
'''

'''
10
def count_occurrences_of_A_and_B(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            
            # Count occurrences of 'A' and 'B' (case-insensitive)
            count_A = content.lower().count('a')
            count_B = content.lower().count('b')
            
            # Display the occurrences
            print(f"Occurrences of a: {count_A}")
            print(f"Occurrences of b: {count_B}")
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

file_name = "a_and_b.txt"  
count_occurrences_of_A_and_B(file_name)
'''