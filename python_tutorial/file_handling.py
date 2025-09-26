# File Handling and Exception Handling Assignment
# File handling is the ability to read and write files on a computer. Files are used to store data permanently (documents like
# texts, images, spreadsheets, and other media). Unlike Variables, which store data temporarily during program execution,
# files provide a way to save data for future use.

# File handling in Python allows you to create, read, update, and delete files. You can work with different file formats, such as text files, CSV files, and JSON files.
# Python's built-in open() function is used to open a file and returns a file object, which provides methods and attributes to interact with the file content. It is at the
# heart of this process, and learning how to use it effectively is crucial for any Python developer.

# The basics of file handling in Python include:
# 1. Opening a file
# 2. Reading from a file
# 3. Writing to a file
# 4. Closing a file

# Opening Files
# To open a file in Python, you use the open() function. The basic syntax is:
# open(file, mode)
# - file: The name of the file you want to open (including the file extension).
# - mode: The mode in which you want to open the file (e.g., "r" for reading, "w" for writing).

# file = open(filename, mode)    where filename is file you want to work with, and mode is the mode you want to use
# Modes include: 'r' for reading, 'w' for writing, 'a' for appending, 'rb' 'wb' binary modes for non-text files, like images
# Example:
from xml.dom.minidom import Document


file = open("example.txt", "r")   # opens example.txt in read mode

# Reading Files: with multiple ways to read file contents.
# Python provides several methods to read file contents:
# 1. read(): Reads the entire file content as a single string.
# 2. readline(): Reads a single line from the file.
# 3. readlines(): Reads all lines and returns a list of strings.

# Example: 
file = open("example.txt", "r")   # opens example.txt in read mode
content = file.read()
file.close()
print(content)  # prints the content of the file

# Use Cases
# 1. Configuration files: Reading settings from a config file at startup.
# 2. Data processing: Reading data files for analysis or processing.
# 3. Log files: Reading log files to monitor application behavior.

# Writing Files: To write to a file, you can use the "w" mode (write) or "a" mode (append).
file = open("output.txt", "w")   # opens output.txt in write mode
file.write("Hello, World!")
file.close()

# Appending to Files: To append to a file, you can use the "a" mode (append).
file = open("output.txt", "a")   # opens output.txt in append mode
file.write("\nHello, Again!")
file.close()

# Closing Files: It is important to close files after you are done working with them to free up system resources.
file.close()  # closes the file
# Python's with statement simplifies file handling by automatically closing the file for you.
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

    # Example: Using with statement for writing
    with open("output.txt", "w") as file:
        file.write("Hello, World!")

# Exception Handling: When working with files, it's important to handle potential errors, such as file not found or permission denied.
try:
    with open("non_existent_file.txt", "r") as file:  # Attempt to open a non-existent file
        content = file.read()  # Attempt to read the file
except FileNotFoundError:  # Handle file not found error
    print("File not found.")
except Exception as e:  # Handle other exceptions
    print("Error:", e)

# Advanced Error Handling with Finally and customs Error
# Finally runs no matter what, often used to clean up (like closing a file)

# Best Practices: Use with for file handling: Auto-close files, preventing potential leaks.
# Check file existence before reading/writing, to avoid crashes.
# Handle specific exceptions over general ones (e.g., FileNotFoundError instead of Exception).
# Document error messages clearly for easier debugging and user support.


# File Handling and Exception Handling Assignment
# Create a program that reads a text file, processes its content, and writes the results to a new file

def process_file(input_file, output_file):
    try:
        with open(input_file, "r") as input_file_handle:
            content = input_file_handle.read()

        word_count = len(content.split())

        uppercase_content = content.upper()

        with open(output_file, "w") as output_file_handle:
            output_file_handle.write(f"WORD COUNT: {word_count}\n")
            output_file_handle.write("=" * 40 + "\n")
            output_file_handle.write(uppercase_content)

        print(f"Success! File processed successfully.")
        print(f"Word count: {word_count}")
        print(f"Processed content has been written to '{output_file}'")

    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied. Cannot read or write to the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        print("File processing complete.")

if __name__ == "__main__":
    process_file(r"c:\Users\olaro\femiweb-apps\power_learn_project\python_tutorial\input.txt", 
                 r"c:\Users\olaro\femiweb-apps\power_learn_project\python_tutorial\output.txt")

