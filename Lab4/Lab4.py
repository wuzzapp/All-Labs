'''
1.1
try:
    # Ввод строки
    user_input = input()

    # Вывод ошибки и прерывание работы если ввод имеет пробелы
    if ' ' in user_input:
        raise ValueError("String should not contain spaces")

    # Конвертация string в tuple
    input_tuple = tuple(user_input)

    # Вывод полученного tuple
    print("Created tuple is:")
    print(input_tuple)
except ValueError as ve:
    print("Error:", ve)
except Exception as e:
    print("An error occurred:", e)
'''
#В следующем таске нужно использовать tuple из прошлого таска, поэтому на защите я хотел просто удалить лишние части кода из 1.1 и запустить 1.2
#1.2 нормально работает таким образом
'''
1.2

    # Конвертация tuple в string при помощи метода join который обьединяет элементы строк
output_string = ''.join(input_tuple)

    
print("The string is:", output_string)
'''





'''
1.3
try:
#Ввод строк
    input_str_A = input()
    input_str_B = input()

    # Конвертация при помощи функции map которая применяет функция для каждого элемента. Метод split разделяет строку на список. 
    tuple_A = tuple(map(int, input_str_A.split(',')))
    tuple_B = tuple(map(int, input_str_B.split(',')))

    # Расчёт срединной точки, len нужен для возврата длины tuple и затем это делится на 2 
    midpoint = len(tuple_A) // 2

    # Обьединение половинок при помощи синтаксиса slice 
    result_tuple = tuple_A[:midpoint] + tuple_B[midpoint:]

    print(result_tuple)
except Exception as e:
    print("An error occurred:", e)
'''

'''
1.4
# Функция которая принимает кортеж и возвращает список пар (элемент, количество вхождений)
def count_elements_occurrences(input_tuple):
    element_count = {}  # Создаем словарь для подсчета количества вхождений каждого элемента
    
    # Проходим по каждому элементу в кортеже и увеличиваем соответствующее значение в словаре
    for element in input_tuple:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1

    return list(element_count.items())  # Возвращаем список пар (элемент, количество вхождений)

try:
    input_str = input() 

    elements = input_str.split(',')  # Разделяем строку по запятым и создаем список элементов
    input_tuple = tuple(elements)  

    output = count_elements_occurrences(input_tuple)  # Вызываем функцию для подсчета вхождений элементов

    print("Elements and their occurrences:")
    print(output) 

except Exception as e:
    print("An error occurred:", e)  

'''

'''
1.5
try:
    input_tuple = input()  
    splitted_tuple = input_tuple.split(',')  # Разделяем строку по запятым 

    integers = []  # Список для целых чисел
    floats = []  # Список для чисел с плавающей запятой
    strings = []  # Список для строк

    for item in splitted_tuple:
        item = item.strip()  # Удаляем лишние пробелы из элемента помощи метода strip который удаляет начальные и конечные элементы

        if item.isnumeric(): #isnumeric проверяет элемент на то число это или нет
            integers.append(int(item))  # Если элемент является целым числом добавляем его в список целых чисел при помощи функции append
        elif item.replace('.', '', 1).isdigit():
            floats.append(float(item))  # Если элемент является числом с плавающей запятой, добавляем его в список чисел с плавающей запятой
        else:
            strings.append(item)  # Остальное летит в строки

    print(integers)  
    print(floats)  
    print(strings)  

except Exception as e:
    print("An error occurred:", e)  # Обрабатываем и выводим ошибку, если она возникнет.

'''

'''

2.1
 # Get user input for a string 
user_input = input()

# Create a set from the input string using set comprehensions
input_set = {char for char in user_input}

# Print the created set
print("Created set is:")
print(input_set)
'''

'''

2.2
try:
    input_str_A = input(set_A = )
    input_str_B = input(set_B = )

    # Split user input and create sets
    set_A = set(map(int, input_str_A.split(',')))
    set_B = set(map(int, input_str_B.split(',')))

    # Calculate the symmetric difference between set_A and set_B
    symmetric_difference = set_A.symmetric_difference(set_B)

    # Print the resulting set
    print(symmetric_difference)
except Exception as e:
    print("An error occurred:", e)
'''

'''
2.3
try:
    # Sample Input: Two sets, set_A and set_B
    input_str_A = input()
    input_str_B = input()

    # Split user input and create sets
    set_A = set(map(int, input_str_A.split(',')))
    set_B = set(map(int, input_str_B.split(',')))

    # Remove elements from set_A that are in set_B
    set_A.difference_update(set_B)

    # Print the resulting set_A
    print(set_A)
except Exception as e:
    print("An error occurred:", e)
'''

'''
2.4
try:
    input_str_A = input("set_A =  ")
    input_str_B = input("set_B = ")
    input_str_C = input("set_C =  ")

    # Split user input and create sets
    set_A = set(map(int, input_str_A.split(',')))
    set_B = set(map(int, input_str_B.split(',')))
    set_C = set(map(int, input_str_C.split(',')))

    # Iterate over set_A and check if each element is in set_B
    # If it is, remove it from set_A and add it to set_C
    for element in set_A.copy():  # Create a copy of set_A to avoid modifying it during iteration
        if element in set_B:
            set_A.remove(element)
            set_C.add(element)

    # Print the updated set_C
    print("Updated set_C =", set_C)
except Exception as e:
    print("An error occurred:", e)
'''

'''
2.5
from itertools import combinations
import random

try:
    # Get user input for superset A, n, and m
    input_str_A = input("A = ")
    n = int(input("n = "))
    m = int(input("m = "))

    # Split user input and create the superset A
    A = set(map(int, input_str_A.split(',')))

    # Create a list of unique combinations from superset A
    unique_combinations = list(combinations(A, n))

    # Check if m is within a valid range
    if m > len(unique_combinations):
        print(f"Error: Value of m is too large. Maximum possible value for m is {len(unique_combinations)}.")
    else:
        # Randomly select m combinations from the list
        selected_combinations = random.sample(unique_combinations, m)

        # Create a list of sets using the selected combinations
        sets_list = [set(combination) for combination in selected_combinations]

        # Print the list of sets
        print(sets_list)
except Exception as e:
    print("An error occurred:", e)
'''

'''
3
try:
    cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

    # Create a dictionary to store the counts of models by manufacturer
    manufacturer_counts = {}

    # Iterate through the cars and count models by manufacturer
    for manufacturer, model in cars_list:
        if manufacturer in manufacturer_counts:
            manufacturer_counts[manufacturer][0] += 1
            manufacturer_counts[manufacturer][1].append(model)
        else:
            manufacturer_counts[manufacturer] = [1, [model]]

    # Print the table output
    for manufacturer, (count, models) in manufacturer_counts.items():
        print(f"{manufacturer} {count}")
        for model in models:
            print(f"- {model}")
except Exception as e:
    print("An error occurred:", e)
'''

