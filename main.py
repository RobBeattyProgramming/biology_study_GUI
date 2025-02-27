import random
from tkinter import *

testDict = {
    1 : ["What is One plus One?", 2, 1, 3],
    2: ["How much cheese?", "none", 8, "all"],
    3: ["Say three?", "three", " fsjldivc", "one"],
    4: ["SAY HEY?", "hey", "ho", "heave"],
    5: ["Joshua?", "JOSHUA", "JOSHUAAAA", "jeesh"],
    6: ["How many blimps?", 5, 6, 7]
}

# random questions are generated on time of loading the program
count = 0
questionsChosen = []
questionList = []
randomNumberChosen = []

while count < 5:

    randomNumber = random.randint(1,6)
    if randomNumber in randomNumberChosen:
        continue
    randomNumberChosen.append(randomNumber)

    questionsChosen.append(testDict[randomNumber])
    questionList.append(questionsChosen[count])
    #label = Label(root, text = questionList[0])
    #label.grid()

    questionCount = 1
    questionCountList = []
    while questionCount < 4:
        randomCountNumber = random.randint(1, 3)
        if randomCountNumber in questionCountList:
            continue
        questionCountList.append(randomCountNumber)
        #print(questionCount, ". ", questionList[randomCountNumber])
        questionCount += 1

    count += 1


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
questionOneAnswerTwo = Checkbutton(root, text = questionOneInfo[2], textvariable=qOneATwo)
questionOneAnswerTwo.grid(column = 0, row = 2)
questionOneAnswerThree = Checkbutton(root, text = questionOneInfo[3], textvariable=qOneAThree)
questionOneAnswerThree.grid(column = 0, row = 3)

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
questionTwoAnswerTwo = Checkbutton(root, text = questionTwoInfo[2], variable=qTwoATwo)
questionTwoAnswerTwo.grid(column = 0, row = 8)
questionTwoAnswerThree = Checkbutton(root, text = questionTwoInfo[3], variable=qTwoAThree)
questionTwoAnswerThree.grid(column = 0, row = 9)

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
questionThreeAnswerTwo = Checkbutton(root, text = questionThreeInfo[2], variable=qThreeATwo)
questionThreeAnswerTwo.grid(column = 0, row = 14)
questionThreeAnswerThree = Checkbutton(root, text = questionThreeInfo[3], variable=qThreeAThree)
questionThreeAnswerThree.grid(column = 0, row = 15)

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
questionFourAnswerTwo = Checkbutton(root, text = questionFourInfo[2], variable=qFourATwo)
questionFourAnswerTwo.grid(column = 0, row = 20)
questionFourAnswerThree = Checkbutton(root, text = questionFourInfo[3], variable=qFourAThree)
questionFourAnswerThree.grid(column = 0, row = 21)

questionFourSpaceTop = Label(root, text = "")
questionFourSpaceTop.grid(column=0,row=22)
questionFourSpaceBottom = Label(root, text = "")
questionFourSpaceBottom.grid(column=0,row=23)

submitButton = Button(root, text = "Submit", command="getValues")


        


root.mainloop()



# questions are answered and list from dictionary is used to determine answers