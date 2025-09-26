# Challenge: Implement a grading system based on user input
# The program will ask for the user's name and grade, then print a message based on the grade
name = input("Enter your name: ")
grade = int(input("Enter your grade: "))

if grade >= 90:
    print("A")
    print("Outstanding performance!")

elif grade >= 80:
    print("B")
    print("Great job!")

elif grade >= 70:
    print("C")
    print("Good effort!")

elif grade >= 60:
    print("D")
    print("Keep trying!")

else:
    print("F")
    print("Need improvement!")

print(f"Your grade is: {grade}")
print(f"Thank you, {name}, for your input!")


# Challenge: Implement a function to check if a number is a large power
def large_power(base, exponent):
    if base ** exponent > 5000:
        return True
    else:
        return False
print(large_power(1, 5001))


# Challenge: Implement a function to check if a number is divisible by 10
def divisible_by_ten(num):
    if num % 10 == 0:
        return True
    else:
        return False
print(divisible_by_ten(20))

# Challenge: Implement a function to calculate discount price, percentage, 
# and final price after applying the discount. if the discount is 20% or higher, 
# apply discount, else return the original price. use calculate_discount function 
# to prompt the user to enter the original price of an item and discount percentage, 
# print final price after applying discount, if no discount was applied, print the original price

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price
    
# Prompt User for input and calculate discount
try:
    original_price = float(input("Enter the original price of the item: N"))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    if discount_percent >= 20:
        discount_amount = original_price * (discount_percent / 100)
        print(f"Discount applied: {discount_percent}%")
        print(f"You saved: N{discount_amount:.2f}")
        print(f"Final price after discount: N{final_price:.2f}")
    else:
        print(f"No discount applied (discount must be 20% or higher)")
        print(f"Original price: N{original_price:.2f}")

except ValueError:
    print("Please enter a valid numeric value for price and discount percentage.")


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

# Create a program that reads a file and writes a modified version to a new file.
# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
import os
def read_and_modify_file():
    input_file = input("Enter the input file name (with extension): ")
    output_file = input("Enter the output file name (with extension): ")

    try:
        with open(input_file, "r") as infile:
            content = infile.read()
            # Modify the content (for example, convert to uppercase)
            modified_content = content.upper()

        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"Successfully processed '{input_file}' and created '{output_file}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_file}' or write to '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    read_and_modify_file()


# Another version of same program but this time with a twist
import os
import csv
import tkinter as tk
from tkinter import filedialog

# For PDF support, you'll need to install: pip install PyPDF2
try:
    import PyPDF2

    PDF_AVAILABLE = True
except ImportError:
    PDF_AVAILABLE = False
    print("Note: PyPDF2 not installed. PDF support disabled.")


def read_pdf_file(file_path):
    """Read content from a PDF file"""
    if not PDF_AVAILABLE:
        raise Exception("PyPDF2 library not installed. Cannot read PDF files.")

    content = ""
    with open(file_path, "rb") as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            content += page.extract_text() + "\n"
    return content


def read_csv_file(file_path):
    """Read content from a CSV file"""
    content = ""
    with open(file_path, "r", newline="", encoding="utf-8") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            content += ",".join(row) + "\n"
    return content


def read_txt_file(file_path):
    """Read content from a TXT file"""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def get_file_from_dialog():
    """Open file dialog to select a file"""
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    file_types = [
        ("All supported", "*.txt;*.csv"),
        ("Text files", "*.txt"),
        ("CSV files", "*.csv"),
        ("All files", "*.*")
    ]

    if PDF_AVAILABLE:
        file_types.insert(1, ("PDF files", "*.pdf"))
        file_types[0] = ("All supported", "*.txt;*.csv;*.pdf")

    file_path = filedialog.askopenfilename(
        title="Select a file to process",
        filetypes=file_types
    )

    root.destroy()
    return file_path


def read_and_modify_file():
    print("File Import Options:")
    print("1. Enter file path manually")
    print("2. Browse and select file")

    choice = input("Choose an option (1 or 2): ").strip()

    if choice == "2":
        try:
            input_file = get_file_from_dialog()
            if not input_file:
                print("No file selected. Exiting...")
                return
        except Exception as e:
            print(f"Error opening file dialog: {e}")
            print("Falling back to manual file path entry...")
            input_file = input("Enter the input file path: ").strip()
    else:
        input_file = input("Enter the input file path: ").strip()

    # Remove quotes if user copied path with quotes
    input_file = input_file.strip('"\'')

    output_file = input("Enter the output file name (with extension): ")

    try:
        # Check if file exists
        if not os.path.exists(input_file):
            print(f"Error: The file '{input_file}' was not found.")
            return

        # Get file extension
        file_extension = os.path.splitext(input_file)[1].lower()

        # Read file based on extension
        if file_extension == ".pdf":
            if not PDF_AVAILABLE:
                print("Error: PDF support not available. Please install PyPDF2: pip install PyPDF2")
                return
            content = read_pdf_file(input_file)
            print("PDF file read successfully!")

        elif file_extension == ".csv":
            content = read_csv_file(input_file)
            print("CSV file read successfully!")

        elif file_extension == ".txt":
            content = read_txt_file(input_file)
            print("Text file read successfully!")

        else:
            print(f"Unsupported file format: {file_extension}")
            print("Supported formats: .txt, .csv, .pdf")
            return

        if not content.strip():
            print("Warning: The file appears to be empty or couldn't be read properly.")

        # Modify the content (convert to uppercase)
        modified_content = content.upper()

        # Add file info to output
        file_info = f"SOURCE FILE: {os.path.basename(input_file)}\n"
        file_info += f"FILE TYPE: {file_extension.upper()}\n"
        file_info += f"WORD COUNT: {len(content.split())}\n"
        file_info += "=" * 50 + "\n\n"

        final_content = file_info + modified_content

        # Write to output file
        with open(output_file, "w", encoding="utf-8") as outfile:
            outfile.write(final_content)

        print(f"Successfully processed '{os.path.basename(input_file)}'")
        print(f"Modified content saved to '{output_file}'")
        print(f"Word count: {len(content.split())}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_file}' or write to '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Add this to your existing code
if __name__ == "__main__":
    read_and_modify_file()
