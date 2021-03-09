# calling the file and reading from it


dicWord = {}

inputFile = input('Enter the file name: ')
try:
    with open(inputFile) as newFile:
        fileName = newFile.readlines()
except FileNotFoundError:
    print(inputFile, 'file not found')
for run in fileName:
    fileSplit = run.strip().split()
    for word in fileSplit:
        dicWord[word] = dicWord.get(word, 0) + 1

getWord = max(dicWord, key=dicWord.get)

print(dicWord)
#print(max(dicWord))

# Find the most common word through loop to get the value for the most common key word

counters = 0

for k, v in dicWord.items():
    if dicWord[k] > counters:
        counters = dicWord[k]
print(counters)

print('The most common word is:',getWord,'with highest number:',counters)
