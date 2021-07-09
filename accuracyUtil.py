#!/usr/bin/python3
import sys

#This seperate util program calculates the accuracy of the first file, compared the the 2nd Gold Standard file
def main():
    guessFile = open(sys.argv[1])
    goldFile = open(sys.argv[2])
    totalTags = 0
    correctTags = 0
    i=1
    for guess, gold in zip(guessFile, goldFile):
        guessArr = guess.strip().split(" ")
        goldArr = gold.strip().split(" ")
        goldArr = goldArr[2::2] #only include every other element starting at 2. Only include tags from test file 
        guessArr.pop(0) #removes the max_score, only includes tags now1
        correctTags = correctTags + sum(t1==t2 for t1,t2 in zip(guessArr,goldArr)) #calculate number of correct tag predictions
        totalTags = totalTags + len(goldArr) #len(goldArr) should always = len(guessArr)
    accuracy = "Accuracy: "+ str(float(correctTags/totalTags)*100)+"%"
    print(accuracy)

main()
