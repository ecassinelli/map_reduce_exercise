import sys

# Creates the empty variables to use in the loop
counter_of_sales = 0
old_amount = 0
store = None

# Loops between each line of the data coming in
for line in sys.stdin:
    # Split each line and assigning them to each declared variable
    store, amount = line.split('\t', 1)

    # Converting the amoun string into a float number, except when the string
    # does not represente a number
    try:
        amount = float(amount)
    except ValueError:
        continue
    
    # Adds 1 to the counter of sales each time a line is read
    counter_of_sales += 1
    # Adds the amounts each time a line is read
    old_amount += amount

# Prints the number of sales and the total amount of sales
print('Number of Sales:', '{:,}'.format(counter_of_sales))
print('Total amount of Sales:', '${:,.2f}'.format(old_amount))