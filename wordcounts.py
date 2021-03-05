# Reading words from the code 

fileNote = open('dicBook.txt')
fileRead = fileNote.readlines()

for read in fileRead:
    noWhitespace = read.strip()
    nameList = noWhitespace.split()
    print(nameList)

