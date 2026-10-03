
import json
import random

# CODE


print('Initiated.')
print('')


# Open quizzes logic.
quiz_file = open("quizzes/template.json")
quiz_data = json.load(quiz_file)


# Question Answer Logic
print(quiz_data["name"]) # Name of the quiz
print("-------------------------------------------------------")
questions = quiz_data["questions"]  # Variable for question

currentQuestion = random.choice(questions) # sets currentQuestion variable to a random choice of questions in the pool
print(currentQuestion["question"]) # Prints the current question that is randomly chosen

answers = currentQuestion["incorrect"].copy() # answers now holds all the incorrect questions
answers.append(currentQuestion["correct"]) # APPEND adds the correct question into the same list as all the incorrect questions
print(answers)

# print(questions[0]["question"]) # Prints the question #1






