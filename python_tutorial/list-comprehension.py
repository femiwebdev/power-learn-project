# A list comprehension is a concise way to create lists in Python.
# It consists of brackets containing an expression followed by a for clause,
# and can include optional if clauses.

# Example: Using the traditional loop
squares = []
for x in range(10):
    squares.append(x**2)

# This can be rewritten using list comprehension for brevity and clarity.
# Example: Using list comprehension
squares = [x**2 for x in range(10)]
print(squares) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Example: List comprehension with a condition
evens = [x**2 for x in range(10) if x % 2 == 0]
print(evens) # output: [0, 4, 16, 36, 64]


# Example: Nested list comprehension
matrix = [[j for j in range(5)] for i in range(3)]
print(matrix) # output: [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]


# Example: List comprehension with Transforming Data
names = ["Alice", "Bob", "Charlie"]
uppercased = [name.upper() for name in names]
print(uppercased) # output: ['ALICE', 'BOB', 'CHARLIE']


# Example: List comprehension with Filtering Data
filtered = [name for name in names if 'a' in name.lower()]
print(filtered) # output: ['Alice', 'Charlie']


# Example: Flattening a nested list
flattened = [j for sublist in matrix for j in sublist]
print(flattened) # output: [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]


# Example: List comprehension with multiple for clauses
combinations = [(x, y) for x in range(3) for y in range(2)]
print(combinations) # output: [(0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1)]


# Example: List comprehension with a function
def square(x):
    return x**2

squared = [square(x) for x in range(10)]
print(squared) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Example: List comprehension with a method
class Math:
    @staticmethod
    def square(x):
        return x**2

squared = [Math.square(x) for x in range(10)]
print(squared) # output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


# Advantages of List Comprehensions: Conciseness, Performance, and Readability
# When not to use: If the logic is too complex, a regular loop may be more readable.
# Conclusion: List comprehensions are a powerful tool in Python, offering a more readable and concise way to create lists.