import sys

# Creates the empty variables to use in the loop
old_id = None
question_lenght = 0
answers_lenghts = []
current_id = None

# Loops between each row of the data coming in (standard input)
for row in sys.stdin:
    # Split each row and assigning them to each declared variable
    current_id, general_lenght, node_type = row.split()
    
    # Condition executes if the current_id is different than the old_id
    if old_id and old_id != current_id:
        # Condition executes when there are no answers
        if len(answers_lenghts) == 0:
            print(old_id + '\t' + str(question_lenght) + '\t' + str(len(answers_lenghts)))
        else:
            # Caluclates the average of the answers lenghts
            answers_average_lenght = float(sum(answers_lenghts))/len(answers_lenghts)
            print(old_id + '\t' + str(question_lenght) + '\t' + str(answers_average_lenght))

        # Resets the variables
        question_lenght = 0
        answers_lenghts = []
    
    # Condition executes to check if the type of the nod is question or answer
    # and assigns the variables accordingly
    if node_type == 'question':
        question_lenght = int(general_lenght)
    elif node_type == 'answer':
        answers_lenghts.append(int(general_lenght))

    old_id = current_id

# Prints the last id
if old_id != None:
    if len(answers_lenghts) == 0:
        print(old_id + '\t' + str(question_lenght) + '\t' + str(len(answers_lenghts)))
    else:
        answers_average_lenght = float(sum(answers_lenghts))/len(answers_lenghts)
        print(old_id + '\t' + str(question_lenght) + '\t' + str(answers_average_lenght))

