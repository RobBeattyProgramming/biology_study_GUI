import random
from tkinter import *
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
promptList = []

while count < 4:
    randomNumber = random.randint(0, len(fullQuestionList) - 1) 
    if randomNumber in randomNumberChosen:
        continue
    randomNumberChosen.append(randomNumber)
    currentQuestion = fullQuestionList[randomNumber]

    orderedQuestionDict[currentQuestion[0]] = currentQuestion[1], currentQuestion[2], currentQuestion[3]
    promptList.append(currentQuestion[0])

    questionPrompt = currentQuestion[0]
    currentQuestion.remove(currentQuestion[0])
    random.shuffle(currentQuestion)
    randomizedQuestionDict[questionPrompt] = currentQuestion

    count += 1

def check_values(answer, correctList):
    if answer == correctList[0]:
        return "correct"
    else:
        return "incorrect"

def get_values():
    questionOneList = orderedQuestionDict[promptList[0]] 
    questionTwoList = orderedQuestionDict[promptList[1]] 
    questionThreeList = orderedQuestionDict[promptList[2]] 
    questionFourList = orderedQuestionDict[promptList[3]] 

    if qOneAOne.get() == 1:
        questionOneSpaceTop.config(text= check_values(questionOneAnswerOneValue, questionOneList))
    elif qOneATwo.get() == 1:
       questionOneSpaceTop.config(text= check_values(questionOneAnswerTwoValue, questionOneList))
    elif qOneAThree.get() == 1:
        questionOneSpaceTop.config(text= check_values(questionOneAnswerThreeValue, questionOneList))

    if qTwoAOne.get() == 1:
        questionTwoSpaceTop.config(text=check_values(questionTwoAnswerOneValue, questionTwoList))
    elif qTwoATwo.get() == 1:
        questionTwoSpaceTop.config(text=check_values(questionTwoAnswerTwoValue, questionTwoList))
    elif qTwoAThree.get() == 1:
        questionTwoSpaceTop.config(text=check_values(questionTwoAnswerThreeValue, questionTwoList))

    if qThreeAOne.get() == 1:
        questionThreeSpaceTop.config(text=check_values(questionThreeAnswerOneValue, questionThreeList))
    elif qThreeATwo.get() == 1:
        questionThreeSpaceTop.config(text=check_values(questionThreeAnswerTwoValue, questionThreeList))
    elif qThreeAThree.get() == 1:
        questionThreeSpaceTop.config(text=check_values(questionThreeAnswerThreeValue, questionThreeList))

    if qFourAOne.get() == 1:
        questionFourSpaceTop.config(text=check_values(questionFourAnswerOneValue, questionFourList))
    elif qFourATwo.get() == 1:
        questionFourSpaceTop.config(text=check_values(questionFourAnswerTwoValue, questionFourList))
    elif qFourAThree.get() == 1:
        questionFourSpaceTop.config(text=check_values(questionFourAnswerThreeValue, questionFourList))

root = Tk()

root.title("Biology Beginner Questions")
root.geometry('800x620')
root.config(bg = "skyblue")


questionOneInfo = randomizedQuestionDict[promptList[0]]
questionOneLabel = Label(root, text = promptList[0], bg = "goldenrod", font=("Arial", 18))
questionOneLabel.grid(column = 0, row = 0)

qOneAOne = IntVar()
qOneATwo = IntVar()
qOneAThree = IntVar()

questionOneAnswerOne = Checkbutton(root, text = questionOneInfo[0], variable=qOneAOne, onvalue=1, offvalue=0, bg = "skyblue", font=("Arial", 15)) 
questionOneAnswerOne.grid(column = 0, row = 1)
questionOneAnswerOneValue = questionOneInfo[0] 
questionOneAnswerTwo = Checkbutton(root, text = questionOneInfo[1], variable=qOneATwo, onvalue=1, offvalue=0, bg = "skyblue", font=("Arial", 15))
questionOneAnswerTwo.grid(column = 0, row = 2)
questionOneAnswerTwoValue = questionOneInfo[1]
questionOneAnswerThree = Checkbutton(root, text = questionOneInfo[2], variable=qOneAThree, onvalue=1, offvalue=0, bg = "skyblue", font=("Arial", 15))
questionOneAnswerThree.grid(column = 0, row = 3)
questionOneAnswerThreeValue = questionOneInfo[2]

questionOneSpaceTop = Label(root, text = "", bg = "skyblue")
questionOneSpaceTop.grid(column=0,row=4)
questionOneSpaceBottom = Label(root, text = "", bg = "skyblue")
questionOneSpaceBottom.grid(column=0,row=5)


questionTwoInfo = randomizedQuestionDict[promptList[1]]
questionTwoLabel = Label(root, text = promptList[1], bg = "goldenrod", font=("Arial", 18))
questionTwoLabel.grid(column = 0, row = 6)

qTwoAOne = IntVar()
qTwoATwo = IntVar()
qTwoAThree = IntVar()

questionTwoAnswerOne = Checkbutton(root, text = questionTwoInfo[0], variable=qTwoAOne, bg = "skyblue", font=("Arial", 15))
questionTwoAnswerOne.grid(column = 0, row = 7)
questionTwoAnswerOneValue = questionTwoInfo[0]
questionTwoAnswerTwo = Checkbutton(root, text = questionTwoInfo[1], variable=qTwoATwo, bg = "skyblue", font=("Arial", 15))
questionTwoAnswerTwo.grid(column = 0, row = 8)
questionTwoAnswerTwoValue = questionTwoInfo[1]
questionTwoAnswerThree = Checkbutton(root, text = questionTwoInfo[2], variable=qTwoAThree, bg = "skyblue", font=("Arial", 15))
questionTwoAnswerThree.grid(column = 0, row = 9)
questionTwoAnswerThreeValue = questionTwoInfo[2]

questionTwoSpaceTop = Label(root, text = "", bg = "skyblue")
questionTwoSpaceTop.grid(column=0,row=10)
questionTwoSpaceBottom = Label(root, text = "", bg = "skyblue")
questionTwoSpaceBottom.grid(column=0,row=11)


questionThreeInfo = randomizedQuestionDict[promptList[2]]
questionThreeLabel = Label(root, text = promptList[2], bg = "goldenrod", font=("Arial", 18))
questionThreeLabel.grid(column=0,row=12)

qThreeAOne = IntVar()
qThreeATwo = IntVar()
qThreeAThree = IntVar()

questionThreeAnswerOne = Checkbutton(root, text = questionThreeInfo[0], variable=qThreeAOne, bg = "skyblue", font=("Arial", 15))
questionThreeAnswerOne.grid(column = 0, row = 13)
questionThreeAnswerOneValue = questionThreeInfo[0]
questionThreeAnswerTwo = Checkbutton(root, text = questionThreeInfo[1], variable=qThreeATwo, bg = "skyblue", font=("Arial", 15))
questionThreeAnswerTwo.grid(column = 0, row = 14)
questionThreeAnswerTwoValue = questionThreeInfo[1]
questionThreeAnswerThree = Checkbutton(root, text = questionThreeInfo[2], variable=qThreeAThree, bg = "skyblue", font=("Arial", 15))
questionThreeAnswerThree.grid(column = 0, row = 15)
questionThreeAnswerThreeValue = questionThreeInfo[2]

questionThreeSpaceTop = Label(root, text = "", bg = "skyblue")
questionThreeSpaceTop.grid(column=0,row=16)
questionThreeSpaceBottom = Label(root, text = "", bg = "skyblue")
questionThreeSpaceBottom.grid(column=0,row=17)


questionFourInfo = randomizedQuestionDict[promptList[3]]
questionFourLabel = Label(root, text = promptList[3], bg="goldenrod", font=("Arial", 18))
questionFourLabel.grid(column=0,row=18)

qFourAOne = IntVar()
qFourATwo = IntVar()
qFourAThree = IntVar()

questionFourAnswerOne = Checkbutton(root, text = questionFourInfo[0], variable=qFourAOne, bg = "skyblue", font=("Arial", 15))
questionFourAnswerOne.grid(column = 0, row = 19)
questionFourAnswerOneValue = questionFourInfo[0]
questionFourAnswerTwo = Checkbutton(root, text = questionFourInfo[1], variable=qFourATwo, bg = "skyblue", font=("Arial", 15))
questionFourAnswerTwo.grid(column = 0, row = 20)
questionFourAnswerTwoValue = questionFourInfo[1]
questionFourAnswerThree = Checkbutton(root, text = questionFourInfo[2], variable=qFourAThree, bg = "skyblue", font=("Arial", 15))
questionFourAnswerThree.grid(column = 0, row = 21)
questionFourAnswerThreeValue = questionFourInfo[2]

questionFourSpaceTop = Label(root, text = "", bg = "skyblue")
questionFourSpaceTop.grid(column=0,row=22)
questionFourSpaceBottom = Label(root, text = "", bg = "skyblue")
questionFourSpaceBottom.grid(column=0,row=23)

submitButton = Button(root, text = "Submit", command=get_values, bg="skyblue")
submitButton.grid(column=0,row=25)

