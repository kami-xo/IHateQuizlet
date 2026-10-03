#
# IMPORTS
#
import json
import random

#
# INITIATION PHASE
#


print('Initiated.')
print('')


# Open quizzes logic.
quiz_file = open("quizzes/template.json")
quiz_data = json.load(quiz_file)


##################################
#
# QUESTION STRUCTURE
#
##################################

print(quiz_data["name"]) # Name of the quiz
print("-------------------------------------------------------")

questions = quiz_data["questions"]  # Variable for question

#
# START OF WHILE LOOP, LOOPS THROUGH QUESTIONS ONE BY ONE
#

while len(questions) > 0:

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
    print ("Unsure? Press enter to skip.")
    choice = input("What is the correct answer? ")
    if choice.isdigit():
        choice = int(choice)
        if len(answers) >= choice > 0:
            selectedAnswer = answers[choice - 1]
    else:
        # Not sure logic
    print("You chose: ", selectedAnswer)

################
#
# SELECTION LOGIC. USER WILL THEN SEE IF WHAT THEY GOT WAS CORRECT.
#
################
    if selectedAnswer == currentQuestion["correct"]:
        print("Correct!")
        questions.remove(currentQuestion)
    else:
        print("Incorrect!")

############
#
# END OF WHILE LOOP
#
############

print("Quizzing Complete!")




# print(questions[0]["question"]) # Prints the question #1






