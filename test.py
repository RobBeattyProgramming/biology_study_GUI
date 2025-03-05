import random
#from tkinter import *
import csv

fullQuestionList = []
rowOrder = 0
with open('question_list.csv', mode='r') as file:
    reader = csv.reader(file)
    for line in reader:
        fullQuestionList.append(line)


count = 0
randomNumberChosen = []

orderedQuestionDict = {}
randomizedQuestionDict = {}

while count < 4:
    randomNumber = random.randint(1, len(fullQuestionList) - 1) 
    if randomNumber in randomNumberChosen:
        continue
    randomNumberChosen.append(randomNumber)
    currentQuestion = fullQuestionList[randomNumber]

    orderedQuestionDict[currentQuestion[0]] = currentQuestion[1], currentQuestion[2], currentQuestion[3]

    questionPrompt = currentQuestion[0]
    currentQuestion.remove(currentQuestion[0])
    random.shuffle(currentQuestion)
    randomizedQuestionDict[questionPrompt] = currentQuestion

    count += 1

print(orderedQuestionDict)
print()
print(randomizedQuestionDict)








