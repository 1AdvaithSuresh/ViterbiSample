#!/usr/bin/python3
#Viterbi test
#Advaith Suresh
import sys
import numpy


def saveTags(weightFile):
    with open(weightFile) as f:
        tagList = set() #create a set of unique tags
        for line in f:
            tag = line.strip().split(" ")
            tags = tag[0].split("_")
            tagList.add(tags[1]) #get just the tag name
    #save to a file
    with open("./tagfile","w") as f:
        for tag in tagList:
            f.write(tag+"\n")
        f.close()

def saveWords(trainFile):
    with open(trainFile) as f:
        wordlist = set() #create a set of unique words
        for line in f:
            word = line.strip().split(" ")
            words = word[1::2]
            for w in words:
                wordlist.add(w) #adds word to set (ignores if already present)
    #save to a file
    with open("./wordfile","w") as f:
        for w in wordlist:
            f.write(w+"\n")
        f.close()

def readWords(wordfile): #reads list of words from the wordfile
    with open(wordfile) as f:
        words = [word.strip() for word in f]
    return words

def readTags(tagfile): #reads list of tags from the tagfile
    with open(tagfile) as f:
        tags = [tag.strip() for tag in f]
    return tags

def readWeights(weightFile):
    with open(weightFile) as f:
        #create emission and transition dicts
        E = {} 
        T = {}
        for line in f:
            tag, weight = line.strip().split(" ")
            tag = tag.split("_")
            #split emission and transition
            if (tag[0]=='E'):
                E[tag[1], tag[2]]= float(weight)
            else:
                T[tag[1],tag[2]]=float(weight)
    return E,T


def viterbi(line, E, T, taglist, results):
    #print("Viterbi")
    #delta
    print(line)
    if (line == []):
        print("Empty line")
        return []
    d = numpy.ones((len(taglist),len(line)))*-1*numpy.inf
    #backtrack
    b = numpy.zeros((len(taglist),len(line)))
    sline = " ".join(line)
    for i, word in enumerate(line):
        if (i==0): #first word case
            for idx, tag in enumerate(taglist):
                d[idx,i] = E.get((tag,word),0) #if no emission prob exists for the first word on the tag, set it to 0 (since it is later added)
                b[idx,i] = -1
        else:
            for idx, tag in enumerate(taglist):
                eVal = E.get((tag,word),0) #emission prob from weights file. If none exist, set to 0
                for prev_idx , prev_tag in enumerate(taglist):
                    tVal = T.get((prev_tag,tag),0)  #trans prob from weights file. If non exist set to 0
                    totalProb = d[prev_idx,i-1]+eVal+tVal #delta(i,t) algorithm from class (we loop until we find the max)
                    if (totalProb > d[idx,i]): #find max prob
                        d[idx,i] = totalProb
                        b[idx,i] = prev_idx #keep track of prev tag assigns
    #backtrack to get viterbi_sequence 
    ind = numpy.argmax(d[:,-1]) #index of final tag in sequence
    max_score = d[ind,-1] #max score of prediction
    pred_tags = []
    for ind2 in range(numpy.size(b,axis=1),0,-1): #trace back through b
        pred_tags.append(taglist[int(ind)]) #add tags
        ind = b[int(ind),ind2-1] #get index of previous tag
    pred_tags.reverse() #reverse the list (since we backtracked)
    output = str(max_score) + " " + " ".join(pred_tags)
    print(output)
    results.write(output+"\n")
    return pred_tags


#Loops through the testFile and uses the viterbi alg on each line. Saves output to results
def viterbiUtil(testFile, E, T, taglist): 
    results = open("./results",'w') #results are saved in this file
    with open(testFile) as f:
        for line in f: #use viterbi on each line in the test data
            arrLine = line.strip().split(" ")
            viterbi(arrLine, E, T, taglist, results) #get predicted tags from viterbi 
    results.close()
    print("Viterbi finished")

def main():
    weightFile = sys.argv[1]
    testFile = sys.argv[2]
    saveTags(weightFile) #save list of tags
    tagFile = "./tagfile"
    tags = readTags(tagFile)
    print(tags)
    saveWords(testFile) #saves each unique word in train file
    wordlist = readWords("./wordfile")

    #read weights
    E,T = readWeights(weightFile)
    viterbiUtil(testFile, E, T, tags) #use viterbi to predict tags and save oututs to results
    print("Predictions and confidence scores saved in results.txt")

if __name__=='__main__':
    main()
