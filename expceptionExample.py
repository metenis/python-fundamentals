# Example of handling exceptions with try and except

# Define a function to divide two numbers
def safe_divide(numerator, denominator):
    """Return the result of dividing numerator by denominator, handling errors."""
    try:
        # Attempt to perform the division
        division_result = numerator / denominator
    except ZeroDivisionError:  # Handle division by zero
        # Return an error message for division by zero
        return "Error: Cannot divide by zero."
    except TypeError:  # Handle incorrect types
        # Return an error message for invalid input types
        return "Error: Invalid input types. Please provide numbers."
    else:
        # Return the result if no exceptions occurred
        return division_result

# Call the safe_divide function with valid inputs
print("10 divided by 2:", safe_divide(10, 2))

# Call the safe_divide function with a zero denominator
print("10 divided by 0:", safe_divide(10, 0))

# Call the safe_divide function with invalid input types
print("10 divided by 'a':", safe_divide(10, 'a'))

# Example of using finally
def safe_read_file(input_file_path):
    """Read the contents of a file and return them, handling file not found."""
    opened_file = None # Initialize file variable outside try
    try:
        # Attempt to open the file
        opened_file = open(input_file_path, 'r')
        # Read the file content
        file_content = opened_file.read()
        # Return the content
        return file_content
    except FileNotFoundError:  # Handle file not found error
        # Return an error message
        return "Error: File not found."
    finally:
        # This block will execute regardless of whether an exception occurred
        # Ensure the file is closed if it was opened
        if opened_file:
            opened_file.close()
        # Indicate completion
        print("Execution of safe_read_file completed.")

# Call the safe_read_file function with a non-existent file
print(safe_read_file("non_existent_file.txt"))

# Call the safe_read_file function with an existing file (ensure the file exists)
# print(safe_read_file("existing_file.txt"))  # Uncomment to test with an actual file
