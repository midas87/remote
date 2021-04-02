# Reading data from Webpage

import urllib.request, urllib.parse, urllib.error

fHand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

count = {}

for line in fHand:
    # print(line.decode().strip())
    splFile = line.decode().strip().split()
    for check in splFile:
        count[check] = count.get(check, 0) + 1

getMax = max(count, key=count.get)
print(count)

# print(getMax)

num = 0

for k, v in count.items():
    if v > num:
        num = v
print('The most common character is:', getMax, 'and the max value is', num)
