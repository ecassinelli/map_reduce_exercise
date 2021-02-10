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
        # Assigns the tag of the post to a variable
        tags = row[2].split()
        # Assigns the type of the post to a variable
        node_type = row[5]

        if node_type == 'question':
            for tag in tags:
                print(tag + '\t' + '1')
