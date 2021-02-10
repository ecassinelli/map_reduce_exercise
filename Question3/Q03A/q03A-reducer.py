import sys

# Creates the empty variables to use in the loop
old_id = None
# creates a list of 24 post counters for each hour of the day
hour_counter = [0]*24
current_id = None

# loops between each row of the data coming in (standard input)
for row in sys.stdin:
    # splits each row and assigns it to each declared variable
    current_id, hour_post = row.split('\t', 1)

    # Converting the hours string into a int number, except when the string
    # does not represente a number
    try:
        hour_post = int(hour_post)
    except ValueError:
        continue
    
    # Condition executes only when the current id is different from the previous id
    if old_id and old_id != current_id:
        # Finds the max number of post in the list hour_counter and assigns it 
        # to a variable.
        max_counts = max(hour_counter)
        # Creates a counter for positioning on each hour
        hour_position = 0

        # Loop iterates for each counter of each hour in the list
        for hour_count in hour_counter:
            # Condition checks if the element is equal to the maximum
            # number of posts
            if hour_count == max_counts:
                # Prints the id and the hour where most posts are  made
                print(old_id + '\t' + str(hour_position))
            # Counter goes to the next hour
            hour_position += 1

        # resets the list of post counters
        hour_counter = [0]*24

    # Assigns current id to previous id
    old_id = current_id
    # Increases the count in the specified hour.
    hour_counter[hour_post] += 1

# Condition executes for the last id
if old_id != None:
    # Same process as before
    max_counts = max(hour_counter)
    hour_position = 0
    for hour_count in hour_counter:
        if hour_count == max_counts:
            print(old_id + '\t' + str(hour_position))
        hour_position += 1



