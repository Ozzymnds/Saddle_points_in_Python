# Without caching:

import random

# Input the number of columns
c = int(input("Enter the number of columns: "))
# Input the number of rows
f = int(input("Enter the number of rows: "))

# List with dimensions specified by c and f
matrix = []

# Generate a random matrix with values between 10 and 99
for row_num in range(f):
    current_row = []
    for col_num in range(c):
        value = random.randint(10, 99)
        current_row.append(value)
    matrix.append(current_row)

    # Display the current state of the matrix
    print(f"Rows: {f}, Columns: {c}")
    for row in matrix:
        print(row)

is_saddle_point = False

# Check for saddle points
for row in matrix:
    for index, value in enumerate(row):
        # Extract the current column for comparison
        column = [row[index] for row in matrix]
        max_in_column = max(column)
        min_in_column = min(column)

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
