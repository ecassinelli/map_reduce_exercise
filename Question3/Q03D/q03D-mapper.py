import sys
import csv

# open the file coming from stdin with the csv reader module
# because is a .tsv file
forum_table = csv.reader(sys.stdin, delimiter='\t')
# skips the headers on the first line
next(forum_table)

for row in forum_table:
    # if each line matchs the table format
    if len(row) == 19:
        # Assigns the first column holding the id of the post
        # to a variable
        node_id = row[0]
        # Assigns the lenght of the post to a variable
        user_id = row[3]
        # Assigns the type of the post to a variable
        node_type = row[5]
        # Assigns the parent id of each post to a variable
        parent_id = row[6]

        # Condition executes depending on the type of the post
        if node_type == 'question':
            print(node_id + '\t' + user_id)
        elif node_type == 'answer':
            print(parent_id + '\t' + user_id)