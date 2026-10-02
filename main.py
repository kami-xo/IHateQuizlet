# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import json
import random

# CODE


print('Initiated.')
print('')


# Open quizzes logic.
quiz_file = open("quizzes/template.json")
quiz_data = json.load(quiz_file)

print(quiz_data["name"])

questions = quiz_data["questions"]

print(questions[0]["question"])




