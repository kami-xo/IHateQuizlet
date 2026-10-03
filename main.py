
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

answers = currentQuestion["incorrect"].copy() # answers now holds all the incorrect answers
answers.append(currentQuestion["correct"]) # APPEND adds the correct question into the same list as all the incorrect questions
random.shuffle(answers) # Shuffles all the random answers


# PRINTS OUT THE QUESTION IN LIST FORM
for index, answer in enumerate(answers):
    print(index + 1, answer)


################
#
# QUIZZING LOGIC. IT WILL ASK FOR A QUESTION AND THE USER WILL ENTER THEIR ANSWER
#
################

print(" ")
choice = int(input("What is the correct answer? "))
print("You chose: ", answers[choice - 1])

################
#
# SELECTION LOGIC. USER WILL THEN SEE IF WHAT THEY GOT WAS CORRECT.
#
################
if answers[choice - 1] == currentQuestion["correct"]:
    print("Correct!")
else:
    print("Incorrect!")




# print(questions[0]["question"]) # Prints the question #1






