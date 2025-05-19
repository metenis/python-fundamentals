# Define a variable to hold an assessment score
assessment_score = 85

# Print the original assessment score
print("Assessment Score:", assessment_score)

# Use if, elif, and else to determine the letter grade based on the assessment score
if assessment_score >= 90:
    # If the score is 90 or above, assign an 'A' grade
    letter_grade = 'A'
elif assessment_score >= 80:
    # If the score is between 80 and 89, assign a 'B' grade
    letter_grade = 'B'
elif assessment_score >= 70:
    # If the score is between 70 and 79, assign a 'C' grade
    letter_grade = 'C'
elif assessment_score >= 60:
    # If the score is between 60 and 69, assign a 'D' grade
    letter_grade = 'D'
else:
    # If the score is below 60, assign an 'F' grade
    letter_grade = 'F'

# Print the determined letter grade
print("Letter Grade:", letter_grade)

# Example of using if-else for a simple condition
has_passed = assessment_score >= 60  # Determine if the assessment score is passing

# Print whether the student has passed or failed
if has_passed:
    print("Status: Passed")
else:
    print("Status: Failed")

# Another example with multiple conditions
current_temperature = 30  # Define a temperature variable

# Print the temperature
print("Current Temperature:", current_temperature)

# Determine the weather condition based on the temperature
if current_temperature > 30:
    weather_condition = "Hot"
elif current_temperature >= 20:
    weather_condition = "Warm"
elif current_temperature >= 10:
    weather_condition = "Cool"
else:
    weather_condition = "Cold"

# Print the determined weather condition
print("Weather condition:", weather_condition)
