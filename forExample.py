# Define a list of numbers
numeric_list = [1, 2, 3, 4, 5]

# Print the original list
print("Original list:", numeric_list)

# Use a for loop to iterate over the list
for current_number in numeric_list:
    # Print each number in the list
    print("Number:", current_number)

# Example of using a for loop with a string
input_string = "Hello, World!"

# Print the original message
print("Original message:", input_string)

# Use a for loop to iterate over the characters in the string
for current_character in input_string:
    # Print each character in the string
    print("Character:", current_character)

# Example of using a for loop with a dictionary
user_profile = {"name": "John", "age": 30, "city": "New York"}

# Print the original dictionary
print("Original dictionary:", user_profile)

# Use a for loop to iterate over the key-value pairs in the dictionary
for profile_key, profile_value in user_profile.items():
    # Print each key-value pair in the dictionary
    print(f"{profile_key}: {profile_value}")

# Example of using a for loop with a range
for loop_counter in range(1, 6):
    # Print each number in the range
    print("Number:", loop_counter)

# Example of using a for loop with enumerate
fruit_list = ["apple", "banana", "cherry"]

# Use a for loop with enumerate to iterate over the list with indices
for item_index, current_fruit in enumerate(fruit_list):
    # Print each fruit with its index
    print(f"Fruit at index {item_index}: {current_fruit}")

# Example of using a for loop with zip
list_of_names = ["John", "Mary", "David"]
list_of_ages = [25, 31, 42]

# Use a for loop with zip to iterate over two lists simultaneously
for current_name, current_age in zip(list_of_names, list_of_ages):
    # Print each name with its corresponding age
    print(f"{current_name} is {current_age} years old.")
