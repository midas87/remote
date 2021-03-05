# Reading words from the code 

fileNote = open('dicBook.txt')
fileRead = fileNote.readlines()

myDict = {}


for read in fileRead:
    noWhitespace = read.strip().split()
    #nameList = noWhitespace.split()

    for name in noWhitespace:
        myDict[name] =  myDict.get(name, 0) + 1

maxNum = max(myDict, key=myDict.get)
print(myDict)
print('The most common word is:',maxNum)
