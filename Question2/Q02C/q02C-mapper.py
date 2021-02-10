import sys

# Loops between each line of the data coming in
for line in sys.stdin:
    # Splits each line into a list
    row = line.split()
    # Evaluates if each line has all the elements
    if len(row) == 10:
        # prints the file path with a tab espace and the number 1
        print(row[6] + '\t' + '1')