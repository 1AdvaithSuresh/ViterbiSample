#!/usr/bin/python3
import sys

#This utility program strips all the gold tags from the dataset put as argument. 
def main():
    testFile = sys.argv[1] #argument is the path of the testfile to process
    result = ""
    with open(testFile) as f:
        for line in f:
            arrLine = line.strip().split(" ")
            testLine = arrLine[1::2] #the testline is every other element after the number
            result = result + " ".join(testLine)+"\n"
    with open("./procTest.txt","w") as f: #save file as procTest
        f.write(result)
        f.close()
    print("Test data with stripped gold tags saved at procTest.txt file")

main()
