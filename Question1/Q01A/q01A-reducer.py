import sys

# Creates the empty variables to use in the loop
old_store = None
old_amount = 0
store = None

# Loops between each line of the data coming in (standard input)
for line in sys.stdin:
    # Split each line and assigning them to each declared variable
    store, amount = line.split('\t', 1)

    # Converting the amount string into a float number, except when the string
    # does not represente a number
    try:
        amount = float(amount)
    except ValueError:
        continue

    # condition executes when the store for the first line has value None
    if old_store == None:
        old_store = store
        old_amount = amount
        continue
    # condition executes when the store for the past line its the same
    # as the store on the present line
    elif old_store == store:
        old_amount += amount
    # When the program arrives at a different store, it prints the 
    # store and accumulated amount and resets the variables.
    else:
        print(old_store, old_amount)
        old_store = store
        old_amount = amount

# Prints the last store
if old_store == store:
    print(old_store, old_amount)