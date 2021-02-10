import sys

# Creates the empty variables to use in the loop
old_node_id = None
users_list = []
current_node_id = None

# Loops between each line of the data coming in (standard input)
for line in sys.stdin:
    # Split each line and assigning them to each declared variable
    current_node_id, user_id = line.strip().split('\t', 1)

    # Condition executes when the old_node_id is different than the current one
    if old_node_id and old_node_id != current_node_id:
        print(old_node_id, users_list)
        # resets the user lists when arriving to a different node
        users_list = []

    old_node_id = current_node_id
    # appends the user_id to the empty list
    users_list.append(user_id)

# Prints the last current_node_id
if old_node_id != None:
    print(old_node_id, users_list)