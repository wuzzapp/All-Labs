import requests

class ToDo:
    def __init__(self, userId, id, title, completed):
        self.userId = userId
        self.id = id
        self.title = title
        self.completed = completed

# 1.1: GET Request
post_id = 1  # replace with the desired post_id
url_get = f"https://jsonplaceholder.typicode.com/todos/{2}"

response_get = requests.get(url_get)

print("GET Request Response:")
if response_get.status_code in range(400, 600):
    print(f"Error: {response_get.status_code}")
else:
    print(response_get.json())

# 1.2: Create a class "ToDo" and 1.3: Create a new object of class ToDo
# Using the response from the GET request to create a ToDo object
if response_get.status_code == 200:
    todo_data = response_get.json()
    new_todo = ToDo(userId=todo_data['userId'], id=todo_data['id'], title=todo_data['title'], completed=todo_data['completed'])

# 1.4: POST Request
new_todo_dict = {
    "userId": new_todo.userId,
    "title": new_todo.title,
    "completed": new_todo.completed
}

url_post = "https://jsonplaceholder.typicode.com/todos"
response_post = requests.post(url_post, json=new_todo_dict)

print("\nPOST Request Response:")
if response_post.status_code in range(400, 600):
    print(f"Error: {response_post.status_code}")
else:
    print(response_post.json())

# 1.5: Edit some data of your attributes of your todo item
new_todo.completed = not new_todo.completed  # changing the completion status

# 1.6: PUT Request
url_put = f"https://jsonplaceholder.typicode.com/todos/{7}"
response_put = requests.put(url_put, json=new_todo_dict)

print("\nPUT Request Response:")
if response_put.status_code in range(400, 600):
    print(f"Error: {response_put.status_code}")
else:
    print(response_put.json())
