import sys

# Loops between each line of the data coming in
for line in sys.stdin:
    # Splits each line into a list
    row = line.split('\t')
    # Prints the third and fifht row with a tab space
    print(row[2] + '\t', row[4])