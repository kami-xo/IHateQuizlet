#
# IMPORTS
#
import json
from quiz import run_quiz
from pathlib import Path

#
# INITIATION PHASE
#

print('Initiated.')
print('')

####################################################################
#
#                  QUIZ LOADING LOGIC
#
####################################################################


# SEARCHES FOR ALL FILES IN /quizzes AND LOADS
quizDirectory = Path('quizzes')
quizDirectory.glob('*.json')

def load_quiz(filepath):
    quiz_data = json.load(open(filepath))
    return quiz_data


####################################################################
#
#                  MAIN.PY PROGRAM BODY
#
####################################################################


print("Please select a quiz below:")
print("")

for file in quizDirectory.glob('*.json'):
    print(file)



# quiz_data = load_quiz("quizzes/template.json")
# run_quiz(quiz_data)












