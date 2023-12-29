# With caching:

import random

# Input the number of columns and rows
c = int(input("Enter the number of columns: "))
f = int(input("Enter the number of rows: "))

# Generate a random matrix with values between 10 and 99
matrix = []
for row in range(f):
    current_row = []
    for column in range(c):
        value = random.randint(10, 99)
        current_row.append(value)
    matrix.append(current_row)

"""
Example matrix:
matrix = [
    [1, 1],
    [1, 1],
]
"""

# Display the matrix dimensions and content
print(f"Rows: {f}, Columns: {c}")
for row in matrix:
    print(row)

# Initialize a cache for columns
cache_columns = {}
is_saddle_point = False

# Check for saddle points
for row in matrix:
    for index, value in enumerate(row):
        # Check if the column data is already cached
        if index in cache_columns.keys():
            max_in_column = max(cache_columns[index])
            min_in_column = min(cache_columns[index])
        else:
            # Cache the column data if not already cached
            column_data = [row[index] for row in matrix]
            cache_columns[index] = column_data
            max_in_column = max(column_data)
            min_in_column = min(column_data)

        # Find the maximum and minimum values in the current row
        max_in_row = max(row)
        min_in_row = min(row)

        # Check if the current value is a saddle point
        if value <= min_in_row and value >= max_in_column:
            is_saddle_point = True
        elif value >= max_in_row and value <= min_in_column:
            is_saddle_point = True

        # Break the loop if a saddle point is found
        if is_saddle_point is True:
            break

    # Break the loop if a saddle point is found
    if is_saddle_point is True:
        print(f"Saddle Point Found: {value}")
        break

# Display a message if no saddle point is found
if is_saddle_point is False:
    print("No Saddle Point Found")
