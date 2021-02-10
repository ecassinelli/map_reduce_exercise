import sys

# Creates the empty variables to use in the loop
old_category = None
old_amount = 0
category = None

# Loops between each line of the data coming in (standard input)
for line in sys.stdin:
    # Split each line and assigning them to each declared variable
    category, amount = line.split('\t', 1)

    # Converting the amount string into a float number, except when the string
    # does not represente a number
    try:
        amount = float(amount)
    except ValueError:
        continue
    
    # Condition executes when starting with the first line assigns
    # the splited values to the "old" variables and continues
    if old_category == None:
        old_category = category
        old_amount = amount
        continue
    # condition executes when the category for the past line its the same
    # as the category on the present line
    elif old_category == category:
        old_amount += amount
    # When the program arrives at a different category, it prints the 
    # category and accumulated amount and resets the variables.
    else:
        print(old_category, old_amount)
        old_category = category
        old_amount = amount
        
# Prints the last category
if old_category == category:
    print(old_category, old_amount)
