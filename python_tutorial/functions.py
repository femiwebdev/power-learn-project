# A function is a reusable block of code that performs a specific task.
# It can take inputs, called parameters, and can return an output.

def function_name(parameters):
    # Code to perform a specific task
    return  # optional return statement


#Types of Functions: 1. Built-in Functions and user-defined Functions

# Built-in Functions: These are functions that are pre-defined in Python.
# Examples include print(), len(), and range().

# User-defined Functions: These are functions that you create yourself.
# They allow you to encapsulate code for reuse and better organization.

# Defining and calling a function
def greet(name):
    return f"Hello, {name}!"

# Calling the function
print(greet("Alice"))  # output: Hello, Alice!

# Key components of a function:
# 1. Function Name: The name of the function (e.g., greet).
# 2. Parameters: Inputs to the function (e.g., name).
# 3. Docstring: A string that describes the function's purpose (e.g., """Greet a person by name.""" ).
# 4. Return Statement: Specifies the output of the function (e.g., return f"Hello, {name}!").

# Parameters and Arguments:
# - Parameters are the variables listed inside the parentheses in the function definition.
# - Arguments are the actual values passed to the function when it is called.

# Functions can accept zero or more arguments.
# Positional Arguments: These are arguments that are passed to a function in the order in which they are defined.
def add(a, b):
    return a + b
print(add(2, 3))  # output: 5


# Keyword Arguments: These are arguments that are passed to a function by explicitly specifying the parameter name.
def greet(name, message, age):
    return f"{message}, {name}! You are {age}."
print(greet(message="Hi", name="Alice", age=30))  # output: Hi, Alice! You are 30.


# Default Arguments: These are arguments that assume a default value if a value is not provided.
# Parameters can have default values.
def greet(name, message="Hello"):
    return f"{message}, {name}!"
print(greet("Alice"))  # output: Hello, Alice!


# Calling the function with and without the default argument
print(greet("Alice"))  # output: Hello, Alice!
print(greet("Bob", "Hi"))  # output: Hi, Bob!


# Functions can return multiple values
def get_user_info():
    name = "Alice"
    age = 30
    return name, age
print(get_user_info())  # output: ('Alice', 30)

user_info = get_user_info()
print(user_info)  # output: ('Alice', 30)


# Returning Values: A function can return a single value or multiple values using the return statement.
def calculate_area(length, width):
    return length * width
result = calculate_area(5, 3)
print(result)  # output: 15


# Anonymous Functions: Lambda Functions
# Lambda functions are small, anonymous functions defined with the lambda keyword.
# They can have any number of parameters but only one expression.
square = lambda x: x ** 2
print(square(5))  # output: 25

# Lambda function for adding two numbers
add = lambda x, y: x + y
print(add(2, 3))  # output: 5

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # output: [1, 4, 9, 16, 25]

# Recursive functions
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))  # output: 120

# Benefits of Functions
# 1. Code Reusability: Functions allow you to reuse code without repeating it.
# 2. Modularity: Functions help break down complex problems into smaller, manageable parts.
# 3. Abstraction: Functions provide a way to hide implementation details and expose only the necessary parts.
# 4. Easier Testing: Functions can be tested individually, making it easier to identify and fix bugs.

# Conclusion
# Functions are a fundamental building block in programming. They promote code reusability, modularity, and abstraction, 
# making it easier to manage and maintain code. By understanding how to define and use functions effectively, 
# you can write cleaner, more efficient, and more organized code.