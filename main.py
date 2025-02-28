import random
from tkinter import *
import csv

questionDict = {}
rowOrder = 0
with open('question_list.csv', mode='r') as file:
    reader = csv.reader(file)
    for line in reader:
        questionDict[rowOrder] = line
        rowOrder += 1

count = 0
questionsChosen = []
questionList = []
randomNumberChosen = []
orderedQuestionList = []

while count < 5:

    randomNumber = random.randint(1,6) #needs length of dict
    if randomNumber in randomNumberChosen:
        continue
    randomNumberChosen.append(randomNumber)

    orderedQuestionList.append(questionDict[randomNumber])
    preshuffledList = questionDict[randomNumber]
    questionPrompt = preshuffledList[0]
    preshuffledList.remove(questionPrompt)
    random.shuffle(preshuffledList)
    preshuffledList.insert(0, questionPrompt)

    questionsChosen.append(preshuffledList)
    questionList.append(questionsChosen[count])

    questionCount = 1
    questionCountList = []
    while questionCount < 4:
        randomCountNumber = random.randint(1, 3)
        if randomCountNumber in questionCountList:
            continue
        questionCountList.append(randomCountNumber)

        questionCount += 1
    count += 1


def get_values():
    questionOneList = orderedQuestionList[0]
    questionTwoList = orderedQuestionList[1]
    questionThreeList = orderedQuestionList[2]
    questionFourList = orderedQuestionList[3]

    if qOneAOne.get() == 1:
        if questionOneAnswerOneValue == questionOneList[1]:
            questionOneSpaceTop.config(text="YES")
    elif qOneATwo.get() == 1:
        if questionOneAnswerTwoValue == questionOneList[1]:
            questionOneSpaceTop.config(text="YES")
    elif qOneAThree.get() == 1:
        if questionOneAnswerThreeValue == questionOneList[1]:
            questionOneSpaceTop.config(text="YES")

    if qTwoAOne.get() == 1:
        if questionTwoAnswerOneValue == questionTwoList[1]:
            questionTwoSpaceTop.config(text="YES")
    elif qTwoATwo.get() == 1:
        if questionTwoAnswerTwoValue == questionTwoList[1]:
            questionTwoSpaceTop.config(text="YES")
    elif qTwoAThree.get() == 1:
        if questionTwoAnswerThreeValue == questionTwoList[1]:
            questionTwoSpaceTop.config(text="YES")

    if qThreeAOne.get() == 1:
        if questionThreeAnswerOneValue == questionThreeList[1]:
            questionThreeSpaceTop.config(text="YES")
    elif qThreeATwo.get() == 1:
        if questionThreeAnswerTwoValue == questionThreeList[1]:
            questionThreeSpaceTop.config(text="YES")
    elif qThreeAThree.get() == 1:
        if questionThreeAnswerThreeValue == questionThreeList[1]:
            questionThreeSpaceTop.config(text="YES")

    if qFourAOne.get() == 1:
        if questionFourAnswerOneValue == questionFourList[1]:
            questionFourSpaceTop.config(text="YES")
    elif qFourATwo.get() == 1:
        if questionFourAnswerTwoValue == questionFourList[1]:
            questionFourSpaceTop.config(text="YES")
    elif qFourAThree.get() == 1:
        if questionFourAnswerThreeValue == questionFourList[1]:
            questionFourSpaceTop.config(text="YES")

root = Tk()

root.title("Biology Beginner Questions")
root.geometry('400x800')


questionOneInfo = questionList[0]
questionOneLabel = Label(root, text = questionOneInfo[0])
questionOneLabel.grid(column = 0, row = 0)

qOneAOne = IntVar()
qOneATwo = IntVar()
qOneAThree = IntVar()

questionOneAnswerOne = Checkbutton(root, text = questionOneInfo[1], variable=qOneAOne, onvalue=1, offvalue=0) 
questionOneAnswerOne.grid(column = 0, row = 1)
questionOneAnswerOneValue = questionOneInfo[1]
questionOneAnswerTwo = Checkbutton(root, text = questionOneInfo[2], variable=qOneATwo)
questionOneAnswerTwo.grid(column = 0, row = 2)
questionOneAnswerTwoValue = questionOneInfo[2]
questionOneAnswerThree = Checkbutton(root, text = questionOneInfo[3], variable=qOneAThree)
questionOneAnswerThree.grid(column = 0, row = 3)
questionOneAnswerThreeValue = questionOneInfo[3]

questionOneSpaceTop = Label(root, text = "")
questionOneSpaceTop.grid(column=0,row=4)
questionOneSpaceBottom = Label(root, text = "")
questionOneSpaceBottom.grid(column=0,row=5)


questionTwoInfo = questionList[1]
questionTwoLabel = Label(root, text = questionTwoInfo[0])
questionTwoLabel.grid(column = 0, row = 6)

qTwoAOne = IntVar()
qTwoATwo = IntVar()
qTwoAThree = IntVar()

questionTwoAnswerOne = Checkbutton(root, text = questionTwoInfo[1], variable=qTwoAOne)
questionTwoAnswerOne.grid(column = 0, row = 7)
questionTwoAnswerOneValue = questionTwoInfo[1]
questionTwoAnswerTwo = Checkbutton(root, text = questionTwoInfo[2], variable=qTwoATwo)
questionTwoAnswerTwo.grid(column = 0, row = 8)
questionTwoAnswerTwoValue = questionTwoInfo[2]
questionTwoAnswerThree = Checkbutton(root, text = questionTwoInfo[3], variable=qTwoAThree)
questionTwoAnswerThree.grid(column = 0, row = 9)
questionTwoAnswerThreeValue = questionTwoInfo[3]

questionTwoSpaceTop = Label(root, text = "")
questionTwoSpaceTop.grid(column=0,row=10)
questionTwoSpaceBottom = Label(root, text = "")
questionTwoSpaceBottom.grid(column=0,row=11)


questionThreeInfo = questionList[2]
questionThreeLabel = Label(root, text = questionThreeInfo[0])
questionThreeLabel.grid(column=0,row=12)

qThreeAOne = IntVar()
qThreeATwo = IntVar()
qThreeAThree = IntVar()

questionThreeAnswerOne = Checkbutton(root, text = questionThreeInfo[1], variable=qThreeAOne)
questionThreeAnswerOne.grid(column = 0, row = 13)
questionThreeAnswerOneValue = questionThreeInfo[1]
questionThreeAnswerTwo = Checkbutton(root, text = questionThreeInfo[2], variable=qThreeATwo)
questionThreeAnswerTwo.grid(column = 0, row = 14)
questionThreeAnswerTwoValue = questionThreeInfo[2]
questionThreeAnswerThree = Checkbutton(root, text = questionThreeInfo[3], variable=qThreeAThree)
questionThreeAnswerThree.grid(column = 0, row = 15)
questionThreeAnswerThreeValue = questionThreeInfo[3]

questionThreeSpaceTop = Label(root, text = "")
questionThreeSpaceTop.grid(column=0,row=16)
questionThreeSpaceBottom = Label(root, text = "")
questionThreeSpaceBottom.grid(column=0,row=17)


questionFourInfo = questionList[3]
questionFourLabel = Label(root, text = questionFourInfo[0])
questionFourLabel.grid(column=0,row=18)

qFourAOne = IntVar()
qFourATwo = IntVar()
qFourAThree = IntVar()

questionFourAnswerOne = Checkbutton(root, text = questionFourInfo[1], variable=qFourAOne)
questionFourAnswerOne.grid(column = 0, row = 19)
questionFourAnswerOneValue = questionFourInfo[1]
questionFourAnswerTwo = Checkbutton(root, text = questionFourInfo[2], variable=qFourATwo)
questionFourAnswerTwo.grid(column = 0, row = 20)
questionFourAnswerTwoValue = questionFourInfo[2]
questionFourAnswerThree = Checkbutton(root, text = questionFourInfo[3], variable=qFourAThree)
questionFourAnswerThree.grid(column = 0, row = 21)
questionFourAnswerThreeValue = questionFourInfo[3]

questionFourSpaceTop = Label(root, text = "")
questionFourSpaceTop.grid(column=0,row=22)
questionFourSpaceBottom = Label(root, text = "")
questionFourSpaceBottom.grid(column=0,row=23)

submitButton = Button(root, text = "Submit", command=get_values)
submitButton.grid(column=0,row=25)






# questions are answered and list from dictionary is used to determine answers
