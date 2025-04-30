# Create a tuple
initial_tuple = (1, 2, 3, 4, 5)

# Print the tuple
print("Original Tuple:", initial_tuple)

# Convert the tuple to a list using the list() function
converted_list = list(initial_tuple)

# Print the list
print("Converted to List:", converted_list)

# Convert the list back to a tuple using the tuple() function
reconverted_tuple = tuple(converted_list)

# Print the tuple again
print("Converted back to Tuple:", reconverted_tuple)

# Verify that the original tuple and the converted tuple are the same
print("Are the original and converted tuples the same?", initial_tuple == reconverted_tuple)

# Create a list
initial_list = [1, 2, 3, 4, 5]

# Print the list
print("Original List:", initial_list)

# Convert the list to a tuple using the tuple() function
converted_tuple_from_list = tuple(initial_list)

# Print the tuple
print("Converted to Tuple:", converted_tuple_from_list)

# Convert the tuple back to a list using the list() function
reconverted_list_from_tuple = list(converted_tuple_from_list)

# Print the list again
print("Converted back to List:", reconverted_list_from_tuple)

# Verify that the original list and the converted list are the same
print("Are the original and converted lists the same?", initial_list == reconverted_list_from_tuple)
