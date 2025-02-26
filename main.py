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
questionOneLabel.grid()

questionTwoInfo = questionList[1]
questionTwoLabel = Label(root, text = questionTwoInfo[0])
questionTwoLabel.grid()

questionThreeInfo = questionList[2]
questionThreeLabel = Label(root, text = questionThreeInfo[0])
questionThreeLabel.grid()

questionFourInfo = questionList[3]
questionFourLabel = Label(root, text = questionFourInfo[0])
questionFourLabel.grid()



        


root.mainloop()



# questions are answered and list from dictionary is used to determine answers