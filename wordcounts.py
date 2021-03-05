# Reading words from the code 

fileNote = open('dicBook.txt')
fileRead = fileNote.readlines()

myDict = {}

for read in fileRead:
    noWhitespace = read.strip()
    nameList = noWhitespace.split()
    #print(nameList)
    for name in nameList:
        #if name not in myDict:
        myDict[name] =  myDict.get(name, 0) + 1

print(myDict)
