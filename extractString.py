myStr = 'X-DSPAM-Confidence: 0.8475 '

search = myStr.find(':')
newSearch = search + 2

countFloat = myStr[20:26]



print(search)
print(float(countFloat))
