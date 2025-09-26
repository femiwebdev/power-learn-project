# Libraries are collections of pre-written code that can be used to perform common tasks, making it easier to develop applications.
# In Python, libraries can be imported using the `import` statement.
# Think of Library as a toolbox that contains useful tools (functions and methods) for specific tasks.

# How to use a Library; importing built-in library, datetime, importing part of a library, random,and creating your own library.
# importing built-in Library: python has several built-in libraries that you can use without installing anything extra. One of the most 
# commonly used built-in libraries is the `datetime` library, which allows you to work with dates and times.

# Example math
import math
print("The value of pi is:", math.pi)
print("The square root of 16 is:", math.sqrt(16))

# Importing part of a library example
from math import sqrt, pi, pow, sin, cos
print("The value of pi is:", pi)
print("The square root of 16 is:", sqrt(16))
print("2 raised to the power of 3 is:", pow(2, 3))
print("The sine of 90 degrees is:", sin(math.radians(90)))

# random
import random
print("A random number between 1 and 10:", random.randint(1, 10))

# Datetime 
import datetime
now = datetime.datetime.now()
print("Current date and time:", now)

# Python packages: these are third-party libraries that you can install using a package manager like pip and pypi. Others are flask, django, numpy, and pandas etc.
# Pip is a package manager for Python that allows you to install and manage additional libraries that are not part of the Python standard library. Pip comes with
# python 3.4 or newer as its default package manager. to install a package, you can use the following command:
# pip install package_name

# PyPI (Python Package Index) is a repository of software for the Python programming language. It is the default package index used by pip. pip pulls packages from 
# PyPI and installs them on your system. you can view and search for packages on the PyPI website: https://pypi.org/

# Popular Extra Python Libraries:
# TensorFlow – For machine learning and deep learning.
# Matplotlib – For creating charts and graphs.
# SciPy – For scientific and technical computing.
# Scrapy – For web scraping (getting data from websites).
# Scikit-learn – For machine learning (like predictions and classifications).
# PyGame – For building games with graphics and sound.
# PyTorch – For deep learning and neural networks.
# PyBrain – For beginners in machine learning and AI.

# NumPy – For numerical computing and working with arrays. Numerical operations are optimized for performance. pip install numpy is the command to install it.
# Numpy example
import numpy as np
# create simple array
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)

# perform operations
print("Array multiplied by 2:", arr * 2)
print("Array plus 5:", arr + 5)
print("Mean of the array:", np.mean(arr))
print("Sum of the array:", np.sum(arr))

arr_task = np.array([10, 15, 20, 25, 30, 35, 40, 45, 50])
# find the max and min of the array
print("Max of Task Array:", np.max(arr_task))
print("Min of Task Array:", np.min(arr_task))
# multiply all elements by 3
print("Task Array multiplied by 3:", arr_task * 3)

# Pandas – For handling and analyzing data. Work with tables (just like Excel or Google Sheets!) Clean and filter data easily. Read from CSV, Excel, JSON, etc.
# Example
import pandas as pd
# Create data frame like table-like feature
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print("Data Frame:")
print(df)

# access column and filter rows
print("Names:")
print(df['Name'])
print("Ages:")
print(df['Age'])
print("Cities:")
print(df['City'])   

#  Reading CSV Files with Pandas
""":df = pd.read_csv('students.csv')
print(df.head())"""  # Show first 5 rows 

# create a dataframe with 4 students: name, age, grade, and year
# add a column called passed with grade >50 = True
# Filter and display only students who passed
data_students = {
    'Name': ['John', 'Jane', 'Jim', 'Jill'],
    'Age': [20, 21, 19, 22],
    'Grade': [55, 45, 75, 85],
    'Year': [2022, 2023, 2022, 2024]
}
df_students = pd.DataFrame(data_students)
df_students['Passed'] = df_students['Grade'] > 50
print("Students who passed:")
print(df_students[df_students['Passed']])

# Matplotlib is a library that allows you to create visual representations of your data. It’s especially useful when working with data in Pandas or NumPy
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 40]

# Create a line plot
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

# Bar Chart Example
# Sample data
names = ['Alice', 'Bob', 'Charlie']
scores = [85, 90, 78]

plt.bar(names, scores, color='skyblue')
plt.title("Student Scores")
plt.xlabel("Students")
plt.ylabel("Scores")
plt.show()

# 🍰 Pie Chart Example
# Sample data
activities = ['Sleeping', 'Eating', 'Coding', 'Gaming']
hours = [8, 2, 8, 6]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Daily Activities")
plt.show()

# 📏 Histogram Example
# Example: showing frequency of values
ages = [22, 21, 20, 23, 24, 22, 20, 21, 22, 25, 23]

plt.hist(ages, bins=5, color='purple')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# 💡 Combine with Pandas Example
import pandas as pd

# Create a DataFrame
data = {
    'Year': [2021, 2022, 2023],
    'Users': [1500, 3000, 5000]
}

df = pd.DataFrame(data)

# Plot using pandas + matplotlib
plt.plot(df['Year'], df['Users'], marker='o')
plt.title("User Growth Over Time")
plt.xlabel("Year")
plt.ylabel("Users")
plt.grid(True)
plt.show()

# Create a bar chart showing 5 different countries and their population. Create a pie chart showing how a student spends 24 hours of their day.
# Make a line chart that shows temperature changes during the day (morning, noon, evening, night).
# Bar Chart task sample data of 5 different countries
countries = ['Nigeria', 'China', 'India', 'Brazil', 'UK']
population = [1331, 1439, 1380, 213, 68]  # in millions

plt.bar(countries, population, color='green')
plt.title("Population of 5 Countries (in millions)")
plt.xlabel("Countries")
plt.ylabel("Population")
plt.show()

# Pie Chart task sample data of how a student spends 24 hours of their day
activities = ['Sleeping', 'Eating', 'Studying', 'Gaming', 'Exercising']
hours = [8, 2, 6, 5, 3]

plt.pie(hours, labels=activities, autopct='%1.1f%%')
plt.title("Student's Daily Activities")
plt.show()

# Line Chart task sample data of temperature changes during the day
times = ['Morning', 'Noon', 'Evening', 'Night']
temperatures = [20, 30, 25, 15]

plt.plot(times, temperatures, marker='o')
plt.title("Temperature Changes Throughout the Day")
plt.xlabel("Time of Day")
plt.ylabel("Temperature (°C)")
plt.grid(True)
plt.show()

# Task 1: Import the following libraries:
# Create a NumPy array of numbers from 1 to 10 and calculate the mean. Load a small dataset into a 
# pandas DataFrame and display summary statistics. Fetch data from a public API using requests and print a key piece of information.
# Plot a simple line graph using matplotlib (e.g., a list of numbers)
import numpy as np
arr_task1 = np.array([1,2,3,4,5,6,7,8,9,10])
mean_value = np.mean(arr_task1)
print("Mean Value:", mean_value)

import pandas as pd

# Create a small DataFrame
data = {
    'Name': ['Jerome', 'Juliet', 'Iyanu', 'Treasure', 'Tofunmi', 'Oby', 'Folake', 'Cyril', 'Wendy'],
    'Age': [24, 27, 25, 26, 29, 24, 24, 30, 27],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas'],
    'Career': ['Engineer', 'Designer', 'Artist', 'Nurse', 'Scientist', 'Teacher', 'Developer', 'Lawyer', 'Manager']
}
df = pd.DataFrame(data)

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe(include='all'))
# Display the first few rows of the DataFrame
print("\nFirst 5 Rows:")
print(df.head())

# request data from public API
import requests
r = requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))
if r.status_code == 200:
    print("Authentication successful!")

