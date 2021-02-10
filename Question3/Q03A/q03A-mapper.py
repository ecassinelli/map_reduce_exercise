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
        # assigns the value of the id in the thrid column
        # to the variable author_id
        author_id = row[3]
        # assigns the date and the time in the eight column
        # to the variable date_time
        date_time = row[8]
        # splits the value of date_time
        date, time = date_time.strip().split(' ')
        # splits the time into hour, minute and seconds
        hour, minute, second = time.split(':')
        # prints the author_id and the hour that corresponds
        print(author_id + '\t' + hour)

