# Example of using a while loop

# Initialize a counter variable
count = 0

# Define the condition for the loop to continue
# The loop will run as long as 'count' is less than 5
print("Starting the while loop...")
while count < 5:
    # Print the current value of the counter
    print(f"Current count: {count}")

    # Increment the counter
    count += 1 # This is equivalent to count = count + 1

# This line is executed after the loop condition is no longer true
print("While loop finished.")

print("\n--- Another while loop example ---")

# Example using a while loop with a break statement

# Initialize a variable
number = 10

# Loop indefinitely until a break condition is met
while True:
    print(f"Current number: {number}")

    # Check if the number is less than or equal to 0
    if number <= 0:
        # If the condition is met, exit the loop
        print("Number is 0 or less. Breaking the loop.")
        break # Exit the loop

    # Decrement the number
    number -= 2 # This is equivalent to number = number - 2

print("Loop after break finished.")

print("\n--- While loop with continue example ---")

# Example using a while loop with a continue statement

# Initialize a counter
i = 0

# Loop as long as i is less than 10
while i < 10:
    # Increment the counter first
    i += 1

    # Check if the number is odd
    if i % 2 != 0:
        # If the number is odd, skip the rest of the current iteration
        print(f"Skipping odd number: {i}")
        continue # Go to the next iteration of the loop

    # This line is only executed if the continue statement was not hit (i.e., the number is even)
    print(f"Processing even number: {i}")

print("Loop with continue finished.")
