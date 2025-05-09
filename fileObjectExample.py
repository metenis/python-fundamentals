# Define the filename to be used
file_name = "example_renamed.txt"

# Create a file object in write mode using a context manager
with open(file_name, "w") as target_file:
    # Write content to the file
    target_file.write("This is an example file with renamed variables.\n")
    target_file.write("It has multiple lines.\n")
    target_file.write("And it's written using Python!")

# Create a file object in read mode using a context manager
with open(file_name, "r") as target_file:
    # Read the entire file contents
    file_contents = target_file.read()
    print("File contents:", file_contents)

# Create a file object in append mode using a context manager
with open(file_name, "a") as target_file:
    # Append a new line to the file
    target_file.write("\nThis is an appended line.")

# Create a file object in read mode again using a context manager
with open(file_name, "r") as target_file:
    # Read the entire file contents again
    file_contents_after_append = target_file.read()
    print("File contents after appending:", file_contents_after_append)

# Using the `readline()` method to read a single line
with open(file_name, "r") as target_file:
    # Read the first line
    single_line = target_file.readline()
    print("First line:", single_line.strip())

# Using the `readlines()` method to read all lines into a list
with open(file_name, "r") as target_file:
    # Read all lines
    list_of_lines = target_file.readlines()
    # Print lines, stripping whitespace
    print("All lines:", [line.strip() for line in list_of_lines])

# Using the `write()` method to overwrite the file with a single line
with open(file_name, "w") as target_file:
    target_file.write("This is a brand new line.\n")

# Using the `writelines()` method to overwrite the file with multiple lines from a list
with open(file_name, "w") as target_file:
    # List of strings to write as lines
    lines_to_write = ["This is line A.\n", "This is line B.\n", "This is line C.\n"]
    target_file.writelines(lines_to_write)

# Using the `seek()` method to move the file pointer and then read
# Using r+ mode for reading and writing
with open(file_name, "r+") as target_file:
    # Write a new line (this will overwrite from the beginning)
    target_file.write("Overwritten content.\n")
    # Move the file pointer back to the beginning (position 0)
    target_file.seek(0)
    # Read the entire content from the current pointer position
    content_after_seek = target_file.read()
    print("File contents after seeking:", content_after_seek)

# Using the `tell()` method to get the current file pointer position
# Using r+ mode for reading and writing
with open(file_name, "r+") as target_file:
    # Write some content
    target_file.write("Some text.")
    # Get the current position of the file pointer
    current_position = target_file.tell()
    print("Current file pointer position after writing 'Some text.':", current_position)

# Note: The file 'example_renamed.txt' will be created/modified in the same directory
# as the script when this code is executed.
