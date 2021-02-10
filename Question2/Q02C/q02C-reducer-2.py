import sys

# Creates the empty variables to use in the loop
old_file = None
old_ocurrance = 0
file_name = None

# Loops between each line of the data coming in
for line in sys.stdin:
    # Split each line and assigning them to each declared variable
    file_name, ocurrances = line.split(' ', 1)

    # Converting the amoun string into a float number, except when the string
    # does not represente a number
    try:
        ocurrances = int(ocurrances)
    except ValueError:
        continue
    
    # condtion checks if the previous ocurrance is less than the current one
    # and replaces the variables
    if old_ocurrance <= ocurrances:
        old_file = file_name
        old_ocurrance = ocurrances
    else:
        continue

# Prints the file name with most ocurrances (most popular)
print(old_file, old_ocurrance)
