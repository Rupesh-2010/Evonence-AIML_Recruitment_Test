# Data ValidationTask: Write a function validate_data(data)
# that checks if a list of dictionaries
# (e.g., [{"name": "Alice", "age": 30}, {"name": "Bob", "age": "25"}])
# contains valid integer values for the "age" key. Return a list of invalid entries.


def validate_data(data): #Created a Function for Finds records with invalid age.

    invalid_entries = []
    for entry in data:
        if "age" in entry:
            try:
                int(entry["age"])  # Check if it can be converted to int or it will give error.
            except (ValueError, TypeError): # Appare Error if Age exists but is not a valid number
                invalid_entries.append(entry)
        else:
            invalid_entries.append(entry)  # Missing "age" key is invalid
    return invalid_entries  # Return all invalid records found in the dataset

data = [{"name": "Alice", "age": 30}, {"name": "Bob", "age": "25"}, {"name": "Charlie"}]
# Given Example data to test the function

print(validate_data(data))  # Output: [{"name": "Bob", "age": "25"}, {"name": "Charlie"}]
# Should be pop-up Error for Bob (string age) & Charlie (missing age) as invalid.