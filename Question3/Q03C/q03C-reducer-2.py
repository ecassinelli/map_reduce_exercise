import sys

top_ten_dict = {}

# Loops between each line of the data coming in
for line in sys.stdin:
    # Split each line and assigning them to each declared variable
    tag, num_of_ocurrance = line.strip().split('\t', 1)

    # converts the num_of_ocurrances to an integer
    num_of_ocurrance = int(num_of_ocurrance)

    # Condition executes when the list has reached 10 elements
    if len(top_ten_dict) == 10:
        # creates a temporary top 10 list
        temp_top_ten = []
        # for loop to make and inverse top 10 list with the values first
        for key, value in top_ten_dict.items():
            temp_top_ten.append((value, key))

        # Gets the lowest element based on value
        lowest_ocurrance = min(temp_top_ten)

        # if the current num_of_ocurrances is bigger than the lowest, then:
        if num_of_ocurrance > lowest_ocurrance[0]:
            # delete the lowest ocurrance from the definitive top 10 list
            del top_ten_dict[lowest_ocurrance[1]]
            # add the current num_of_ocurrences to the definitive top 10 list
            top_ten_dict[tag] = num_of_ocurrance
    # if the definitive list has not reached 10 elements keep adding until that
    else:
        top_ten_dict[tag] = num_of_ocurrance

# sorts the top 10 list from greatest to lowest
sorted_top_ten = sorted(top_ten_dict.items(), key=lambda x: x[1], reverse=True)

# prints each tag and its value
for tag in sorted_top_ten:
    print(tag[0], tag[1])
