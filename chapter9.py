# calling the file and reading from it


dicWord = {}

inputFile = input('Enter the file name: ')
try:
    with open(inputFile) as newFile:
        fileName = newFile.readlines()
        #print(fileName)
except FileNotFoundError:
    print(inputFile, 'file not found')
for run in fileName:
    fileSplit = run.strip().split()
    for word in fileSplit:
        dicWord[word] = dicWord.get(word, 0) + 1
print(dicWord)
print(max(dicWord))
