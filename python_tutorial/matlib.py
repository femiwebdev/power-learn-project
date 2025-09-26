# matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It's often used for visualizing the results of data 
# analysis. The most common form of visualization is through line plots, scatter plots, bar plots, and histograms.

# Basic Plotting with matplotlib
# Simple Line Plot:
import matplotlib.pyplot as plt
import pandas as pd
df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
})

# Plotting Age vs. Name
plt.plot(df['Name'], df['Age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Name vs Age')
plt.show()

# Bar Plot: Plotting a bar chart for Age by City
df.groupby('City')['Age'].mean().plot(kind='bar')
plt.xlabel('City')
plt.ylabel('Average Age')
plt.title('Average Age by City')
plt.show()

# Histogram: Plotting a histogram for Age
df['Age'].plot(kind='hist', bins=10)
plt.xlabel('Age')
plt.title('Age Distribution')
plt.show()

# Scatter Plot: Plotting a scatter plot of Age vs. City
df.plot(kind='scatter', x='City', y='Age')
plt.title('City vs Age')
plt.show()

# Customizing Plots: Adding Labels and Title:
plt.xlabel('City')
plt.ylabel('Average Age')

# Plotting a scatter plot of Age vs. City
df.plot(kind='scatter', x='City', y='Age')
plt.title('City vs Age')
plt.show()

# Customizing Plots: Adding Labels and Title:
plt.xlabel('City')
plt.ylabel('Average Age')
plt.title('Average Age by City')

# Color and Style:
df['Age'].plot(kind='line', color='green', linestyle='--', linewidth=2)

# Best Practices for Working with Data and Basic Data Analysis: Data Cleaning: Before analysis, always ensure the data is clean. This includes handling missing 
# values (df.fillna()), removing duplicates (df.drop_duplicates()), and dealing with outliers. Efficient Data Access: pandas provides several ways to read large 
# datasets efficiently. For example, use chunksize to read large CSV files in chunks. Handling Data Types: Ensure the data types of your columns are correct 
# (e.g., using df['Age'] = df['Age'].astype(int)).

# Documentation: When working on analysis, make sure to document your code and the reasoning behind each transformation or computation.