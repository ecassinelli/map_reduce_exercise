import sys

old_tag = None
old_count = 0
current_tag = None

for line in sys.stdin:
    line = line.strip()
    current_tag, count = line.split('\t', 1)

    # Converting the count string into a int number, except when the string
    # does not represente a number
    try:
        count = int(count)
    except ValueError:
        continue

    # condition executes when the tag for the first line has value None
    if old_tag == None:
        old_tag = current_tag
        old_count = count
        continue
    # condition executes when the tag for the past line is the same
    # as the tag on the present line
    elif old_tag == current_tag:
        old_count += count
    # When the program arrives at a different tag, it prints the 
    # tag and accumulated count and resets the variables.
    else:
        print(old_tag + '\t' + str(old_count))
        old_tag = current_tag
        old_count = count

# Prints the last tag
print(old_tag + '\t' + str(old_count))
