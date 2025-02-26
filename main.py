import random
from tkinter import *

root = Tk()

root.title("Biology Beginner Questions")
root.geometry('400x800')

root.mainloop()


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
    questionList = questionsChosen[count]
    print(questionList[0]) #changing this to display with a GUI

    questionCount = 1
    questionCountList = []
    while questionCount < 4:
        randomCountNumber = random.randint(1, 3)
        if randomCountNumber in questionCountList:
            continue
        questionCountList.append(randomCountNumber)
        print(questionCount, ". ", questionList[randomCountNumber])
        questionCount += 1

    count += 1


for i in questionList:
    print(i)




# questions are answered and list from dictionary is used to determine answers