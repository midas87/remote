# Reading words from the code 

fileNote = open('dicBook.txt')
fileRead = fileNote.readlines()

myDict = {}
count = 0

for read in fileRead:
    noWhitespace = read.strip()
    nameList = noWhitespace.split()

    for name in nameList:
        myDict[name] =  myDict.get(name, 0) + 1

maxNum = max(myDict, key=myDict.get)
print(myDict)
print('The most common word is:',maxNum)
