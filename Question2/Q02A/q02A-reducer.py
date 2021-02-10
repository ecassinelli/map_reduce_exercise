import sys

# Creates the empty variables to use in the loop
old_file = None
old_count = 0
file_name = None

# Loops between each line of the data coming in (standard input)
for line in sys.stdin:
    # Split each line and assigning them to each declared variable
    file_name, count = line.split('\t', 1)

    # Converting the count string into a int number, except when the string
    # does not represente a number
    try:
        count = int(count)
    except ValueError:
        continue

    # condition executes when the file for the first line has value None
    if old_file == None:
        old_file = file_name
        old_count = count
        continue
    # condition executes when the file for the past line is the same
    # as the file on the present line
    elif old_file == file_name:
        old_count += count
    # When the program arrives at a different file, it prints the 
    # file and accumulated count and resets the variables.
    else:
        print(old_file, old_count)
        old_file = file_name
        old_count = count

# Prints the last file_name
if old_file == file_name:
    print(old_file, old_count)