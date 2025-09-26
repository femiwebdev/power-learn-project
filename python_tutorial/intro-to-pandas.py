# Objectives:
# Use Python libraries to handle and analyze data. Learn to perform basic data manipulation with pandas. Understand data analysis techniques such as filtering,
# sorting, and aggregating data. Gain insight into data visualization using matplotlib.

# Introduction to Pandas: Creating, Reading, and Manipulating DataFrames
# Pandas: is an open-source Python library that provides high-performance, easy-to-use data structures and data analysis tools. It is primarily used for working 
# with tabular data in the form of DataFrames. It allows you to efficiently manipulate, clean, and analyze structured data.

# Series: A one-dimensional labeled array that can hold any data type (integers, strings, etc.).
# DataFrame: A two-dimensional, size-mutable, potentially heterogeneous tabular data structure with labeled axes (rows and columns).

# Key Operations in pandas:
# Creating DataFrames: You can create a DataFrame by loading data from various formats like CSV, Excel, or SQL databases. For example:
import pandas as pd

# Creating DataFrame from a dictionary
data = {'Name': ['John', 'Bobby', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['Edo', 'Keffi', 'Ibadan']}

df = pd.DataFrame(data)
print(df)

# Reading Data: pandas allows you to load data from multiple sources, such as:
# Read data from a CSV file
# df = pd.read_csv('data.csv')

# Manipulating DataFrames:
# Selecting Columns: You can select a specific column like this:
df['Age']  # Selects the Age column
print(df)

# Filtering Rows: You can filter rows based on a condition:
df[df['Age'] > 30]  # Returns rows where Age > 30
print(df)

# Adding/Removing Columns:
df['Country'] = ['Nigeria', 'Nigeria', 'Nigeria']  # Adds a new column
df.drop('Country', axis=1, inplace=True)  # Drops the 'Country' column
print(df)

# Basic Filtering: To filter data based on conditions, you can use boolean indexing.
# Get rows where Age is greater than 30
df_filtered = df[df['Age'] > 30]
print(df_filtered)

# Multiple Conditions: You can combine multiple conditions using logical operators:
# Get rows where Age is greater than 30 and City is 'Keffi'
df_filtered = df[(df['Age'] > 30) & (df['City'] == 'Keffi')]
print(df_filtered)

# Sorting by Columns: You can sort the DataFrame by a column in ascending or descending order:
df_sorted = df.sort_values(by='Age', ascending=False)  # Sort by Age in descending order
print(df_sorted)

# Sorting by Multiple Columns:
df_sorted = df.sort_values(by=['Age', 'City'], ascending=[True, False])
print(df_sorted)

# Groupby: pandas groupby method is essential for aggregating data based on one or more columns. For example:
grouped = df.groupby('City').agg({'Age': 'mean', 'Name': 'count'})
print(grouped)

# Summary Statistics: pandas provide several built-in functions to calculate summary statistics:
df['Age'].mean()  # Mean of 'Age' column
df['Age'].sum()   # Sum of 'Age' column
df['Age'].max()   # Maximum of 'Age' column
print(df['Age'].describe())  # Summary statistics for 'Age' column

# Best Practices for Working with Data and Basic Data Analysis: Data Cleaning: Before analysis, always ensure the data is clean. This includes handling missing 
# values (df.fillna()), removing duplicates (df.drop_duplicates()), and dealing with outliers. Efficient Data Access: pandas provides several ways to read large 
# datasets efficiently. For example, use chunksize to read large CSV files in chunks. Handling Data Types: Ensure the data types of your columns are correct 
# (e.g., using df['Age'] = df['Age'].astype(int)).

# Documentation: When working on analysis, make sure to document your code and the reasoning behind each transformation or computation.