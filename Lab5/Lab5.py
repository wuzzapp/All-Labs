'''
1.1
string = input()

# Converting 
list_lowercase = list(string.lower())

print("Created list is:")
print(list_lowercase)
'''


'''
1.2
# Empty dictionary to store the symbol frequencies
symbols_count = {}

# Count the frequency of each symbol in the list
for symbol in list_lowercase:
    if symbol in symbols_count:
        symbols_count[symbol] += 1
    else:
        symbols_count[symbol] = 1

# Converting
frequency_list = list(symbols_count.items())

print(frequency_list)
'''

'''
1.3
list_vow = []
list_cons = []
list_symb = []

# Function to check if a character is a vowel
def is_vowel(char):
    return char in 'aeiouAEIOU'

# Spliting the list into three lists
for char, count in frequency_list:
    if is_vowel(char):
        list_vow.append((char, count))
    elif char.isalpha():
        list_cons.append((char, count))
    else:
        list_symb.append((char, count))

# Display the three new lists
print(f"list_vow = {list_vow}")
print(f"list_cons = {list_cons}")
print(f"list_symb = {list_symb}")
'''

'''
1.4
input_list = input()

elements = input_list.split()

# Convert
list_A = [int(element) for element in elements]

# Sort the list
sorted_list = sorted(list_A)

# Determine the quartiles
length = len(sorted_list)
q1_group = length // 4

# Calculate the number of elements per quartile
elements_per_quartile = q1_group

# Calculate the number of zeros needed to make it divisible by 4
zeros_needed = 4 - (length % 4)

# Extend list_A with zeros
list_A.extend([0] * zeros_needed)

# Re-sort the extended list
sorted_list = sorted(list_A)

# Recalculate the quartile boundaries
length = len(sorted_list)
q1_group = length // 4

# Divide the list into quartiles
q1 = sorted_list[:q1_group]
q2 = sorted_list[q1_group:q1_group * 2]
q3 = sorted_list[q1_group * 2:q1_group * 3]
q4 = sorted_list[q1_group * 3:]

print(f"q1 = {q1}")
print(f"q2 = {q2}")
print(f"q3 = {q3}")
print(f"q4 = {q4}")
'''

'''
2.1
name1 = str(input('Student name - '))
assignments1 = input('scores for assignments: ')
assignments_scores1 = list(map(int, assignments1.split()))
labs1 = input('labs: ')
labs_scores1 = list(map(float, labs1.split()))
tests1 = input('tests: ')
tests_scores1 = list(map(float, tests1.split()))

student1 = {
      'name': name1,
      'assignment': assignments_scores1,
      'test': tests_scores1,
      'lab': labs_scores1,
  }

#print(student)


2.2
submission_check = 0
if 'assignment' in student1 and len(student1['assignment']) == 4:
    submission_check += 4
if 'test' in student1 and len(student1['test']) == 2:
    submission_check += 2
if 'lab' in student1 and len(student1['lab']) == 2:
    submission_check += 2


submission_check = {student1['name']: submission_check}

#print(student)
print(submission_check)




2.3
name2 = str(input('Student name - '))
assignments2 = input('scores for assignments: ')
assignments_scores2 = list(map(int, assignments2.split()))
labs2 = input('labs: ')
labs_scores2 = list(map(float, labs2.split()))
tests2 = input('tests: ')
tests_scores2 = list(map(float, tests2.split()))

student2 = {
      'name': name2,
      'assignment': assignments_scores2,
      'test': tests_scores2,
      'lab': labs_scores2,
  }

submission_check2 = 0
if 'assignment' in student2 and len(student2['assignment']) == 4:
    submission_check2 += 4
if 'test' in student2 and len(student2['test']) == 2:
    submission_check2 += 2
if 'lab' in student2 and len(student2['lab']) == 2:
    submission_check2 += 2

    submission_check2 = {student2['name']: submission_check2}
    print(submission_check2)

else:
    submission_check2 = {student2['name']: len(student2['assignment']) + len(student2['test']) + len(student2['lab'])}
    print(submission_check2)            
#print(student2)



if student1['name'] in submission_check and submission_check[student1['name']] >= 4:
    assignment_avg = sum(student1['assignment']) / len(student1['assignment'])
    lab_avg = sum(student1['lab']) / len(student1['lab'])
    test_avg = sum(student1['test']) / len(student1['test'])
    final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg

    
    student1['final_grade'] = round(final_grade, 2)
else:
    
    student1['final_grade'] = 0

if student2['name'] in submission_check2 and submission_check2[student2['name']] >= 4:
    assignment_avg = sum(student2['assignment']) / len(student2['assignment'])
    lab_avg = sum(student2['lab']) / len(student2['lab'])
    test_avg = sum(student2['test']) / len(student2['test'])
    final_grade = 0.3 * assignment_avg + 0.5 * lab_avg + 0.2 * test_avg

    
    student2['final_grade'] = round(final_grade, 2)
else:
    
    student2['final_grade'] = 0

#print(student)
#print(student2)


2.4
students = {}


student_list = [student1, student2]

for student in student_list:
    student_name = student['name']
    students[student_name] = {
        'assignment': student.get('assignment', []),
        'test': student.get('test', []),
        'lab': student.get('lab', []),
        'final_grade': student.get('final_grade', 0)
    }

print("students =", students)
'''

'''
3
print("Enter transactions in the format (user_id, transaction_type). Enter 'f' to finish.")

transactions = []
while True:
    user_input = input("Enter a transaction (e.g., 1001, 2): ")
    if user_input.lower() == 'f':
        break
    try:
        user_id, transaction_type = map(int, user_input.split(','))
        transactions.append((user_id, transaction_type))
    except ValueError:
        print("Invalid input. Enter the correct format.")

# Initialize dictionaries to store user statistics and transaction order.
stats = {}
transaction_order = {}

# Process user transactions.
for user_id, transaction_type in transactions:
    if user_id not in stats:
        stats[user_id] = {1: 0, 2: 0, 3: 0, 'mft': None, 'lft': None}
        transaction_order[user_id] = []

    stats[user_id][transaction_type] += 1
    transaction_order[user_id].append(transaction_type)

# Calculate most and least frequent transactions for each user.
for user_id, user_stats in stats.items():
    most_frequent_transaction = max(user_stats, key=lambda x: user_stats[x] if x in [1, 2, 3] else 0)

    least_frequent_transaction = None
    for transaction_type in [2, 3, 1]:
        if transaction_type in transaction_order[user_id]:
            least_frequent_transaction = transaction_type
            break

    user_stats['mft'] = most_frequent_transaction
    user_stats['lft'] = least_frequent_transaction

# Display user statistics.
print("stats =", stats)
'''

