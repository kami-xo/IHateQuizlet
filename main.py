#
# IMPORTS
#
import json
from quiz import run_quiz

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

def load_quiz(filepath):
    quiz_data = json.load(open(filepath))
    return quiz_data


####################################################################
#
#                  MAIN.PY PROGRAM BODY
#
####################################################################

quiz_data = load_quiz("quizzes/template.json")
run_quiz(quiz_data)












