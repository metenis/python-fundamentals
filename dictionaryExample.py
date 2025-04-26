# Create a dictionary called 'user_profile' with some initial key-value pairs
user_profile = {"name": "John", "age": 30, " occupation": "Software Engineer"}

# Print the entire dictionary
print("Original Dictionary:", user_profile)

# Access a specific value in the dictionary by its key
print("Name:", user_profile["name"])  # Output: John

# Add a new key-value pair to the dictionary
user_profile["city"] = "New York"
print("Updated Dictionary:", user_profile)

# Modify an existing value in the dictionary
user_profile["age"] = 31
print("Updated Dictionary:", user_profile)

# Remove a key-value pair from the dictionary
del user_profile["occupation"]
print("Updated Dictionary:", user_profile)

# Check if a key exists in the dictionary
if "name" in user_profile:
    print("Key 'name' exists in the dictionary")
else:
    print("Key 'name' does not exist in the dictionary")

# Get a list of all keys in the dictionary
profile_keys = list(user_profile.keys())
print("Keys:", profile_keys)

# Get a list of all values in the dictionary
profile_values = list(user_profile.values())
print("Values:", profile_values)

# Get a list of all key-value pairs in the dictionary
profile_items = list(user_profile.items())
print("Items:", profile_items)

# Create a new dictionary from an existing one using the dict() constructor
cloned_profile = dict(user_profile)
print("New Dictionary:", cloned_profile)

# Update a dictionary with new key-value pairs from another dictionary
additional_details = {"country": "USA", "hobbies": ["reading", "hiking"]}
user_profile.update(additional_details)
print("Updated Dictionary:", user_profile)

# Clear all key-value pairs from the dictionary
user_profile.clear()
print("Cleared Dictionary:", user_profile)